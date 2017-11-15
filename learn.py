# import functools
#
# def log(text):
#     def decorator(fn):
#         @functools.wraps(fn)
#         def wrapper(*args, **kw):
#             print('begin call')
#             fn(*args, **kw)
#             print('end call')
#             if callable(text):
#                 pass
#             else:
#                 print('%s' % text)
#             return
#         return wrapper
#     if callable(text):
#         return decorator(text)
#     else:
#         return decorator
#
# @log('lxxk')
# def now():
#     print('test')
#
# if __name__ == '__main__':#从其他地方导入该模块是，if判断失效
#     now()
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

def print_score(std):
    print('%s %s' %(std['name'], std['score']))













