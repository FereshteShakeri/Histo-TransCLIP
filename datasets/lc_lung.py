import os
import copy
import math
import random
from collections import defaultdict, OrderedDict

import torch
import torchvision
import torchvision.transforms as transforms
from .utils import Datum, DatasetBase, read_json, write_json, build_data_loader, listdir_nohidden



TO_BE_IGNORED = ["README.txt"]

class_names = ['Lung adenocarcinoma', 'Benign lung’', 'Lung squamous cell carcinoma']

labels_dict = {"lung_aca": "Lung adenocarcinoma", "lung_n": "Benign lung", 
                "lung_scc": "Lung squamous cell carcinoma"}

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


class LCLUNG(DatasetBase):

    dataset_dir = "LC25000"

    def __init__(self, root, preprocess):
        
        self.dataset_dir = os.path.join(root, self.dataset_dir)
        self.image_dir = os.path.join(self.dataset_dir, "lung")

        # text_file = os.path.join(self.dataset_dir, "classnames.txt")
        # classnames, labels = self.read_classnames(text_file)
        self.template = templates

        train = val = test = self.read_data()

        super().__init__(train_x=train, val=val, test=test)

    def read_data(self):
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


        return items

    def generate_fewshot_dataset_(self,num_shots, split):

            print('num_shots is ',num_shots)
            if split == "train":
                few_shot_data = self.generate_fewshot_dataset(self.train_x, num_shots=num_shots)
            elif split == "val":
                few_shot_data = self.generate_fewshot_dataset(self.val, num_shots=num_shots)
        
            return few_shot_data