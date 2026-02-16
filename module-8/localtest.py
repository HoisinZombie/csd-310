import json
import tkinter as tk
from tkinter import messagebox
import os


with open('Student.json') as f:
    studentlist = json.load(f)

print()
print ('Student list:')
print (studentlist)
print ()

with open('Student.json') as f:
    melist = json.load(f)

melist.append({
    "F_Name": "Andy",
    "L_Name": "Estrada",
    "Student_ID": 45834,
    "Email": "Esandada@gmail.com"
})

print('Updated Student List:')
print(melist)

with open('Student.json', 'w') as json_file:
    json.dump(melist, json_file, indent=4, separators=(',',': '))

print()
print('Successfully appended Andy to the JSON file')
