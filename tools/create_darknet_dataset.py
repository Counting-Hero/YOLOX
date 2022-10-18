from operator import le
import os
import glob
from random import shuffle
import shutil

train_val_split = 0.8

root_folder = "/home/simen/Data/tire_dataset/data"
root_folder_name = root_folder.split(os.sep)[-1]
data_folder = os.path.join(root_folder, "data")
if not os.path.exists(data_folder):
    os.mkdir(data_folder)

# move all the data into a folder called data, we keep a list of all the images for later
images = []
for root, dirs, files in os.walk(root_folder):
    for file in files:
        new_file = os.path.join(data_folder, file)
        if new_file.endswith("class.names"):
            continue
        elif new_file.endswith("labels.txt"):
            shutil.move(os.path.join(root, file), os.path.join(root, "class.names"))
            continue
        elif new_file.endswith(".png") or new_file.endswith(".jpg"):
            images.append(new_file)
        shutil.move(os.path.join(root, file), new_file)

# create the train, val, test files
shuffle(images)
split_idx = int(len(images)*train_val_split)
with open(os.path.join(root_folder, "train.txt"), "w") as f:
    for image in images[split_idx:]:
        f.write(image + "\n")
with open(os.path.join(root_folder, "val.txt"), "w") as f:
    for image in images[:split_idx]:
        f.write(image + "\n")
open(os.path.join(root_folder, "test.txt"), 'w').close()

with open(os.path.join(root_folder, "class.names"), "r") as f:
    num_classes = len(f.readlines())

data_file_content = f"""classes = {num_classes}
train  = {os.path.join(root_folder_name, "train.txt")}
valid  = {os.path.join(root_folder_name, "val.txt")}
test = {os.path.join(root_folder_name, "test.txt")}
names = {os.path.join(root_folder_name, "class.names")}
"""

with open(os.path.join(root_folder, "dataset.data"), "w") as f:
    f.write(data_file_content)