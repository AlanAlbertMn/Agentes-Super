import sys, os, re
import time

def mergefiles(in_filenames, merge_name):
    out_file = open(merge_name,"w+")
    for file in in_filenames:
        in_file = open(file, 'r')
        out_file.write(in_file.read())
        in_file.close()
    out_file.close()

if __name__ == "__main__":
    file1="amazon_cells_labelled.txt"
    file2="imdb_labelled.txt"
    file3="yelp_labelled.txt"
    in_filenames=[]
    in_filenames.append(file1)
    in_filenames.append(file2)
    in_filenames.append(file3)
    '\n'.join(in_filenames)
    merge_name="merged_data.txt"
    mergefiles(in_filenames, merge_name)