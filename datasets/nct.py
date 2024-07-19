import os
import copy
import math
import random
from collections import defaultdict, OrderedDict

import torch
import torchvision
import torchvision.transforms as transforms
from .utils import Datum, DatasetBase, read_json, write_json, build_data_loader, listdir_nohidden


labels = ['ADI', 'BACK', 'DEB', 'LYM', 'MUC', 'MUS', 'NORM', 'STR', 'TUM']

TO_BE_IGNORED = ["README.txt"]

class_names = ["Adipose", "Background", "Debris", "Lymphocytes", "Mucus", "Smooth muscle",
           "Normal colon mucosa", "Cancer-associated stroma", 
           "Colorectal adenocarcinoma epithelium"]

labels_dict = {"ADI": "Adipose", "BACK": "Background", "DEB": "Debris", 
               "LYM": "Lymphocytes", "MUC": "Mucus", "MUS": "Smooth muscle",
               "NORM": "Normal colon mucosa", "STR": "Cancer-associated stroma", 
                "TUM": "Colorectal adenocarcinoma epithelium"}

templates = [
            "{}.",
            "a photomicrograph showing {}.",
            "a photomicrograph of {}.",
            "an image of {}.",
            "an image showing {}.",
            "an example of {}.",
            "{} is shown.",
            "this is {}.",
            "there is {}.",
            "a histopathological image showing {}.",
            "a histopathological image of {}.",
            "a histopathological photograph of {}.",
            "a histopathological photograph showing {}.",
            "shows {}.",
            "presence of {}.",
            "{} is present.",
            "an H&E stained image of {}.",
            "an H&E stained image showing {}.",
            "an H&E image showing {}.",
            "an H&E image of {}.",
            "{}, H&E stain.",
            "{}, H&E."
]


class NCT(DatasetBase):

    dataset_dir = "NCT-CRC-HE-100K"

    def __init__(self, root, preprocess):
        
        self.dataset_dir = os.path.join(root, self.dataset_dir)
        self.image_dir = os.path.join(self.dataset_dir, "NCT-CRC-HE-100K")
        self.image_dir_test = os.path.join(self.dataset_dir, "CRC-VAL-HE-7K")

        text_file = os.path.join(self.dataset_dir, "classnames.txt")
        # classnames, labels = self.read_classnames(text_file)
        self.template = templates
        train_path = os.path.join(self.dataset_dir, "NCT-CRC-HE-100K")
        test_path = os.path.join(self.dataset_dir, "CRC-VAL-HE-7K")

        train, val = self.read_data(train_path, "train")
        test,_ = self.read_data(test_path, "test")

        super().__init__(train_x=train, val=val, test=test)

    def read_data(self, data_path, split):
        
        if split == "test":
            image_dir = self.image_dir
        else:
            image_dir = self.image_dir
        folders = listdir_nohidden(image_dir, sort=True)
        folders = [f for f in folders if f not in TO_BE_IGNORED]
        items = []

        data_count = 0
        for label, folder in enumerate(folders):

            imnames = listdir_nohidden(os.path.join(image_dir, folder))
            classname = labels_dict[folder]
            for imname in imnames:
                impath = os.path.join(image_dir, folder, imname)            
                item = Datum(impath=impath, label=label, classname=classname)
                items.append(item)
                data_count += 1
        print(data_count)        
        if split == "train":
            random.shuffle(items)
            return items[:int(data_count/2)], items[int(data_count/2):]
        elif split == "test":
            random.shuffle(items)
            return items[:40000], items[40000:]
