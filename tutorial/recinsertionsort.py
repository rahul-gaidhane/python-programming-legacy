def myinsertionsort(x):
    isort(x, len(x))

def isort(x, k):
    if k > 1:
        isort(x, k-1)
        insert(x, k-1)

def insert(x, k):
    pos = k
    while pos > 0 and x[pos] < x[pos-1]:
        (x[pos], x[pos-1]) = (x[pos-1], x[pos])
        pos = pos - 1
        print(x[0])
