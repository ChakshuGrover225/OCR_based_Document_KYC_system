from ultralytics import YOLO
import os

def yolo_cropping_2(grey_img_dir):
    model_path = r'app\resources\aadhar_best_21.pt'
    model_1 = YOLO(model_path)
    conf_score = 0.40

    # Define output folder correctly
    project_dir = os.path.join(os.getcwd()+"/uploaded_images", "yolo_results")  # base folder
    run_name = "yolo_output"  # subfolder

    # Run YOLO inference
    model_1(
        source=grey_img_dir,
        save=True,
        project=project_dir,     # base folder
        name=run_name,           # subfolder
        exist_ok=True,           # overwrite if folder exists
        boxes=False,
        save_crop=True,
        save_txt=True,
        conf=conf_score,
        show_labels=False,
        show_conf=False,
    )

print("hey")

yolo_cropping_2(r"uploaded_images\processed_image.jpg")


yolo_img_path = r'uploaded_images\yolo_results\yolo_output\crops'
jpg_files = []

for root, dirs, files in os.walk(yolo_img_path):
    for file in files:
        if file.lower().endswith(".jpg"):
            jpg_files.append(os.path.join(root, file))

print(jpg_files , end="\n")

import shutil
import os

folder_path = r"uploaded_images\yolo_results"


if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
    print(f"Deleted folder: {folder_path}")
else:
    print("Folder does not exist.")
