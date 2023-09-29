# Import Multiprocessing
from multiprocessing import Process

def getName(name):
    print('hello', name)

# Ham main
if __name__ == '__main__':
    p = Process(target=getName, args = ('multiprocessing',))
    # Khoi dong process
    p.start()
    # Join Process
    p.join()
