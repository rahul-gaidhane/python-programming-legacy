def myinsertionsort(x):
    for sliceEnd in range(len(x)):
        pos = sliceEnd
        while pos > 0 and x[pos] < x[pos-1]:
            (x[pos], x[pos-1]) = (x[pos-1], x[pos])
            pos = pos - 1

def recinsertionsort(x):
    isort(x,len(x))

def isort(x, k):
    if k > 1 :
        isort(x, k-1)
        insert(x, k-1)

def insert(x, k):
    for k > 0 and x[k] < x[k-1]:
        (x[k], x[k-1]) = (x[k-1], x[k])
        k = k-1
        print x
