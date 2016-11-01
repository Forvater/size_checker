import sys
import urllib.request
import os
import contextlib

remote_file_path = 'http://docs.python-requests.org/en/master/_static/requests-sidebar.png'
local_file_path = "file.dat"


def get_server_size(uri):
    size = None
    try:
        with contextlib.closing(urllib.request.urlopen(uri)) as file:
            size = file.headers.get('content-length')
    except IOError:
        return None
    if size is not None:
        return int(size)
    else:
        return None


def get_file_data(uri):
    file_data = None
    try:
        with contextlib.closing(urllib.request.urlopen(uri)) as file:
            file_data = file.read()
    except IOError:
        return None
    return file_data


def get_file_size(path):
    return os.path.getsize(path)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Using predefined url: {}'.format(remote_file_path))
        print('To use other url type it as 1st command line argument for this script')
        print('')
    elif len(sys.argv) == 2:
        remote_file_path = sys.argv[1]
    server_size = get_server_size(remote_file_path)
    if server_size is None:
        print('Could not get size of the file on server')
    else:
        file_data = get_file_data(remote_file_path)
        if file_data is None:
            print('Could not get file data')
        else:
            try:
                with open(local_file_path, 'wb') as f:
                    f.write(file_data)
            except IOError:
                print('Failed to open file {} for writing'.format(local_file_path))
            else:
                if get_file_size(local_file_path) == server_size:
                    print("Files have the same size")
                else:
                    print("Files have different size")
