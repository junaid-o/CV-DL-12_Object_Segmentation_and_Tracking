# Object Detection or Segmentation With Tracking and Counting

[![Python 3.10.12](https://img.shields.io/badge/python-3.10.12-blue.svg)](https://www.python.org/downloads/release/python-31012/)
![Static Badge](https://img.shields.io/badge/YOLO-8-orange.svg)
![Static Badge](https://img.shields.io/badge/DeepSORT-purple.svg)


## Table of Contents

- [Features](#features)
- [Installation](#installation-and-usage)

## Features

Outline the key features of your project:

- Object detection using YOLOv8
- Object segmentation using YOLOv8
- Object tracking using DeepSORT
- Tracking with IDs and Trail
- Object Counting

## Installation and Usage

To use the Coccidiosis Detection Web App, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/junaid-o/CV-DL-12_Object_Segmentation_and_Tracking.git
   cd CV-DL-12_Object_Segmentation_and_Tracking
   ```

2. **Create a conda environment after opening the repository**

   ```bash
   conda create --prefix ./envYOLO8 python=3.10.12 -y
   ```

   ```bash
   conda activate ./envYOLO8
   ```

3. **Install Dependencies:**

   ```bash
   pip install -e '.[dev]'
   ```

   ```bash
   pip install easydict
   ```
4. **Test File Location:**

   Keep all your test video files inside `input_data_USER/test`

5. **Run From Terminal:**

 - When running without any argument it will take dafault values for model, test files etc

    ```bash
    python run_Yolo_DeepSORT_tracking.py 
    ```
 - For help

    ```bash
    python run_Yolo_DeepSORT_tracking.py -h
    ```
    
    
    OPTIONS AVAILABLE FOR ARGUMENTS
    
    ```bash

    $ python run_Yolo_DeepSORT_tracking.py -h
    usage: run_Yolo_DeepSORT_tracking.py [-h] [-task TASK] [-ds DETECTION_SCRIPT] [-ss SEGMENT_SCRIPT]
                                        [-dm DETECTION_MODEL] [-sm SEGMENTATION_MODEL] [-t TEST_FILE] [-w WORKING_DIR]

    Run segment prediction script.

    options:
    -h, --help            show this help message and exit
    -task TASK, --task TASK
                            Task to be performed (Detection+DeepSORT Tracking ID + TRAIL) or (Segmentation + DeepSORT
                            Tracking ID + TRAIL)
    -ds DETECTION_SCRIPT, --detection-script DETECTION_SCRIPT
                            Path to predict.py script for detection with DeepSORT
    -ss SEGMENT_SCRIPT, --segment-script SEGMENT_SCRIPT
                            Path to predict.py script
    -dm DETECTION_MODEL, --detection-model DETECTION_MODEL
                            Path to detection model
    -sm SEGMENTATION_MODEL, --segmentation-model SEGMENTATION_MODEL
                            Path to segmentation model
    -t TEST_FILE, --test-file TEST_FILE
                            Path to test video file
    -w WORKING_DIR, --working-dir WORKING_DIR
                            Working directory having all the files for of YOLOv8 for detection or segmentation along with
                            DeepSORT folder. In this repository this working dir points to ultralytics/yolo/v8/detect or
                            segment

    ```

6. **View Output Video Files:**

    Find output files in `run folder`
