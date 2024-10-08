# Boosting VLMs for Histopathology Classification
The official implementation of [*Boosting Vision-Language Models for Histopathology Classification: Predict all at once*](https://arxiv.org/abs/2409.01883).


This repo is built on top of [TransCLIP](https://github.com/MaxZanella/transduction-for-vlms).


## Table of Contents

1. [Introduction](#introduction) 
2. [Installation](#installation) 
3. [Usage](#usage)
4. [Citation](#citation)
5. [Contact](#contact) 


---

## Introduction

### Short abstract
We enhance vision-language models (VLMs) for histopathology by introducing a transductive approach that leverages text-based predictions and patch affinity in its objective funtion. Histo-TransCLIP improves zero-shot classification accuracy without additional labels and is able to manage more than 100,000 patches in seconds.

### Visual explanation
<p align="center">
  <img src="drawing.png" alt="Histo-TransCLIP in action" width="700" height="315">
  <br>
  <em>Figure 1: VLMs leverage textual descriptions of each class to generate pseudo-labels without any manual annotation. These initial predictions are then refined by Histo-TransCLIP by leveraging the data structure thanks to the Laplacian term as well as the text-based predictions.</em>
</p>

### Results

|Dataset | Method | CLIP | Quilt-B16 | Quilt-B32 |  PLIP | CONCH |
|----------|----------|----------|----------|----------|----------|----------|
| SICAP-MIL  | Zero-shot | **29.85** | 40.44 | **35.04** | 46.84 | 27.71 |
| | Histo-TransCLIP |  24.72 | **58.49** | 28.18 | **53.23** | **32.58** |
| LC(Lung)   | Zero-shot | **31.46** | 43.00 | 76.24 |  84.96 | 84.81 |
| | Histo-TransCLIP | 25.62 | **50.53** | **93.93** | **93.80** | **96.29** | 
| SKINCANCER   | Zero-shot | 4.20 | 15.38 | 39.71 | 22.90 | 58.53 |
| | Histo-TransCLIP |  **11.46** | **33.33** | **48.80** | **36.72** | **66.22** |
| NCT-CRC   | Zero-shot | 25.39 | 29.61 |  53.73 | 63.17 | 66.27 |
| | Histo-TransCLIP | **39.61** | **48.40** | **58.13** | **77.53** | **70.36** |



## Installation

### Environment
Create a Python environment with your favorite environment manager. For example, with `conda`: 
```bash
conda create -y --name TransCLIP python=3.10.0
conda activate TransCLIP
pip3 install -r requirements.txt
```
And install Pytorch according to your configuration:
```bash
pip3 install torch==2.0.1 torchaudio==2.0.2 torchvision==0.15.2
```
## Datasets

Install each dataset follow the instructions in [DATASETS.md](https://github.com/FereshteShakeri/Histo-TransCLIP/blob/main/DATASETS.md).

## Models

Clone repository of each Medical VLM inside Histo-TransCLIP directory:

```bash
cd Histo-TransCLIP
git clone https://github.com/mahmoodlab/CONCH.git
git clone https://github.com/PathologyFoundation/plip.git
git clone https://github.com/mlfoundations/open_clip.git
```

Download Quilt-1m models from [hugginface](https://huggingface.co/wisdomik/QuiltNet-B-32).  


## Usage
We present the basic usage to get started with our method. You have to pass the datasets folder path and the pre-computed prototypes folder path. Every script has pre-set parameters but you can change them manually.

### Histo VLM + TransCLIP-ZS
TransCLIP-ZS based on the textual embeddings of the zero-shot histological models.

- **Zero-Shot setting**

Here is an example for the NCT dataset, with the Quilt-1m architecture, and seed 1:
```bash
python3 main.py --root_path /path/to/datasets/folder --dataset nct --method TransCLIP  --seed 1 --model Quilt
```

To run the whole experiment, use the following command:
```bash
bash ./scripts/transclip_zs.sh /path/to/datasets/folder Quilt
```

## Citations

If you find this repository useful, please consider citing our paper:
```
@article{zanella2024histo,
  title={Boosting Vision-Language Models for Histopathology Classification: Predict all at once},
  author={Zanella, Maxime and Shakeri, Fereshteh and Huang, Yunshi and Bahig, Houda and Ayed, Ismail Ben},
  journal={arXiv preprint arXiv:2409.01883},
  year={2024}
}
```
Please also consider citing the original TransCLIP paper:
```
@article{zanella2024boosting,
  title={Boosting Vision-Language Models with Transduction},
  author={Zanella, Maxime and G{\'e}rin, Beno{\^\i}t and Ayed, Ismail Ben},
  journal={arXiv preprint arXiv:2406.01837},
  year={2024}
}
```

## Contact

For any inquiries, feel free to [create an issue](https://github.com/FereshteShakeri/Histo-TransCLIP/issues) or contact us at [maxime.zanella@uclouvain.be](mailto:maxime.zanella@uclouvain.be) and [fereshteh.shakeri.1@etsmtl.net](mailto:fereshteh.shakeri.1@etsmtl.net)



