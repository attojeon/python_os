import os

dirname = 'c:/python35/Tools/'

def search(_dirname):
    for(path, dirs, files) in os.walk(_dirname):
        print(path)

        for dir in dirs:
            print("\t", dir)

        for filename in files:
            print("\t", filename)



search(dirname)