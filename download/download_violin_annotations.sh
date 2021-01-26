# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

DOWNLOAD=$1

ANN=$DOWNLOAD/ann
if [ ! -d $ANN ] ; then
    mkdir -p $ANN
fi


if [ ! -d $ANN/violin ] ; then
    mkdir -p $ANN/violin
fi

# processed subtitles
wget -nc --no-check-certificate 'https://docs.google.com/uc?export=download&id=15XS7F_En90CHnSLrRmQ0M1bqEObuqt1-' -O $ANN/violin/violin_annotations.json
