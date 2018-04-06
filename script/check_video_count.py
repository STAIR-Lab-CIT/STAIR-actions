#! encoding=UTF-8
from __future__ import print_function
import argparse
import os
import json
from collections import defaultdict

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check downloaded video counts for STAIR Actions.")
    parser.add_argument('-t', '--test', type=str, help="", default="")
    args = parser.parse_args()

    with open("data/dataset_train.json") as f:
        dataset = json.load(f)
    
    expected_totals = defaultdict(int)
    actual_totals = defaultdict(int)
    for action in dataset.keys():
        expected_counts = defaultdict(int)
        actual_counts = defaultdict(int)
        files = os.listdir(os.path.join("STAIR_Actions_v1.0/{}".format(action)))
        for fn in files:
            if "X" in fn:
                actual_counts["X"] += 1
            elif "Y" in fn:
                actual_counts["Y"] += 1
            elif "Z" in fn:
                actual_counts["Z"] += 1
            elif "C" in fn:
                actual_counts["C"] += 1
            else:
                raise Exception("Something wrong")

        for elm in dataset[action]["train"]:
            expected_counts[elm["type"]] += 1

        s = "{0:>40}\t".format(action)
        for t in ["X", "Y", "Z", "C"]:
            s += "{}:{}({}) ".format(t, actual_counts[t], expected_counts[t])
            expected_totals[t] += expected_counts[t]
            actual_totals[t] += actual_counts[t]
        print(s)

    print("---")
    s = "{0:>40}\t".format("total")
    for t in ["X", "Y", "Z", "C"]:
        s += "{}:{}({}) ".format(t, actual_totals[t], expected_totals[t])
    print(s)
