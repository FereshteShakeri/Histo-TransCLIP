import torch
import torchvision.transforms as transforms
from .sicapv2 import SicapV2
from .sicap_mil import SicapMIL
from .skincancer import SKIN
from .nct import NCT
from .lc_lung import LCLUNG

from .utils import *

dataset_list = {
                "sicapv2": SicapV2,
                "sicap_mil": SicapMIL,
                "skincancer": SKIN,
                "nct": NCT,
                "lc_lung": LCLUNG,
                }


def get_all_dataloaders(cfg, preprocess):
    dataset_name = cfg['dataset']

    if dataset_name.startswith('imagenet'):
        dataset = dataset_list[dataset_name](cfg['root_path'], cfg['shots'], preprocess=preprocess, train_preprocess=None, test_preprocess=None, load_cache=cfg['load_cache'], load_pre_feat=cfg['load_pre_feat'])
        test_loader = torch.utils.data.DataLoader(dataset.test, batch_size=64, num_workers=8, shuffle=False)
        train_loader = None
        val_loader = None
        if cfg['shots'] > 0:
            train_loader = torch.utils.data.DataLoader(dataset.train, batch_size=256, num_workers=8, shuffle=False)
            val_loader = torch.utils.data.DataLoader(dataset.val, batch_size=64, num_workers=8, shuffle=False)

    else:
        dataset = dataset_list[dataset_name](cfg['root_path'], cfg['shots'])
        val_loader = build_data_loader(data_source=dataset.val, batch_size=64, is_train=False, tfm=preprocess,
                                       shuffle=False)
        test_loader = build_data_loader(data_source=dataset.test, batch_size=64, is_train=False, tfm=preprocess,
                                        shuffle=False)
        train_loader = None
        if cfg['shots'] > 0:

            train_loader = build_data_loader(data_source=dataset.train_x, batch_size=256, tfm=preprocess,
                                                   is_train=False, shuffle=False)

    return train_loader, val_loader, test_loader, dataset


