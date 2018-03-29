# Homework - Week 3

### • hw1.py:
```python
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


if __name__ == "__main__":

        input = input(": ")
        print(''.join(reverse(input)))

```

> Bir girdi alarak 'input' adlı değişkene atadım. 'rev' adında bir fonksiyon oluşturdum. 'arr' isimli bir list oluşturup içine klavyeden girilen girdiyi aktardım. 'leng' adında bir değişkenin oluşturup içine 'arr' adlı listin boyutunu int olarak atadım. Ardından 'ave' adlı değişkenime leng/2 diyerek uzunluğu ikiye böldüm. 'single' adında bir boolean değişkene 'True' değer tanımladım. 'leng' isimli uzunluk değişkenime tek/çift kontrolü yaptım. Çift ise 'single' değişkenimin değerini 'False' olarak değiştirdim. Sonrasında eğer tek ise 'ave' adlı değişkene içerisindeki sayıyı yuvarlayıp kendisine atadım. 'ave2' diye bir değişken daha oluşturup 'ave' değişkeni içerisindeki sayıyı tanımladım. Bir döngü oluşturup 0'dan başlayıp girilen string değeri reverse ettim harf harf sırayla ve çıktıyı ekrana bastım.