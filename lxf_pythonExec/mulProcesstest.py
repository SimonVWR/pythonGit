from multiprocessing import Pool
import os,random,time

def long_time_task(name):
    print('Run long time task %s(%s)'%(name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s run %.2f seconds'%(name, end-start))


if __name__ == '__main__':
    sp = Pool(4)
    print('Parent prosess %s' %os.getpid())
    for i in range(5):
        sp.apply_async(long_time_task, args=(i,))
    print('wait for childprocess finish...')
    sp.close()
    sp.join()
    print('Child process finished')


