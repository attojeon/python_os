import os

count = 0
def search_python(dirname):
    global count
    try:
        filenames = os.listdir(dirname)

        for onefile in filenames:
            full_filename = os.path.join(dirname, onefile)
            if os.path.isdir(full_filename):
                search_python(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
                    count += 1

    except PermissionError:
        pass

search_python('c:/python35/')
print("="*80)
print('No files' if count == 0 else 'count: {}'.format(count)) 