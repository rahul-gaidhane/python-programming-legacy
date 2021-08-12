import threading

print("inside mythread.py")

def make_it_zero(num, count):
    print("thread %d : %d" % (count, num))
    while (num > 0):
        num = num - 1
    print("thread %d : %d" % (count, num))

print("inside main")
numlist = [1234567890, 9876543210, 12345, 123654789, 147852369, 98765]
'''t1 = threading.Thread(target=make_it_zero, args=(numlist[0], 1))
t2 = threading.Thread(target=make_it_zero, args=(numlist[1], 2))
t3 = threading.Thread(target=make_it_zero, args=(numlist[2], 3))
t4 = threading.Thread(target=make_it_zero, args=(numlist[3], 4))
t5 = threading.Thread(target=make_it_zero, args=(numlist[4], 5))
t6 = threading.Thread(target=make_it_zero, args=(numlist[5], 6))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()'''
make_it_zero(numlist[0], 1)
make_it_zero(numlist[1], 2)
make_it_zero(numlist[2], 3)
make_it_zero(numlist[3], 4)

print("It's Done!")
