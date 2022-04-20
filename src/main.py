import sys

if __name__ == "__main__":
    print('args: '+str(sys.argv))

    if len(sys.argv) == 1:
        print('NO XLS PATH PROVIDED')
    else:
        xls_path = str(sys.argv[1])
        



