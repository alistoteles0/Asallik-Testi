num = int(input("Pozitif ve 1'den büyük bir tam sayı giriniz: "))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"asal sayı değildir.")
            break
    else:
        print(num,"asal sayıdır.")
else:
    print(num, "asal sayı değildir.")
