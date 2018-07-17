import os

def search_python(dirname):
    filenames = os.listdir(dirname)

    count = 0
    for onefile in filenames:
        full_filename = os.path.join(dirname, onefile)
        ext = os.path.splitext(full_filename)[-1]
        if ext == '.py':
            print(full_filename)
            count += 1

    print('No files' if count == 0 else '')

search_python('c:/python35/Tools/demo/')