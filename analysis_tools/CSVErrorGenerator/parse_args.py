from pathlib import Path
import argparse
from error_preset import Preset

def csv_from_dir(directory):
    return Path('.').glob(directory+'/**/*.csv')
preset = Preset()
PERCENTS=[0.01, 0.025, 0.05, 0.1, 0.15]
parser = argparse.ArgumentParser(description='Generate statistical info on error from csv files.')
parser.add_argument('error_preset', metavar='E', type=preset, help=preset.help_message())
parser.add_argument('parent_dir', metavar='D', type=csv_from_dir, help='specify relative path of parent directory')
parser.add_argument('-p', '--percents', metavar='P', nargs='*', type=float, help=f'floating point numbers to trim the csv data; default={PERCENTS}', default=PERCENTS)
parser.add_argument('-o', "--output", metavar='O', default='output_log.csv', help="Name of output file; default=output_log.csv")
