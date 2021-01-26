# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

DOWNLOAD=$1

for FOLDER in 'vis_features' 'ann'; do
    if [ ! -d $DOWNLOAD/$FOLDER ] ; then
        mkdir -p $DOWNLOAD/$FOLDER
    fi
done

BLOB='https://convaisharables.blob.core.windows.net/leaderboard/value/vis_features'

TVQA='http://tvqa.cs.unc.edu/files/'
TVR='https://raw.githubusercontent.com/jayleicn/TVRetrieval/master/data/'
TVC='https://raw.githubusercontent.com/jayleicn/TVCaption/master/data/'

# TV subtitles
if [ ! -d $DOWNLOAD/ann/tvqa_subtitles ] ; then
    # raw subtitles
    wget -nc $TVQA/tvqa_subtitles.tar.gz -P $DOWNLOAD/ann/
    tar -zxvf $DOWNLOAD/ann/tvqa_subtitles.tar.gz -C $DOWNLOAD/ann/
    rm -rf $DOWNLOAD/ann/tvqa_subtitles.tar.gz
fi
# processed subtitles
wget -nc $TVR/tvqa_preprocessed_subtitles.jsonl -P $DOWNLOAD/ann/

# TVQA annotations
if [ ! -d $DOWNLOAD/ann/tvqa_qa_release ] ; then
    wget -nc $TVQA/tvqa_qa_release.tar.gz -P $DOWNLOAD/ann/
    tar -zxvf $DOWNLOAD/ann/tvqa_qa_release.tar.gz -C $DOWNLOAD/ann/
    rm -rf $DOWNLOAD/ann/tvqa_qa_release.tar.gz
fi

# TVR annotations
for SPLIT in 'train' 'val' 'test_public'; do
    if [ ! -f $DOWNLOAD/ann/tvr_${SPLIT}_release.jsonl ] ; then
        wget -nc $TVR/tvr_${SPLIT}_release.jsonl -P $DOWNLOAD/ann/
    fi
done
wget -nc $TVR/tvr_video2dur_idx.json -P $DOWNLOAD/ann/

# TVC annotations
for SPLIT in 'train' 'val' 'test_public'; do
    if [ ! -f $DOWNLOAD/ann/tvc_${SPLIT}_release.jsonl ] ; then
        wget -nc $TVC/tvc_${SPLIT}_release.jsonl -P $DOWNLOAD/ann/
    fi
done

# vis features
if [ ! -d $DOWNLOAD/vis_features/tv ] ; then
    mkdir -p $DOWNLOAD/vis_features/tv
fi
for FEAT in '2d_resnet' 'slowfast'; do
    if [ ! -d $DOWNLOAD/vis_features/tv/$FEAT ] ; then
        wget $BLOB/tv/$FEAT.tar -P $DOWNLOAD/vis_features/tv/
        tar -xvf $DOWNLOAD/vis_features/tv/$FEAT.tar -C $DOWNLOAD/vis_features/tv
        rm -rf $DOWNLOAD/vis_features/tv/$FEAT.tar
    fi
done
# info files
wget -nc $BLOB/tv/info.json -P $DOWNLOAD/vis_features/tv/
wget -nc $BLOB/tv/id2nframe.json -P $DOWNLOAD/vis_features/tv/
