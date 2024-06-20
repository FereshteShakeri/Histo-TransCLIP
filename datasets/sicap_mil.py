import os
import random
import pandas as pd

from .utils import Datum, DatasetBase

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



class SicapMIL(DatasetBase):
    
    image_dir = "SICAP_MIL"
    
    def __init__(self, root, num_shots):

        self.image_dir = os.path.join(root, self.image_dir)

        csv_file = os.path.join(self.image_dir, "dataframes", "gt_test_patches.xlsx")
        self.data_test = pd.read_excel(csv_file)

        # drop all columns except image_name and the label columns
        label_columns = ['NC', 'G3', 'G4', 'G5']  # , 'G4C']
        self.data_test = self.data_test[['image_name'] + label_columns]

        # get the index of the maximum label value for each row
        self.data_test['labels'] = self.data_test[label_columns].idxmax(axis=1)

        # replace the label column values with categorical values
        self.cat_to_num_map = label_map = {'NC': 0, 'G3': 1, 'G4': 2, 'G5': 3}  # , 'G4C': 4}
        self.data_test['labels'] = self.data_test['labels'].map(label_map)

        self.image_paths_test = self.data_test['image_name'].values
        self.labels_test = self.data_test['labels'].values
        self.classes = ["non-cancerous well-differentiated glands",
                "gleason grade 3 with atrophic well differentiated and dense glandular regions",
                "gleason grade 4 with cribriform, ill-formed, large-fused and papillary glandular patterns",
                "gleason grade 5 with nests of cells without lumen formation, isolated cells and pseudo-roseting patterns",
                ]

        self.template = templates

        test = []
        for i in range(len(self.data_test)):
            impath = os.path.join(self.image_dir, 'patches', self.data_test.at[i, "image_name"])
            item = Datum(
                impath=impath,
                label=int(self.data_test.at[i, "labels"]),
                classname=self.classes[self.data_test.at[i, "labels"]]
            )
            test.append(item)
        # Only testing for zero-shot setting
        train = val = test
            
        super().__init__(train_x=train, val=val, test=test)
        


