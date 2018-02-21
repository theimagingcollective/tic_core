#!/usr/bin/env bash

# Environment variables

export NEWSTUDY_SCRIPTS_PATH=${TIC_PATH}/studies/newstudy/scripts

export NEWSTUDY_PATH=/gandg/newstudy/
export NEWSTUDY_BIDS_PATH=${NEWSTUDY_PATH}/bids
export NEWSTUDY_IMAGE_ANALYSIS_PATH=${NEWSTUDY_PATH}/image_analysis
export NEWSTUDY_IMAGE_PROCESSING_PATH=${NEWSTUDY_PATH}/image_processing
export NEWSTUDY_IMAGE_PROCESSING_LOG_PATH=${NEWSTUDY_IMAGE_PROCESSING_PATH}/logs

export NEWSTUDY_QC_PATH=${NEWSTUDY_PATH}/qc
export NEWSTUDY_MRIQC_PATH=${NEWSTUDY_QC_PATH}/mriqc

export NEWSTUDY_FMRIPREP_PATH=${NEWSTUDY_IMAGE_PROCESSING_PATH}/fmriprep
export NEWSTUDY_NETPREP_PATH=${NEWSTUDY_IMAGE_PROCESSING_PATH}/netprep

export NEWSTUDY_BIDS_CONFIG_FILE=${NEWSTUDY_SCRIPTS_PATH}/NEWSTUDY_bids.cfg
export NEWSTUDY_HEUDICONV_PROTOCOL=${NEWSTUDY_SCRIPTS_PATH}/NEWSTUDY_protocol.py

export NEWSTUDY_SUBJECTS_DIR=${NEWSTUDY_IMAGE_PROCESSING_PATH}/freesurfer

