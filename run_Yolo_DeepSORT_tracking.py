import os
import subprocess

# Construct the path to predict.py
#detection_DeepSORT_prediction_path = os.path.join('ultralytics', 'yolo', 'v8', 'detect', 'predict.py')
segment_DeepSORT_prediction_path =os.path.abspath(os.path.join('ultralytics', 'yolo', 'v8', 'segment', 'predict.py'))

# Construct the path to yolov8s.pt model
detection_model_path = '../../../../Models_USER/detect/yolov8s.pt'  # Assuming it's in the root directory
segmentation_model_path = '../../../../Models_USER/segment/yolov8s-seg.pt'  # Assuming it's in the root directory

# Construct the path to test3.mp4
test_file_path = os.path.abspath(os.path.join('input_data_USER', 'test', 'test3.mp4'))

# Build the command to execute predict.py with the necessary arguments
#command_detect = ['python', detection_DeepSORT_prediction_path, f'model={detection_model_path}', f'source={test_file_path}']
command_segment = ['python', segment_DeepSORT_prediction_path, f'model={segmentation_model_path}', f'source={test_file_path}']



# Specify the working directory as the segment directory
working_directory = os.path.abspath(os.path.join('ultralytics', 'yolo', 'v8', 'segment'))

# Execute the command with the specified working directory
subprocess.call(command_segment, cwd=working_directory)