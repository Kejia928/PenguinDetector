import os

# The dataset repo will be cloned at the first time of training
if not os.path.exists(os.path.abspath("local-detection-dataset")):
    os.system("git clone https://github.com/Kejia928/local-detection-dataset")

data_config = "local-detection-dataset/data.yaml"
weight = "yolov5s.pt"
cfg = "yolov5/models/yolov5s.yaml"
save_period = "200"
img_size = "640"
epoch = "1"

command = f"python yolov5/train.py --data {data_config} --weights {weight} --cfg {cfg} --save-period={save_period} --img {img_size} --epochs {epoch}"
os.system(command)
