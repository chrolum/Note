import foo

filename = 'func.py'

def show_filenaem():
    return 'filename is %s' % filename

if __name__ == "__main__":
    print(foo.call_func(show_filenaem()))#filename为func.py因为执行环境在func.py里边