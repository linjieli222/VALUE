import h5py
import os
import numpy as np
from tqdm import tqdm 
resNet_feat = h5py.File("/pretrain/tvqa/tvr_feature_release/video_feature/tvr_resnet152_rgb_max_cl-1.5.h5", "r")
data_len = len(resNet_feat)
output_dir = "/storage/resnet_features/tv/"
os.makedirs(output_dir, exist_ok=True)
for key in tqdm(resNet_feat.keys()):
    curr_resnet_feat = np.array(resNet_feat.get(key), dtype="float32")
    tv_name = key.split("_")[0]
    if tv_name not in ["castle", "friends", "grey", "house", "met"]:
        tv_name = "bbt"
    os.makedirs(F"{output_dir}/{tv_name}", exist_ok=True)
    output_feat_path = os.path.join(output_dir, tv_name, key+".npz")
    np.savez(output_feat_path, features=curr_resnet_feat)
    # curr_feat = np.load(curr_feat_path)["features"].astype("float32")
    # resNet_feat_len = curr_resnet_feat.shape[0]
    # new_feat = curr_feat[:resNet_feat_len]
    # new_feat = np.concatenate(
    #     (curr_resnet_feat, curr_feat[:resNet_feat_len]), axis=1)
resNet_feat.close()
