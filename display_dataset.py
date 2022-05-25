#!/usr/bin/env python3
"""! @brief This python script displays some entries of the BeeDataset """
##
# @file display_dataset.py
#
# @brief Displays some elements of the bee_dataset
#
# @section authors Author(s)
# - Created by Fabian Hickert, 2021
#
import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow_datasets as tfds

print("="*30)
try:
    from bee_dataset import BeeDataset
    print("Using local Bee-Dataset")
except:
    print("Using Bee-Dataset from TFDS installation")
print("="*30)
    
ROWS = 4
COLUMNS = 5

# Load via TFDS
ds = tfds.load('bee_dataset/bee_dataset_300',
        batch_size=(ROWS * COLUMNS),
        as_supervised=True,
        split="train")

# Display some images using pyplot 
figure, axis = plt.subplots(ROWS, COLUMNS, figsize=(24, 15))
for example in ds.shuffle(buffer_size=(ROWS * COLUMNS)).prefetch(tf.data.experimental.AUTOTUNE).take(1):
    for r in range(ROWS):
        for c in range(COLUMNS):
            num = (r*COLUMNS)+c
            text = ""
            for char in ["cooling_output", "pollen_output", "varroa_output", "wasps_output"]:
                if (example[1][char][num] == 1):
                    text += char.replace("_output", "") + " "
            
            axis[r, c].imshow(example[0][num])
            axis[r, c].set_title(text, fontsize = 20)

plt.show()
