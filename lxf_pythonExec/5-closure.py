def count():
    def f(j):
        def g():
            print('exec with v=%d' % j)
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))     # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

print('do call')
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
