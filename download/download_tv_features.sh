DOWNLOAD=$1

DATASET=tv

VIS=$DOWNLOAD/vis_features/$DATASET
if [ ! -d $VIS ] ; then
    mkdir -p $VIS
fi

BLOB='https://convaisharables.blob.core.windows.net/leaderboard/value/vis_features'

for FEAT in '2d_resnet' 'slowfast'; do
    if [ ! -d $VIS/$FEAT ] ; then
        wget $BLOB/$DATASET/$FEAT.tar -P $VIS
        tar -xvf $VIS$FEAT.tar -C $VIS
        rm -rf $VIS$FEAT.tar
    fi
done
# info files
wget -nc $BLOB/$DATASET/info.json -P $VIS
wget -nc $BLOB/$DATASET/id2nframe.json -P $VIS
