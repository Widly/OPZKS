import sys, os

def remove_file_secure(filepath, iterations, clear_type):
    chunk_size = 1024
    write_values = lambda count: os.urandom(count) if clear_type == 'r' else bytes([0] * count)

    for i in range(iterations):
        with open(filepath, 'r+b') as f:
            f.seek(0, 2)
            file_size = f.tell()
            f.seek(0, 0)

            while file_size > chunk_size:
                f.write(write_values(chunk_size))
                file_size -= chunk_size

            f.write(write_values(file_size))

    os.remove(filepath)


def cleanup(path, iterations=1, clear_type='z'):
    if not os.path.isdir(path):
        remove_file_secure(path, iterations, clear_type)
    else:
        for p in os.listdir(path):
            target = path + '/' + p
            if os.path.isdir(target):
                cleanup(target, iterations, clear_type)
            else:
                remove_file_secure(target, iterations, clear_type)

        os.rmdir(path)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('please, enter params')
        sys.exit()

    if sys.argv[1] == '--help':
        print('''Input params:
        path to file/dir
        number of iterations
        clear type: 'r' - erase with random values, 'z' - erase with zeros''')
        sys.exit()

    try:
        path = sys.argv[1]
        iterations = int(sys.argv[2])
        clear_type = sys.argv[3]
    except(IndexError):
        print('please, type all params')
        sys.exit()
    except(ValueError):
        print('bad iterations format')
        sys.exit()

    if clear_type not in ('z', 'r'):
        print('bad clear type format')
        sys.exit()

    if not os.path.exists(path):
        print('file or dir not found')
        sys.exit()

    cleanup(path, iterations, clear_type)