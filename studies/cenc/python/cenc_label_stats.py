#!/usr/bin/env python3

"""

"""
import sys
import os                                               # system functions
import re
import pandas
import json
import argparse
import _utilities as util
import cenc
import labels
import datetime
from collections import OrderedDict
import getpass
import subprocess

def _calc_volumes_in_tissue_regions( tissue_mask,  mask, verbose=False ):
    df_properties = labels.properties(tissue_mask)
    df_measure    = labels.measure(tissue_mask, mask)

    tissue_volume = df_properties['volume_mm3'].values[0]
    label_fraction_volume_in_tissue = df_measure['mean'].values[0]

    label_volume_in_tissue = tissue_volume * label_fraction_volume_in_tissue

    output_metrics = (label_volume_in_tissue, label_fraction_volume_in_tissue, tissue_volume)

    if verbose:
        print( output_metrics )

    return output_metrics 

    


def cenc_stats(input_dir, in_image, out_json, instrument_prefix='', verbose=False):
    """ Write MagTrans Instrument to JSON output file"""

    cenc_dirs = cenc.directories( input_dir )

    if verbose:
         print(cenc_dirs['results']['dirs']['labels'])

    tissue_labels = {'gm_cerebral':    os.path.join( cenc_dirs['results']['dirs']['labels'], 'gm.cerebral_cortex.nii.gz'),
                     'gm_subcortical': os.path.join( cenc_dirs['results']['dirs']['labels'], 'gm.subcortical.nii.gz'),
                     'wm_cerebral':    os.path.join( cenc_dirs['results']['dirs']['labels'], 'wm.cerebral.nii.gz'),
                     'wm_lesions':     os.path.join( cenc_dirs['results']['dirs']['labels'], 'wmlesions_lpa_mask.nii.gz')
              }
    
    pandas.set_option('expand_frame_repr', False)

    df_stats_gm_cortical    = labels.measure(tissue_labels['gm_cerebral'], in_image)
    df_stats_gm_subcortical = labels.measure(tissue_labels['gm_subcortical'], in_image)
    df_stats_wm_cerebral    = labels.measure(tissue_labels['wm_cerebral'], in_image)
    df_stats_wm_lesions     = labels.measure(tissue_labels['wm_lesions'], in_image)

    (gm_cortical_label_volume, 
     gm_cortical_label_fraction, 
     gm_cortical_volume) = _calc_volumes_in_tissue_regions( tissue_labels['gm_cerebral'], in_image, verbose=True)

    (gm_subcortical_label_volume, 
     gm_subcortical_label_fraction, 
     gm_subcortical_volume) = _calc_volumes_in_tissue_regions( tissue_labels['gm_subcortical'], in_image, verbose=True)

    (wm_cerebral_label_volume, 
     wm_cerebral_label_fraction, 
     wm_cerebral_volume) = _calc_volumes_in_tissue_regions( tissue_labels['wm_cerebral'], in_image, verbose=True)

    (wm_lesions_label_volume, 
     wm_lesions_label_fraction, 
     wm_lesions_volume) = _calc_volumes_in_tissue_regions( tissue_labels['wm_lesions'], in_image, verbose=True)

    dict_stats = OrderedDict(( ('subject_id', cenc_dirs['cenc']['id']),
                               ( instrument_prefix + 'analyst', getpass.getuser()),
                               ( instrument_prefix + 'datetime', '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())),
                               ( instrument_prefix + 'image', in_image),

                               ( instrument_prefix + 'gm_cortical_volume_mm3', '{0:4.3f}'.format( gm_cortical_volume)),
                               ( instrument_prefix + 'gm_cortical_label_volume_mm3', '{0:4.3f}'.format( gm_cortical_label_volume)),
                               ( instrument_prefix + 'gm_cortical_label_fraction', '{0:4.3f}'.format( gm_cortical_label_fraction)),

                               ( instrument_prefix + 'gm_subcortical_volume_mm3', '{0:4.3f}'.format( gm_subcortical_volume)),
                               ( instrument_prefix + 'gm_subcortical_label_volume_mm3', '{0:4.3f}'.format( gm_subcortical_label_volume)),
                               ( instrument_prefix + 'gm_subcortical_label_fraction', '{0:4.3f}'.format( gm_subcortical_label_fraction)),

                               ( instrument_prefix + 'wm_cerebral_volume_mm3', '{0:4.3f}'.format( wm_cerebral_volume)),
                               ( instrument_prefix + 'wm_cerebral_label_volume_mm3', '{0:4.3f}'.format( wm_cerebral_label_volume)),
                               ( instrument_prefix + 'wm_cerebral_label_fraction', '{0:4.3f}'.format( wm_cerebral_label_fraction)),

                               ( instrument_prefix + 'wm_lesions_volume_mm3', '{0:4.3f}'.format( wm_lesions_volume)),
                               ( instrument_prefix + 'wm_lesions_label_volume_mm3', '{0:4.3f}'.format( wm_lesions_label_volume)),
                               ( instrument_prefix + 'wm_lesions_label_fraction', '{0:4.3f}'.format( wm_lesions_label_fraction)),

                               )
                              )

    if out_json==None:
         json_stats_filename =  in_image.replace( 'nii.gz', 'json')
    else:
         json_stats_filename = out_json
         
    if verbose:
         print( json_stats_filename )

    with open(json_stats_filename, 'w') as outfile:
         json.dump(dict_stats, outfile, indent=4, ensure_ascii=True, sort_keys=False)

    if verbose:
        util.print_json_redcap_instrument(json_stats_filename)

    return

# ======================================================================================================================
#  Main
def main():
    ## Parsing Arguments

    usage = "usage: %prog [options] arg1 arg2"

    parser = argparse.ArgumentParser(prog='cenc_mt')

    parser.add_argument("in_image", help="Input image", default=None )
    parser.add_argument("--in_dir", help="Participant directory", default=os.getcwd())
    parser.add_argument("--out_json", help="Output JSON filename", default=None )
    parser.add_argument("--prefix", help="Instrument Prefix", default='' )

    parser.add_argument('-v', '--verbose', help="Verbose flag", action="store_true", default=False)

    inArgs = parser.parse_args()

    cenc_stats(inArgs.in_dir, inArgs.in_image, inArgs.out_json, inArgs.prefix, inArgs.verbose)


# Main Function

if __name__ == "__main__":
    sys.exit(main())

    
