# How to install datasets

We recommend placing all datasets in a single folder. Follow the instructions below to organize the datasets without needing to change the source code. The file structure is as follows:

```
$DATA/
|–– NCT-CRC-HE-100K/
|–– SICAP_MIL/
|–– LC25000/
|–– skincancer/
```

Detailed instructions for preparing each dataset are provided below. To ensure reproducibility and enable fair comparisons in future work, we offer fixed train/validation/test splits for all datasets. These fixed splits are either taken from the original datasets (when available) or created by us.

### NCT
- Create a folder named `NCT-CRC-HE-100K/`.
- Download the the train set `NCT-CRC-HE-100K.zip` and val set `CRC-VAL-HE-7K.zip` from the [official website](https://zenodo.org/records/1214456) and extract them under `NCT-CRC-HE-100K/`. The directory structure should look like:
```
NCT-CRC-HE-100K/
|–– CRC-VAL-HE-7K/
|–– NCT-CRC-HE-100K/
```

### SICAP_MIL
- Create a folder named `SICAP_MIL/`.
- Download the the dataset from the [official github](https://github.com/jusiro/mil_histology) and extract it under `SICAP_MIL/`. The directory structure should look like:
```
SICAP_MIL/
|–– annotation_masks/
|–– dataframes/
|–– patches/
|–– slides/
```

### LC_LUNG
- Create a folder named `LC25000/`.
- Download the the dataset from the [official website](https://github.com/tampapath/lung_colon_image_set) and extract it under `LC25000/`. The directory structure should look like:
```
LC25000/
|–– colon/
|–– lung/
```
Here we only use the lung subset.

### skincancer
- Create a folder named `skincancer/`.
- Download the dataset from the [official website](https://zenodo.org/records/1214456) and extract it under `skincancer/`. The directory structure should look like:
```
skincancer/
|–– data/
|   |–– class_dict.json 
|   |–– tiles/
|   |–– tiles-v2.csv 
```