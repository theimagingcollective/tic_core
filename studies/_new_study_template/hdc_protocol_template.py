import os

"""
heudiconv template protocol file. 

This template file can be used as an example and starting point for creating your own protocol files.  


"""

def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    """
    Create key for HDC DICOM to NIFTI conversion

    DO NOT MODIFY

    :param template:
    :param outtype:
    :param annotation_classes:
    :return:
    """

    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group


    The namedtuple `s` contains the following fields:

    * total_files_till_now
    * example_dcm_file
    * series_id
    * dcm_dir_name
    * unspecified2
    * unspecified3
    * dim1
    * dim2
    * dim3
    * dim4
    * TR
    * TE
    * protocol_name
    * is_motion_corrected
    * is_derived
    * patient_id
    * study_description
    * referring_physician_name
    * series_description
    * image_type

    Below is an example of the output from the iMove study

    >>> csvcut -c 4,21,8,9,10,11,12,13,15 dicominfo_ses-1.csv | csvlook

    | ----------------------------| ------------- | ---- | ---- | ---- | ---- | ----- | ------ | ------------------- |
    | series_id                   | sequence_name | dim1 | dim2 | dim3 | dim4 |    TR |     TE | is_motion_corrected |
    | 2-MPRAGE_GRAPPA2            | *tfl3d1_16ns  |  256 |  240 |  192 |    1 | 2.300 |   2.98 |               False |
    | 3-BOLD_resting 4X4X4 A>>P   | *epfid2d1_64  |   64 |   64 |   35 |  190 | 2.000 |  25.00 |               False |
    | 4-rest_topup_A>>P           | *epse2d1_64   |   64 |   64 |  140 |    1 | 2.400 |  38.00 |               False |
    | 5-rest_topup_P>>A           | *epse2d1_64   |   64 |   64 |  140 |    1 | 2.400 |  38.00 |               False |
    | 6-Field_mapping 4X4X4 A>>P  | *fm2d2r       |   64 |   64 |   35 |    1 | 0.488 |   4.92 |               False |
    | 7-Field_mapping 4X4X4 A>>P  | *fm2d2r       |   64 |   64 |   35 |    1 | 0.488 |   7.38 |               False |


    key-value tags
    --------------

    BIDS uses a key-value pairs in the naming convention.  The sub-<participant_label> is a required field. It is used
    to create a subject specific directory in the BIDS directory.

    It must also be included in each and every filename. The ses-<session_label> is a bug the <session_label> includes
    the key.  This means that {session} translates to
    ses-<session-label>.

    Only certain keys are associated with each imaging modality.
    key-value pairs are in [] are optional.  If a key-value pair is not in [] then it must be included in the name.
    For example every filename must include sub-<participant_label> to be BIDS compliant.  The session key-value
    is optional. However, if you include session key-value in the path then you must also include it in the
    filename.

    Another example of required and optional key-value pairs is in the FUNC images.  Here is the key-value
    pairs taken from the BIDS documentation for images in the func directory.

     _task-<task_label>[_acq-<label>][_rec-<label>][_run-<index>][_echo-<index>]_bold

     You can see that task-<task_label> is not in [] so it is required. While _acq-<acq_label> is in [] and is
     therefore optional.

     Below I have included some notes for the key-value pairs for the different imaging modalities and BIDS
     sub-directories.


    common key-value tags:

        sub-<participant_label>/[ses-<session_label>/]/<dir>/sub-<participant_label>[_ses-<session_label>]

        <dir> = anat, func, fmap, dwi, swi

        {participant_label} is the variable which will be replaced by the subject's acrostic

        {session_label} is the variable which will be replaced by the session value key.  {session} is inconsistent
                        and is replaced by the key and it's value. An example, should help clarify this inconsistency
                        {session} is replaced by ses-{session_id}.

        {acq} is the acquisition value

        {item:01d} is the item counter padded by two zeros.  This allows HDC to create a unique name if it finds
                  multiple images that meet your criteria.  We recommend that only one DICOM image should match your
                  criteria for data conversion. However, this can not happen if the scan is repeated.

    anat key-value tags:

        [_acq-<label>][_ce-<label>][_rec-<label>][_run-<index>]<modality_label>.nii[.gz]
        [_acq-<label>][_ce-<label>][_rec-<label>][_run-<index>][_mod-<label>]_defacemask.nii[.gz]


        Imaging Type/Name,       modality_label
        T1 weighted              T1w
        T2 weighted              T2w
        T1 Rho map               T1rho
        T1 map                   T1map
        T2 map                   T2map
        T2*                      T2star
        FLAIR                    FLAIR
        FLASH                    FLASH
        Proton density           PD
        Proton density map       PDmap
        Combined PD/T2           PDT2
        Inplane T1               inplaneT1
        Inplane T2               inplaneT2
        Angiography              angio



    func/ _task-<task_label>[_acq-<label>][_rec-<label>][_run-<index>][_echo-<index>]_bold

    fmap/  [_acq-<label>][_run-<run_index>]_phasediff
           [_acq-<label>][_run-<run_index>]_magnitude1

           [_acq-<label>]_dir-<dir_label>[_run-<run_index>]_epi

    dwi/   [_acq-<label>][_run-<index>]_dwi
           [_acq-<label>][_run-<index>]_sbref

    swi/  [_acq-<label>][_rec-<label>]_part-<phase|mag>[_coil-<index>][_echo-<index>][_run-<index>]_GRE.nii[.gz]

        https://docs.google.com/document/d/1kyw9mGgacNqeMbp4xZet3RnDhcMmf4_BmRgKaOkO2Sc/edit


    asl/  _task-<task_label>[_acq-<label>][_rec-<label>][_run-<index>]_asl.nii[.gz]

        https://docs.google.com/document/d/15tnn5F10KpgHypaQJNNGiNKsni9035GtDqJzWqkkP6c/edit#heading=h.mqkmyp254xh6

    """

    t1 = create_key('anat/sub-{subject}_run-{item:02d}_T1w')
    rest_fmri_ap = create_key('func/sub-{subject}_dir-ap_task-rest_run-{item:02d}_bold')
    rest_topup_ap = create_key('func/sub-{subject}_dir-ap_run-{item:02d}_bold')
    rest_topup_pa = create_key('func/sub-{subject}_dir-pa_run-{item:02d}_bold')
    fmap_rest_magnitude1 = create_key('fmap/sub-{subject}_run-{item:02d}_magnitude1')
    fmap_rest_phasediff = create_key('fmap/sub-{subject}_run-{item:02d}_phasediff')

    # Create an empty dictionary called info for each key

    info = {t1: [],
            rest_fmri_ap: [],
            rest_topup_ap: [],
            rest_topup_pa: [],
            fmap_rest_magnitude1: [],
            fmap_rest_phasediff: [],
            }

    # Loop over each sequence. Use if statements to determine which sequences should be linked to which key

    for idx, s in enumerate(seqinfo):

        if (('MPRAGE_GRAPPA2' in s.series_id) and
                ('tfl3d1_16ns' in s.sequence_name) and
                (s.dim3 == 192) and
                (s.dim4 == 1)):
                info[t1] = [s.series_id]

        if (('BOLD_resting 4X4X4 A>>P' in s.series_id) and
                ('epfid2d1_64' in s.sequence_name) and
                (s.dim3 == 35) and
                (s.dim4 == 190)):
                info[rest_fmri_ap] = [s.series_id]

        if (('rest_topup_A>>P' in s.series_id) and
                ('epse2d1_64' in s.sequence_name) and
                (s.dim3 == 140) and
                (s.dim4 == 1)):
                info[rest_topup_ap] = [s.series_id]

        if (('rest_topup_P>>A' in s.series_id) and
                ('epse2d1_64' in s.sequence_name) and
                (s.dim3 == 140) and
                (s.dim4 == 1)):
                info[rest_topup_pa] = [s.series_id]

        if (('Field_mapping 4X4X4 A>>P' in s.series_id) and
                ('fm2d2r' in s.sequence_name) and
                (s.dim3 == 35) and
                (s.dim4 == 1) and
                (s.TE == 4.92)):
                info[fmap_rest_magnitude1] = [s.series_id]

        if (('Field_mapping 4X4X4 A>>P' in s.series_id) and
                ('fm2d2r' in s.sequence_name) and
                (s.dim3 == 35) and
                (s.dim4 == 1) and
                (s.TE == 7.38)):
                info[fmap_rest_phasediff] = [s.series_id]

    return info
