import os
import json

from files import list_files


if not os.path.exists(list_files.animals):
    with open(list_files.animals, "w", encoding="utf-8"):
        pass

with open(list_files.animals, "r", encoding="utf-8") as fh:
    animals = fh.readlines()
    animals = [animal.strip() for animal in animals]

if not os.path.exists(list_files.reviews):
    with open(list_files.reviews, "w", encoding="utf-8"):
        pass

with open(list_files.reviews, "r", encoding="utf-8") as fh:
    reviews = fh.readlines()
    reviews = [review.strip() for review in reviews]

if not os.path.exists(list_files.employees):
    with open(list_files.employees, "w", encoding="utf-8") as fh:
        json.dump({}, fh)

with open(list_files.employees, "r", encoding="utf-8") as fh:
    employees = json.load(fh)

if not os.path.exists(list_files.animals_cured):
    with open(list_files.animals_cured, "w", encoding="utf-8") as fh:
        json.dump([], fh)

with open(list_files.animals, "r", encoding="utf-8") as fh:
    animals_cured = json.load(fh)

if not os.path.exists(list_files.log):
    with open(list_files.log, "w", encoding="utf-8") as fh:
        json.dump([], fh)

with open(list_files.log, "r", encoding="utf-8") as fh:
    log = json.load(fh)

if not os.path.exists(list_files.most_using_command):
    with open(list_files.most_using_command, "w", encoding="utf-8") as fh:
        json.dump({}, fh)

with open(list_files.most_using_command, "r", encoding="utf-8") as fh:
    most_using_command = json.load(fh)