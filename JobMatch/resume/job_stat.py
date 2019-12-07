import json
from collections import Counter
import re


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


def top_companies(data):
    companies = []
    for line in data:
        job = line['current_job'][0]
        company = re.search(r"\sat\s(.+)", job)
        if company:
            companies.append(company.group(1))

    return Counter(companies).most_common(3)


def top_positions(data):
    positions = []
    for line in data:
        job = line['current_job'][0]
        position = re.search(r"(.+)\sat\s", job)
        if position:
            positions.append(position.group(1))

    return Counter(positions).most_common(3)

