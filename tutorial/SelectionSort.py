def myselectionsort(x):
    for pos in range(len(x)):
        minipos = pos
        for i in range(pos+1, len(x)):
            if x[minipos] > x[i]:
                minipos = i
        (x[pos], x[minipos]) = (x[minipos], x[pos]) 
