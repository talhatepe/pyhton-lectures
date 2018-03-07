# Homework - Week 2

### • hw1.py:
```python
	import random 

	arr = [None] * 100
	for i in range (1,100):
	    arr[i] = i
	
	arr[0] = random.randint(1,99)
	random.shuffle(arr)
	print (arr)
	
	x = 4950 #1+2+.....+99 = 4950
	total = 0
	for i in range (len(arr)):
	    total += arr[i]
	print ("Duplicate Num: ", total - x)
```

> Öncelikle 100 elemanlı bir array oluşturdum sonrasında bu arrayin içerisine 1-99 arasındaki sayıları ekledim. Arrayın içerisindeki indexlerin yerini karışık bir şekilde dağıttım. Bir tane dublicate sayı ekledim. Arrayi ekrana bastım. 'x' adında bir değişkene 4950 (1-99 arasındaki sayıların toplamı) değerini atadım. Arrayin index sayısı kadar for döndüm ve toplam değişkenine her döngüde arrayın elemanını ekleyerek toplamı buldum. 'toplam' değişkeninden 'x' değişkenini çıkartarak ekrana bastım.


### • hw2.py:
```python
	while True:
        num1 = input("Num 1: ")
        num1 = int(num1) - 1
        num2 = input("Num 2: ")
        num2 = int(num2)
        str = input("String: ")
        str2 = str[num2:]
        str = str[:num1]
        print (str,str2)
```

> 2 tane int değer isteyerek num1 ve num2 değişkenlerine atadım. 1 tane string değeri de str değişkenine atadım. Girilen 2 int değerin arası sileneceği için girilen ilk sayı kadar olan string girdiyi str adlı değişkene, girilen ikinci sayıden sonraki string değeri str2 adlı değişkene atadım ve ekrana bastım.


### • hw3.py:
```python
	while True:
	    str = input(": ")
	    arr = []
	    arr += str
	    notDubStr = [i for j , i in enumerate(arr) if i not in arr[:j]]
	    print (''.join(notDubStr))
```

> Bir string değer aldım str değişkenine atadım. 'arr' adından bir list oluşturdum. 'arr' adlı arrayin içine girilen string değeri her harf bir indexe gelecek şekilde bir işlem yaptım. Sonrasında tekrar eden indexleri ayıkladım ve çıkan sonucu ekrana bastım.


### • hw4.py:
```python
	while True:
        str = input(": ")
        if str == str[::-1]:
            print ("Polindrome")
        else:
            print ("Not Polindrome")
```

> ...