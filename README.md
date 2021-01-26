# Datat Release of VALUE (Video And Language Understanding Evaluation) Leaderboard
This is the official data release repository of [VALUE Leaderboard]().
This repository currently supports data downloading of
[TVQA](http://tvqa.cs.unc.edu/), [TVR](https://tvr.cs.unc.edu/), [TVC](https://tvr.cs.unc.edu/tvc.html),
[VIOLIN](https://github.com/jimmy646/violin),
[VLEP](https://github.com/jayleicn/VideoLanguageFuturePred#videolanguagefutureprediction), 
[How2R and How2QA](https://github.com/ych133/How2R-and-How2QA).

![Overview of VALUE]()

The visual frame features are extracted using [SlowFast](https://github.com/facebookresearch/SlowFast) and ResNet-152. Feature extraction code is available at [HERO_Video_Feature_Extractor](https://github.com/linjieli222/HERO_Video_Feature_Extractor)


## Quick Start
We use VIOLIN as an end-to-end example for using this code base.

1. Download raw annotations.
    ```bash
    bash download/download_violin_annotations.sh $PATH_TO_STORAGE
    ```
2. Download visual features.
    ```bash
    bash download/download_violin_features.sh $PATH_TO_STORAGE
    ```
    After downloading you should see the following folder structure:
    ```
    ├── vis_features
    │   └── violin
    |       ├── id2nframe.json
    |       ├── info.json
    |       ├── 2d_resnet
    |       |   ├── xxx.npz
    |       |   ├── yyy.npz
    |       |   └── ...
    |       └── slowfast
    |           ├── xxx.npz
    |           ├── yyy.npz
    |           └── ...
    └── ann
        └── violin
            └── violin_annotations.json
    ```

3. Misc.   
    In case you would like to reproduce the video feature extraction:    
    We provide feature extraction code at [HERO_Video_Feature_Extractor](https://github.com/linjieli222/HERO_Video_Feature_Extractor).
    Please follow the link for instructions to extract both 2D ResNet features and 3D SlowFast features.
    These features are saved as separate .npz files per video.


## Other Tasks

### TVQA, TVR and TVC
1. Download raw annotations.
    ```bash
    bash download/download_tv_annotations.sh $PATH_TO_STORAGE
    ```
       
    Descriptions about raw annotations, please refer to [TVQA](http://tvqa.cs.unc.edu/download_tvqa.html), [TVR](https://github.com/jayleicn/TVRetrieval), [TVC](https://github.com/jayleicn/TVCaption).
2. Download visual features.
    ```bash
    bash download/download_tv_features.sh $PATH_TO_STORAGE
    ```

### VLEP
1. Download raw annotations.
    ```bash
    bash download/download_vlep_annotations.sh $PATH_TO_STORAGE
    ```
       
    Descriptions about raw annotations, please refer to [VLEP Data README](https://github.com/jayleicn/VideoLanguageFuturePred/blob/main/data/README.md).
2. Download visual features.
    ```bash
    bash download/download_vlep_features.sh $PATH_TO_STORAGE
    ```

### How2R and How2QA
1. Download raw annotations.
    ```bash
    bash download/download_vlep_annotations.sh $PATH_TO_STORAGE
    ```
        
    Descriptions about raw annotations, please refer to [How2R_and_How2QA Data README](https://docs.google.com/document/d/1CO9eQPU-1SkJHdDBCzpNK9WMVrpCm8v8zN0qohFVHhs/edit?usp=sharing).
2. Download visual features.    
   Features coming soon ....

## Citation

If you find this code useful for your research, please consider citing:
```
@inproceedings{li2020hero,
  title={HERO: Hierarchical Encoder for Video+ Language Omni-representation Pre-training},
  author={Li, Linjie and Chen, Yen-Chun and Cheng, Yu and Gan, Zhe and Yu, Licheng and Liu, Jingjing},
  booktitle={EMNLP},
  year={2020}
}
```

## License

MIT
