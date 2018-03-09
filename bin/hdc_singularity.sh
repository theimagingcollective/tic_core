#!/bin/bash

echo
echo 'active study = ' $ACTIVE_STUDY
echo 'bids path    = ' $ACTIVE_BIDS_PATH
echo 'protocol     = ' $ACTIVE_HEUDICONV_PROTOCOL
echo 'pattern      = ' $ACTIVE_HEUDICONV_PATTERN
echo
echo 'parameters   = ' $@
echo

if [ $# -eq 0 ]
  then
    echo
    echo "No arguments supplied for heudiconv"
    echo

    /usr/local/bin/singularity run $HDC_SINGULARITY_IMAGE -h

else
    /usr/local/bin/singularity run     \
       -w                              \
       -B /cenc                        \
       -B /gandg                       \
       -B /bkraft1                     \
       $HDC_SINGULARITY_IMAGE          \
       -c dcm2niix                     \
       -b --minmeta                    \
       -f $ACTIVE_HEUDICONV_PROTOCOL   \
       -o $ACTIVE_BIDS_PATH            \
       -d "{subject}/2*/*/*.DCM"       \
       $@
fi