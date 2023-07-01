import os
import argparse
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
    parser = argparse.ArgumentParser(description='YOLO Detector')
    parser.add_argument('--video', type=str, help='Path to the video file')
    parser.add_argument('--model', type=str, help='Path to the YOLO model file')
    args = parser.parse_args()

    video_file = args.video if args.video else "video/SP_N5_20170808_2_4.mp4"
    model_file = args.model if args.model else "model/yolov5s_best.pt"

    run_yolo_detector(video_file, model_file)
