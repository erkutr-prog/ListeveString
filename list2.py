def digit(number):
    digits = []
    for i in number:
        digits.append(i)
    return digits

def multiply(first,second):
    dot  = digit(first)
    second = second.strip("1")
    second = list(second)
    return dot+second

#girilen sayının basamaklarını liste halinde döndürmek için;
#sayi = str(input("Bir sayı giriniz: "))
#print(digit(sayi))

#Girilen bir integer sayı ve 10un katı ikinci bir sayının çarpımını liste halinde almak için;

#int1 = str(input("İlk sayıyı giriniz: "))
#int2 = str(input("İkinci sayıyı giriniz: "))

#print(multiply(int1,int2))

