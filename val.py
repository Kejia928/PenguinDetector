import os

# The dataset repo will be cloned at the first time of training
if not os.path.exists(os.path.abspath("local-detection-dataset")):
    os.system("git clone https://github.com/Kejia928/local-detection-dataset")

weight = "model/yolov5s_best.pt"
data_config = "local-detection-dataset/data.yaml"
img_size = "640"

commond = f"python yolov5/val.py --weights {weight} --data {data_config} --img {img_size}"
os.system(commond)
