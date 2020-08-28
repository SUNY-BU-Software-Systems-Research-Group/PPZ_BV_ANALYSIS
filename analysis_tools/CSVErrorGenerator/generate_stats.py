from typing import List

def mean(data):
    """Return the sample arithmetic mean of data."""
    if data == "undefined":
        return "undefined"
    n = len(data)
    if n < 1:
        raise ValueError("mean requires at least one data point")
    return sum(data)/n # in Python 2 use sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def stddev(data, ddof=0):
    """Calculates the population standard deviation
    by default; specify ddof=1 to compute the sample
    standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/(n-ddof)
    return pvar**0.5

def remove_percent(a,p):
    a.sort()
    return a[int(len(a)*p):int(len(a)*(1.0-p))]

def normalize(a, x, y):
    """ 
    Returns a list with normalized values of a in [x, y] range.

    Adds a sense of direction when using x=-1 y=1 vs. normalization in just [0, 1] range.
    """
    if x >= y:
        raise ValueError("must have x less than y to specify proper range")
    min_a = min(a)
    max_a = max(a)
    if min_a == max_a:
        return "undefined"
    return [(y-x)*(float(i)-min_a)/(max_a-min_a) + x for i in a]

def pearson_correlation(x,y,ddof=0):
    mean_x = mean(x)
    mean_y = mean(y)
    n = len(x)
    if ddof == 0:
        scale_denom = 1
        scale_nom = 1
    else:
        ddof = 1
        scale_denom = n-1
        scale_nom = n
    denom = scale_denom*stddev(x,ddof)*stddev(y,ddof)
    if denom == 0:
        return "undefined"
    mean_xy = mean([x * y for x, y in zip(x,y)])
    return (scale_nom*(mean_xy - (mean_x * mean_y))) / denom

class csv_stat_writer:
    def __init__(self, of, percents=[]):
        self.log = open(of, "w")
        self.percents = percents
        self.log.write("FILE,MEAN,NORM_MEAN,STDDEV,PCC,")
        for p in percents:
            p_str = str(p*100)
            self.log.write(f"MEAN({p_str}%),NORM_MEAN({p_str}%),STDDEV({p_str}%),PCC({p_str}%),")
        self.log.write("\n")

    def process_data_file(self, path, actual, desired, difference, func, norm_low, norm_high):
        """    
        Populate actual, desired, and difference with data from f.
   
        Difference is populated by +/- % Error. When desired element is 0 the error is 0 or 1. 
        0, if the actual element is 0; or, -1, if the actual element is not 0.

        Turns out this code block writes -1 not 1 when just the desired element is equal to 0
        """
        fi = path.name
        print(f"======={fi}=======")
        f = open(path)
        itr = 0
        for l in f.readlines()[1:]:
            actual.append(float(l.split(',')[0]))
            desired.append(float(l.split(',')[1]))
            func(actual, desired, difference, itr)
            itr += 1
        f.close()
        diff = list(filter(lambda x: x != "undefined", difference))
        self.write_line(fi, actual, desired, diff, norm_low, norm_high)

    def write_line(self, fi, actual, desired, diff, norm_low, norm_high):    
        self.log.write(fi+",")
        print("\t=======Full Sample========")
        data_mean = mean(diff)
        data_norm_mean = mean(normalize(diff, norm_low, norm_high))
        data_std_dev = stddev(diff)
        data_pcc = pearson_correlation(actual, desired)
        print("\tMEAN:", data_mean)
        print("\tNORM MEAN:", data_norm_mean)
        print("\tSTDDEV:", data_std_dev)
        print("\tPCC:", data_pcc)
        self.log.write(str(data_mean)+","+str(data_norm_mean)+","+str(data_std_dev)+","+str(data_pcc)+",")
        self.do_percents(actual, desired, diff, norm_low, norm_high)
        self.log.write('\n')

    def do_percents(self, actual, desired, diff, norm_low, norm_high):
        for p in self.percents:
            print(f"\t===={p*100}% Removed=====")
            data_set = remove_percent(diff,p)
            data_mean = mean(data_set)
            data_norm_mean = mean(normalize(data_set, norm_low, norm_high))
            data_std_dev = stddev(data_set,1)
            data_x = remove_percent(actual, p)
            data_y = remove_percent(desired, p)
            data_pcc = pearson_correlation(data_x, data_y,1)
            print("\tMEAN:", data_mean)
            print("\tNORM MEAN:", data_norm_mean)
            print("\tSTDDEV:", data_std_dev)
            print("\tPCC:", data_pcc)
            self.log.write(str(data_mean)+","+str(data_norm_mean)+","+str(data_std_dev)+","+str(data_pcc)+",")



"""
PERCENTS=[0.01, 0.025, 0.05, 0.1, 0.15]

LOG_OUTPUT=open("output_log.csv", "w")
LOG_OUTPUT.write("FILE,MEAN,NORM_MEAN,STDDEV,PCC,")
for p in PERCENTS:
    p_str = str(p*100)
    LOG_OUTPUT.write(f"MEAN({p_str}%),NORM_MEAN({p_str}%),STDDEV({p_str}%),PCC({p_str}%),")
LOG_OUTPUT.write("\n")

for fi in glob.glob("./data/*.csv"):
    actual = []
    desired = []
    difference = []
    process_data_file(fi, actual, desired, difference, new_pe, -1, 1, PERCENTS)

for fi in glob.glob("./data/cross_sim_cases/*.csv"):
    actual = []
    desired = []
    difference = []
    process_data_file(fi, actual, desired, difference, new_pe, -1, 1, PERCENTS)
"""

