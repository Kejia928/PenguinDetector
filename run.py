import os

import yoloV5 as Yolo


def run_yolo_detector(video_path, model_path):
    """
    Before use this function, set the conda encironment to the yoloV5
    conda activate yoloV5
    """

    # get each frame image from video
    ori_path = Yolo.video2img(video_path)
    # run yolo detector
    yolo_pic = Yolo.yolo_detection(ori_path, model_path)
    # transfer the result image to the video
    Yolo.make_video(yolo_pic)


if __name__ == '__main__':
    run_yolo_detector("video/20170929_F_5_3.mp4", "model/yolov5s_best.pt")
