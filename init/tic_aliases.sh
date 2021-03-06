#!/usr/bin/env bash

# TIC Functions

source $TIC_PATH/bin/tic_functions.sh

alias gpl='grep parameters *.log'
alias fif='fmap_intended_for.py'
alias fifc='fmap_intended_for_check.py'

alias commac='comm $ACTIVE_BIDS_PATH/acrostic.list'

alias bps='bids_processing_status.py'

alias tic_help='firefox $TIC_PATH/docs/build/html/index.html > /dev/null 2>&1 &'

alias tic_info='tic_info.sh'
alias tsi='tic_info.sh'  # Duplicated alias to match alias asi

alias tic_update='cd $TIC_PATH; git pull; cd -; rehash'

alias tic_make_docs='cd $TIC_PATH; git pull; cd -; rehash; cd $TIC_PATH/docs/; make clean; make html; cd -; firefox $TIC_PATH/docs/build/html/index.html&'


alias dfgandg='echo; df -h /gandg/; echo'

alias catlast='ls -1drt * | tail -1 | xargs cat'
alias cl='ls -1drt * | tail -1 | xargs cat'

alias cdtb='cd $TIC_PATH/bin; lsreport_function'
alias cdts='cd $TIC_STUDIES_PATH; lsreport_function'
alias cdtic='cd $TIC_PATH; lsreport_function'


alias cdtemplates='cd $TEMPLATES_PATH; lsreport_function'
alias cdixi='cd $TEMPLATE_IXI; lsreport_function'
alias cdinia='cd $TEMPLATE_INIA19; lsreport_function'
alias cdmni='cd $TEMPLATE_MNI; lsreport_function'

alias cdsd='cd $SUBJECTS_DIR; lsreport_function'

alias cda='echo; echo $PWD; cd $(pwd -P); echo $PWD; echo; ls; echo'

alias retic='source $TIC_PATH/init/tic_aliases.sh'

alias fmriprep='/usr/local/bin/singularity run -w -B /cenc -B /gandg -B /bkraft1 $FMRIPREP_SINGULARITY_IMAGE'
alias mriqc='/usr/local/bin/singularity run -w -B /cenc -B /gandg -B /bkraft1 $MRIQC_SINGULARITY_IMAGE'

alias hdc_convert='/usr/local/bin/singularity run -w -B /cenc -B /gandg -B /bkraft1 $HDC_SINGULARITY_IMAGE -c dcm2niix '
alias hdc_scan='/usr/local/bin/singularity run -w -B /cenc -B /gandg -B /bkraft1 $HDC_SINGULARITY_IMAGE -f $TIC_PATH/studies/_new_study_template/hdc_convertall.py -c none'

alias ag='alias | grep'
alias hg='history | grep '
alias eg='env | grep '
alias lg='ls | grep '

alias lsp='echo; echo $PATH | tr ":" "\n" | cat -n | sort -n -r; echo'          # Enumerates path
alias lspp='echo; echo $PYTHONPATH | tr ":" "\n" | cat -n | sort -n -r; echo'   # Enumerates Python Path
alias lssd='echo; echo $SUBJECTS_DIR; echo'

alias l1='ls -1d'
alias lld='ld -ld'
alias llr='ls -lrt'
alias lls='ls -lrS'

alias frv='freeview'
alias fsv='fslview'
alias fse='fsleyes'

alias fsvall='fslview_all_function'

alias lnflatten='${TIC_PATH}/lnflatten.sh'
alias cpflatten='${TIC_PATH}/cpflatten.sh'
