def func_a(func_a_arg_a, func, **kwargs):
    print(func_a_arg_a)
    func(**kwargs)

def func_b(arg_a):
    print(arg_a)

def func_c():
    print('Hello World')

if __name__ == '__main__':
    func_a(func_a_arg_a='temp', arg_a='Hello Python', func=func_b)
    func_a(func_a_arg_a='temp', func=func_c)