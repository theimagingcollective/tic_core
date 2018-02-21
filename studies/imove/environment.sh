#!/usr/bin/env bash

# Environment variables

export IMOVE_SCRIPTS_PATH=${TIC_PATH}/studies/imove/scripts

export IMOVE_PATH=/gandg/imove/
export IMOVE_BIDS_PATH=${IMOVE_PATH}/bids
export IMOVE_IMAGE_ANALYSIS_PATH=${IMOVE_PATH}/image_analysis
export IMOVE_IMAGE_PROCESSING_PATH=${IMOVE_PATH}/image_processing
export IMOVE_IMAGE_PROCESSING_LOG_PATH=${IMOVE_IMAGE_PROCESSING_PATH}/logs

export IMOVE_QC_PATH=${IMOVE_PATH}/qc
export IMOVE_MRIQC_PATH=${IMOVE_QC_PATH}/mriqc


export IMOVE_FMRIPREP_PATH=${IMOVE_IMAGE_PROCESSING_PATH}/fmriprep
export IMOVE_NETPREP_PATH=${IMOVE_IMAGE_PROCESSING_PATH}/netprep

export IMOVE_BIDS_CONFIG_FILE=${IMOVE_SCRIPTS_PATH}/IMOVE_bids.cfg
export IMOVE_HEUDICONV_PROTOCOL=${IMOVE_SCRIPTS_PATH}/imove_protocol.py
export IMOVE_CLEAN_BIDS=${IMOVE_SCRIPTS_PATH}/imove_clean_bids.sh

export IMOVE_SUBJECTS_DIR=${IMOVE_IMAGE_PROCESSING_PATH}/freesurfer

