from pathlib import Path
import csv
import tkinter
from tkinter import filedialog

female_names = []
male_names = []
nb_names = []
last_names = []

file_name = filedialog.askopenfilename()
read_csv = Path(file_name)

with open(read_csv) as csvfile:
    data = csv.reader(csvfile)
    raw_names = list(data)

for list in raw_names:
    if list[3] == "Female":
        female_names.append(list[1])
    elif list[3] == "Male":
        male_names.append(list[1])
    else:
        nb_names.append(list[1])
    last_names.append(list[2])

print(f"Female names: {len(female_names)}")
print(f"Male names: {len(male_names)}")
print(f"Non-binary names: {len(nb_names)}")
print(f"Last names: {len(last_names)}")

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

female_names = Remove(female_names)
male_names = Remove(male_names)
nb_names = Remove(nb_names)
last_names = Remove(last_names)

print(f"Female names: {len(female_names)}")
print(f"Male names: {len(male_names)}")
print(f"Non-binary names: {len(nb_names)}")
print(f"Last names: {len(last_names)}")

write_csv = Path('names.csv')

with open(write_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(female_names)
    csvwriter.writerow(male_names)
    csvwriter.writerow(nb_names)
    csvwriter.writerow(last_names)