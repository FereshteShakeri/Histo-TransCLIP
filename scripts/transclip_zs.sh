#!/bin/bash

DATA=$1
ARCH=$2

datasets=("nct" "skincancer" "lc_lung" "sicap_mil")
seeds=("1" "2" "3")


for dataset in "${datasets[@]}"; do
  for seed in "${seeds[@]}"; do
    python3 main.py --root_path "${DATA}" \
                    --dataset "$dataset" \
                    --method TransCLIP \
                    --model ${ARCH} \
                    --seed "$seed"
  done
done