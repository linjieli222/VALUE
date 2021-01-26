# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

DOWNLOAD=$1

ANN=$DOWNLOAD/ann
if [ ! -d $ANN ] ; then
    mkdir -p $ANN
fi

HOW2='https://raw.githubusercontent.com/ych133/How2R-and-How2QA/master'

if [ ! -d $ANN/how2_subtitles ] ; then
    mkdir -p $ANN/how2_subtitles
fi

# processed subtitles
wget -nc $HOW2/subtitles/how2r_qa_sub.jsonl -O $ANN/how2_subtitles/preprocessed_subtitles.jsonl 

# How2QA annotations
if [ ! -d $ANN/how2qa ] ; then
    mkdir -p $ANN/how2qa
fi
for SPLIT in 'train' 'val' 'test_public'; do
    wget -nc $HOW2/how2QA/how2QA_${SPLIT}_release.csv -O $ANN/how2qa/how2qa_${SPLIT}_release.csv
done

# How2R annotations
if [ ! -d $ANN/how2r ] ; then
    mkdir -p $ANN/how2r
fi
for SPLIT in 'train' 'val' 'test_public'; do
    wget -nc $HOW2/how2R/how2R_${SPLIT}_release.csv -O $ANN/how2r/how2r_${SPLIT}_release.csv 
done
