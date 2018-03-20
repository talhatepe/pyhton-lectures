while True:
    input = input(": ")
    def reverse(str):
        arr = []
        arr += str
        leng = len(arr)
        ave = leng / 2
        single = True
        if leng % 2 == 0:
            single = False
        if single:
            ave = round(ave)
        ave2 = int(ave)
        for i in range(0, ave2):
            tmp = arr[i]
            arr[i] = arr[0 - (i + 1)]
            arr[0 - (i + 1)] = tmp
        return arr


    print (''.join(reverse(input)))
