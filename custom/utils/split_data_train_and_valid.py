import random
import os
import shutil


path = "datasets/original/"
filenames, jsonnames = [], []

# SPLITING IMAGES
for lstfile in os.walk(path):
    for file in lstfile[2]:
        if ".JPG" in file:
            filenames.append(file)  # list of all images
        elif ".json" in file:
            jsonnames.append(file)

random.shuffle(filenames)  # randomly shuffles the ordering of filenames

split_1 = int(0.8 * len(filenames))  # 80% train
split_2 = int(1.0 * len(filenames))  # 20% val

train_filenames = filenames[:split_1]
val_filenames = filenames[split_1:split_2]

# move files for the train and val folders
for file in train_filenames:
    shutil.move(path+""+file, "datasets/train")

for file in val_filenames:
    shutil.move(path+""+file, "datasets/val")

# JSON FILES
for file in jsonnames:
    shutil.copy(path+""+file, "datasets/train")
    shutil.move(path+""+file, "datasets/val")
