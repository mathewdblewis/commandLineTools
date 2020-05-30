from multiprocessing import Pool
def f(x):
    return x*x
print(Pool().map(f, [1, 2, 3]))
