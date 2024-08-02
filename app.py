import cv2
import numpy as np
from flask import Flask, request, jsonify
import torch
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
import logging

app = Flask(__name__)

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Detectron2 model
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")
cfg.MODEL.DEVICE = "cpu"  # Set to CPU
predictor = DefaultPredictor(cfg)

@app.route('/detect', methods=['POST'])
def detect_objects():
    app.logger.debug('Received request')
    if 'image' not in request.files:
        app.logger.error('No image file provided')
        return jsonify({'error': 'No image file provided'}), 400
    
    file = request.files['image']
    try:
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    except Exception as e:
        app.logger.error(f'Error decoding image: {e}')
        return jsonify({'error': 'Error decoding image'}), 500
    
    try:
        outputs = predictor(img)
    except Exception as e:
        app.logger.error(f'Error during prediction: {e}')
        return jsonify({'error': 'Error during prediction'}), 500
    
    # Process the outputs
    instances = outputs["instances"].to("cpu")
    boxes = instances.pred_boxes.tensor.numpy().tolist()
    classes = instances.pred_classes.numpy().tolist()
    scores = instances.scores.numpy().tolist()
    
    # Get class names
    class_names = MetadataCatalog.get(cfg.DATASETS.TRAIN[0]).thing_classes
    
    results = []
    for box, class_id, score in zip(boxes, classes, scores):
        results.append({
            'box': box,
            'class': class_names[class_id],
            'score': float(score)
        })
    
    app.logger.debug(f'Detections: {results}')
    return jsonify({'detections': results})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)