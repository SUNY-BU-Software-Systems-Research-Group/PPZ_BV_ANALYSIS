import generate_stats
from parse_args import parser

if __name__ == "__main__":
    args = parser.parse_args()
    percents = args.percents
    logger = generate_stats.csv_stat_writer(args.output, percents)
    for path in args.parent_dir:
        actual = []
        desired = []
        difference = []
        (method, norm_min, norm_max) = args.error_preset
        logger.process_data_file(path, actual, desired, difference, method, norm_min, norm_max)

