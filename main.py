'''
we will need to run a code repeatedly till a specific amount of time.
now this program will check the folder for the last updated files.
if we find a file a directly
'''
# myf = open("hello.txt", "wt")
# print("I am so happy!.", file=myf)
# myf.close()

import os
from datetime import datetime, timedelta

# os.mkdir('myfolder')
# os.makedirs("fol1/fol2")

path = "fol1"


def file_dispenser(path, thresh, base=True):

    if os.path.isdir(path):
        print(f"This is a directory: {path}")
        for internal in os.listdir(path):
            file_dispenser(path + "/" + internal, thresh, False)

        if (not base) and len(os.listdir(path))==0:
            print("Empty Folder.")
            # os.rmdir(path)
        return


    mod = os.path.getmtime(path)
    print(" ")
    if thresh > mod:
        print("this is an Old file.")
        print(path)
        # os.remove(path)
    else:
        print("This is a new file.")
        print(path)


# x = int(input("Enter the Threshold Time: "))
threshold = (datetime.now() - timedelta(minutes=10)).timestamp()
file_dispenser("fol1", threshold)
# threshold = (datetime.now() - timedelta(minutes=3)).timestamp()
# print(threshold)
# threshold = (datetime.now() - timedelta(minutes=1)).timestamp()
# print(threshold)
