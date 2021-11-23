import random
import os
import shutil


path = "dataset/original"
filenames = []

for file in os.walk(path):
    filenames.append(file)  # list of all images

random.shuffle(filenames)  # randomly shuffles the ordering of filenames

split_1 = int(0.8 * len(filenames))  # 80% train
split_2 = int(1.0 * len(filenames))  # 20% val

train_filenames = filenames[:split_1]
val_filenames = filenames[split_1:split_2]

# move files for the train and val folders
for file in train_filenames:
    shutil.move(file, "dataset/train")

for file in val_filenames:
    shutil.move(file, "dataset/val")
