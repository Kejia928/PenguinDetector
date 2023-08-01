# PenguinDetector

This penguin detector model is implemented based on the YOLOv5 architecture developed by Ultralytics and rooted in the classic real-time object detection algorithm YOLO.

## Usage
```bash
git clone https://github.com/Kejia928/PenguinDetector.git
```

## Set up environment
The following shows the Python environment requirements for this detector. This is shown in the `yolov5` folder `requirements.txt`.

The requirement can be directly installed by using pip:
```bash
cd yolov5
pip install -r requirements.txt
```

```
# YOLOv5 requirements
# Usage: pip install -r requirements.txt

# Base ------------------------------------------------------------------------
gitpython
ipython  # interactive notebook
matplotlib>=3.2.2
numpy>=1.18.5
opencv-python>=4.1.1
Pillow>=7.1.2
psutil  # system resources
PyYAML>=5.3.1
requests>=2.23.0
scipy>=1.4.1
thop>=0.1.1  # FLOPs computation
torch>=1.7.0  # see https://pytorch.org/get-started/locally (recommended)
torchvision>=0.8.1
tqdm>=4.64.0
# protobuf<=3.20.1  # https://github.com/ultralytics/yolov5/issues/8012

# Logging ---------------------------------------------------------------------
tensorboard>=2.4.1
# clearml>=1.2.0
# comet

# Plotting --------------------------------------------------------------------
pandas>=1.1.4
seaborn>=0.11.0

# Export ----------------------------------------------------------------------
# coremltools>=6.0  # CoreML export
# onnx>=1.12.0  # ONNX export
# onnx-simplifier>=0.4.1  # ONNX simplifier
# nvidia-pyindex  # TensorRT export
# nvidia-tensorrt  # TensorRT export
# scikit-learn<=1.1.2  # CoreML quantization
# tensorflow>=2.4.1  # TF exports (-cpu, -aarch64, -macos)
# tensorflowjs>=3.9.0  # TF.js export
# openvino-dev  # OpenVINO export

# Deploy ----------------------------------------------------------------------
# tritonclient[all]~=2.24.0

# Extras ----------------------------------------------------------------------
# mss  # screenshots
# albumentations>=1.0.3
# pycocotools>=2.0.6  # COCO mAP
# roboflow
# ultralytics  # HUB https://hub.ultralytics.com
```

## Detect
To detect on a single image, fill the 'image path' in the below command line:
```bash
python yolov5/detect.py --weights model/yolov5s_best.pt --source 'image path' --save-txt
```

To detect on a video:

Directly run the `run.py`, specifying path to video file after the `--video` argument:
```bash
python run.py --video video/SP_N5_20170808_2_4.mp4
```

To specify a custom YOLO model file for detecting on a video, include the `--model` argument (default best model is used below):
```bash
python run.py --video video/SP_N5_20170808_2_4.mp4 --model model/yolov5s_best.pt
```

## Training
Clone the dataset:
```bash
git clone https://github.com/Kejia928/local-detection-dataset.git
```

Run the yolov5 `train.py`:
```bash
python yolov5/train.py --data local-detection-dataset/data.yaml --weights yolov5s.pt --cfg yolov5/models/yolov5s.yaml --save-period=200 --img 640 --epochs 1000
```

## Test
Run the yolov5 `val.py`:
```bash
python yolov5/val.py --weights model/yolo/yolov5n_best.pt --data local-detection-dataset/data.yaml --img 640
```
