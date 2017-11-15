# import foo
#
# def warpper():
#     filename = "enclosed.py"
#     def show_filename():
#         return "filename is %s" % filename
#     print(foo.call_func(show_filename))
#
# warpper()

# def wrapper():
#     alist = range(1, 100)
#     def lazy_sum():
#         return reduce(lambda x,y: x+y, alist)
#     return lazy_sum
#
# lazy_sum = wrapper()
#
# if __name__ == '__main__':
#     lazy_sum()

# import logging
#
# logging.basicConfig(level = logging.INFO)
# @checkParams #语法糖 实际解释时 add = checkParams(add)
# def add(a, b):
#     return a + b
# def checkParams(fn):
#     def wrapper(a, b):
#         if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#             return fn(a, b)
#
#         logging.warning("variable 'a' and 'b' cannot be added")
#         return
#     return wrapper #fn引用add，被封存在闭包的执行环境中返回,创建闭包
#
#
# if __name__ == '__main__':
#     #将add函数对象传入，fn指向add
#
#     add = checkParams(add)
#     add(3, 4)


#若装饰器本身需要传入参数

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s()' %  (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('text')
# def now():
#     print('time')

#now = log('text')(now)
# class Animals(object):
#     __slots__ = ('age', 'name')
#
#     def run(self):
#         print('Animal is running')
#
# class Dog(Animals):
#
#     def run(self):
#         print('Dog is runing')
#
# class Cat(Dog):
#     pass
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
#
#
# cat = Animals()
# cat.name = '233'
# cat.num = 233
# print(cat.__doc__)

# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2017 - self._birth

# class Screen(object):
#
#     @property
#     def width(self):
#         return self._width
#
#     @property
#     def height(self):
#         return self._height
#     @width.setter
#     def width(self, value):
#         self._width = value#可以在此加参数检查的代码
#
#     @height.setter
#     def height(self, value):
#         self._height = value
#
#     @property
#     def resolution(self):
# #
#链式调用
# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))#?
#
#     def __str__(self):
#         return self._path
#
#     def users(self, path):
#         return 'GET %s' % self._path
#
#     __repr__ = __str__
#
# print(Chain().list.a233.s2333.d23333)

# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
#
# class MyList(list, metaclass=ListMetaclass):








