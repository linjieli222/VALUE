"""
convert feature npz file to lmdb
"""
import argparse
import json
import multiprocessing as mp
import os

from cytoolz import curry
import numpy as np
from tqdm import tqdm
import pickle as pkl


@curry
def load_npz(fname):
    try:
        vid, nframes, slowfast_fname, resnet_fname, _ = fname
    except Exception:
        vid, nframes, slowfast_fname, resnet_fname = fname
    try:
        if nframes == 0:
            raise ValueError('wrong ndim')
        slowfast_features = np.load(
            slowfast_fname, allow_pickle=True)["features"]
        if slowfast_features.dtype == np.float16:
            slowfast_features = slowfast_features.astype(np.float32)
        resnet_features = np.load(
            resnet_fname, allow_pickle=True)["features"]
        if resnet_features.dtype == np.float16:
            resnet_features = resnet_features.astype(np.float32)
        resnet_features = resnet_features[:nframes, :]
        slowfast_features = slowfast_features[:nframes, :]
        dump = {"2d": resnet_features, "3d": slowfast_features}
    except Exception as e:
        # corrupted file
        print(f'corrupted file {vid}', e)
        dump = {}
        nframes = 0

    return vid, dump, nframes


def main(opts):
    output_dir = f'{opts.output}/{opts.dataset}/{opts.feat_version}_{opts.frame_length}'
    os.makedirs(output_dir, exist_ok=True)
    output_dir_2d = f'{output_dir}/2d_resnet/'
    os.makedirs(output_dir_2d, exist_ok=True)
    output_dir_3d = f'{output_dir}/slowfast/'
    os.makedirs(output_dir_3d, exist_ok=True)

    clip_interval = int(opts.clip_interval/opts.frame_length)
    # files = glob.glob(f'{opts.img_dir}/*.npz')
    files_dict = pkl.load(open(opts.vfeat_info_file, "rb"))
    files = [[key]+list(val) for key, val in files_dict.items()]
    # for root, dirs, curr_files in os.walk(f'{opts.img_dir}/'):
    #     for f in curr_files:
    #         if f.endswith('.npz'):
    #             files.append(os.path.join(root, f))
    load = load_npz()
    name2nframes = {}
    corrupted_files = set()
    with mp.Pool(opts.nproc) as pool, tqdm(total=len(files)) as pbar:
        for i, (fname, features, nframes) in enumerate(
                pool.imap_unordered(load, files, chunksize=128)):
            if not features or nframes == 0:
                pbar.update(1)
                corrupted_files.add(fname)
                continue  # corrupted feature
            if opts.clip_interval != -1:
                feature_values_2d = features["2d"]
                feature_values_3d = features["3d"]
                clip_id = 0
                for st_ind in range(0, nframes, clip_interval):
                    clip_name = fname+f".{clip_id}"
                    ed_ind = min(st_ind + clip_interval, nframes)
                    clip_features_2d = feature_values_2d[st_ind: ed_ind]
                    clip_features_3d = feature_values_3d[st_ind: ed_ind]
                    clip_id += 1
                    name2nframes[clip_name] = ed_ind - st_ind
                    output_file_2d = f'{output_dir_2d}/{fname}.{clip_id}.npz'
                    np.savez(output_file_2d, features=clip_features_2d)
                    output_file_3d = f'{output_dir_3d}/{fname}.{clip_id}.npz'
                    np.savez(output_file_3d, features=clip_features_3d)
            else:
                feature_values_2d = features["2d"]
                feature_values_3d = features["3d"]
                output_file_2d = f'{output_dir_2d}/{fname}.npz'
                np.savez(output_file_2d, features=feature_values_2d)
                output_file_3d = f'{output_dir_3d}/{fname}.npz'
                np.savez(output_file_3d, features=feature_values_3d)
                name2nframes[fname] = nframes
            pbar.update(1)
    id2frame_len_file = f'{output_dir}/id2nframe.json'
    with open(id2frame_len_file, 'w') as f:
        json.dump(name2nframes, f)
    corrupted_files = list(corrupted_files)
    if len(corrupted_files) > 0:
        corrupted_output_file = f'{output_dir}/corrupted.json'
        with open(corrupted_output_file, 'w') as f:
            json.dump(corrupted_files, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--vfeat_info_file", default=None, type=str,
                        help="The input feature paths stored in pkl file.")
    parser.add_argument("--output", default=None, type=str,
                        help="output lmdb")
    parser.add_argument(
        '--frame_length', type=float, default=2,
        help='1 feature per "frame_length" seconds used in feature extraction,'
             'in seconds (1.5/2)')
    parser.add_argument('--dataset', type=str,
                        default="")
    parser.add_argument('--feat_version', type=str,
                        default="resnet_slowfast")
    parser.add_argument('--nproc', type=int, default=4,
                        help='number of cores used')
    parser.add_argument('--compress', action='store_true',
                        help='compress the tensors')
    parser.add_argument(
        '--clip_interval', type=int, default=-1,
        help="cut the whole video into small clips, in seconds"
             "set to 60 for HowTo100M videos, set to -1 otherwise")
    args = parser.parse_args()
    main(args)
