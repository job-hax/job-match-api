import json
from collections import Counter


def top_skills_in(comp, data):
    comp = comp.lower()
    target = []
    for line in data:
        job = ' '.join(line["current_job"]).lower()
        if comp in job:
            target.append(line)

    skills = Counter()
    for line in target:
        skills.update(Counter(line["top_skills"]))
    return skills.most_common(3)


def common_attr(attr, data):
    skills = Counter()
    for line in data:
        skills.update(Counter(line[attr]))
    return skills.most_common((3))

