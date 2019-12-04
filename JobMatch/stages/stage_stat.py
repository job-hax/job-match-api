import time
import json


def accept_rate(data):
    N = len(data)
    accept = 0
    for line in data:
        if "None" not in line.values():
            accept += 1
    return accept / N


def longest_dur(data):
    max_ = 0
    for line in data:
        if "None" not in line.values():
            apply = time.mktime(time.strptime(line["Applied"], '%m-%d-%Y %H:%M'))
            offer = time.mktime(time.strptime(line["Offer"], '%m-%d-%Y %H:%M'))
            max_ = max(max_, (offer - apply) / 3600)
    return max_


def most_fail_stage(data):
    # index 1->onsite, 2->phone, 3->apply
    stages = [0,0,0,0]
    for line in data:
        res = tuple(line.values())
        if "None" in res:
            i = res.count("None")
            stages[i] += 1
    i = stages.index(max(stages))
    if i == 3:
        stage = "Applied"
    elif i == 2:
        stage = "Phone"
    else:
        stage = 'Onsite'
    return stage, stages[i]