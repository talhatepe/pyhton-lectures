while True:
    str = input(": ").lower()
    arr = []
    for i in str:
        bool = False
        for j in arr:
            if i == j:
                bool = True
                break
        if bool == False:
            arr.append(i) 
    print(''.join(arr))
