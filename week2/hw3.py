while True:
    str = input(": ")
    arr = []
    arr += str
    notDubStr = [i for j , i in enumerate(arr) if i not in arr[:j]]
    print (''.join(notDubStr))