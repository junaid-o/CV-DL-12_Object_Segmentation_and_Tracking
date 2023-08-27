import os
import subprocess
import argparse


# Default values
DEFAULT_DETECT_PREDICTION_WITH_DEEP_SORT_PATH = os.path.abspath(os.path.join('ultralytics', 'yolo', 'v8', 'detect', 'predict.py'))
DEFAULT_SEGMENT_PREDICTION_WITH_DEEP_SORT_PATH = os.path.abspath(os.path.join('ultralytics', 'yolo', 'v8', 'segment', 'predict.py'))

DEFAULT_DETECTION_MODEL_PATH = '../../../../Models_USER/detect/yolov8s.pt'
DEFAULT_SEGMENTATION_MODEL_PATH = '../../../../Models_USER/segment/yolov8s-seg.pt'

DEFAULT_TEST_FILE_PATH = os.path.abspath(os.path.join('input_data_USER', 'test', 'test3.mp4'))

DEFAULT_WORKING_DIRECTORY = os.path.abspath(os.path.join('ultralytics', 'yolo', 'v8', 'segment'))

DEFAULT_TASK_VALUE = "detect"

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Run segment prediction script.')
parser.add_argument('-task', '--task', default=DEFAULT_TASK_VALUE, help='Task to be performed (Detection+DeepSORT Tracking ID + TRAIL) or (Segmentation + DeepSORT Tracking ID + TRAIL)')
parser.add_argument('-ds', '--detection-script', default=DEFAULT_DETECT_PREDICTION_WITH_DEEP_SORT_PATH, help='Path to predict.py script for detection with DeepSORT')
parser.add_argument('-ss', '--segment-script', default=DEFAULT_SEGMENT_PREDICTION_WITH_DEEP_SORT_PATH, help='Path to predict.py script')
parser.add_argument('-dm', '--detection-model', default=DEFAULT_DETECTION_MODEL_PATH, help='Path to detection model')
parser.add_argument('-sm', '--segmentation-model', default=DEFAULT_SEGMENTATION_MODEL_PATH, help='Path to segmentation model')
parser.add_argument('-t', '--test-file', default=DEFAULT_TEST_FILE_PATH, help='Path to test video file')
parser.add_argument('-w', '--working-dir', default=DEFAULT_WORKING_DIRECTORY, help='Working directory having all the files for of YOLOv8 for detection or segmentation along with DeepSORT folder. In this repository this working dir points to ultralytics/yolo/v8/detect or segment')


args = parser.parse_args()

if args.task == "segment":
    print("Segmentation with tracking is runing ...")
    MODEL = args.segmentation_model
    SCRIPT = args.segment_script
    
else:
    print("Detection with tracking is runing ...")
    MODEL = args.detection_model
    SCRIPT = args.detection_script
    


# Build the command to execute predict.py with the necessary arguments
# IF ABOVE LOGIC IS NOT BEING USED THEN JUST COMMENT OUT THE CURRENT COMMAND CODE LINE AND UNCOMMENT THE COMMENTED LINE OF CODE
#command_segment = ['python', args.script, f'model={args.segmentation_model}', f'source={args.test_file}']
command_segment = ['python', SCRIPT, f'model={MODEL}', f'source={args.test_file}']


# Execute the command with the specified working directory
subprocess.call(command_segment, cwd=args.working_dir)

#################################### END ###############################################################
#################################### END ##############################################################










# Construct the path to predict.py
#detection_DeepSORT_prediction_path = os.path.join('ultralytics', 'yolo', 'v8', 'detect', 'predict.py')
#segment_DeepSORT_prediction_path =os.path.abspath(os.path.join('ultralytics', 'yolo', 'v8', 'segment', 'predict.py'))

# Construct the path to yolov8s.pt model
#detection_model_path = '../../../../Models_USER/detect/yolov8s.pt'  # Assuming it's in the root directory
#segmentation_model_path = '../../../../Models_USER/segment/yolov8s-seg.pt'  # Assuming it's in the root directory

# Construct the path to test3.mp4
#test_file_path = os.path.abspath(os.path.join('input_data_USER', 'test', 'test3.mp4'))

# Build the command to execute predict.py with the necessary arguments
#command_detect = ['python', detection_DeepSORT_prediction_path, f'model={detection_model_path}', f'source={test_file_path}']
#command_segment = ['python', segment_DeepSORT_prediction_path, f'model={segmentation_model_path}', f'source={test_file_path}']



# Specify the working directory as the segment directory
#working_directory = os.path.abspath(os.path.join('ultralytics', 'yolo', 'v8', 'segment'))

# Execute the command with the specified working directory
#subprocess.call(command_segment, cwd=working_directory)