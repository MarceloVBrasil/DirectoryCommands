# Author: Marcelo Brasil

import os
import shutil

# calculate average 
def calculate_avg(arr):
    total = 0
    n = len(arr)
    for i in range(0,n):
        total += arr[i]
    return total / n
# Final Grades
final_grades = [8,7.5,9,6,7.1,8.7,6.8,9.5,10]
# parent Directory path
parent_dir = "C:/"
# Directory
dir_source = "Source folder/"
dir_destination = "Destination folder/"
# path
path_source = os.path.join(parent_dir, dir_source)
path_destination = os.path.join(parent_dir, dir_destination)
# Create directory
os.mkdir(path_source)
os.mkdir(path_destination)
# Source and Destination folders
source_folder = path_source
destination_folder = path_destination
# Create file under source folder
l = len(final_grades)
class_avg = calculate_avg(final_grades)
for i in range(0,l):
    fgrade = final_grades[i]
    newFileName = "Student" + str(i+1) + ".txt"
    newFile = os.path.join(source_folder, newFileName)
    f = open(newFile, "w")
    f.write("CANADA PROGRAMMING SCHOOL\n\n\n")
    f.write("REPORT CARD \n\n")
    f.write("Subject: PROGRAMMING FUNDAMENTALS\n")
    f.write("Student" + str(i+1) + " final grade is " + str(fgrade) + ": ")
    if fgrade < 7:
        f.write("POOR")
    elif fgrade >= 7 and fgrade < class_avg:
        f.write("GOOD")
    elif fgrade > class_avg and fgrade < 9:
        f.write("GREAT JOB!")
    else:
        f.write("EXCELLENT!")
    f.close()
# fetch all files
for file in os.listdir(source_folder):
    # construct full file name
    source = source_folder + file
    destination = destination_folder + file
    # copy files only
    if os.path.isfile(source):
        shutil.copy(source, destination)
