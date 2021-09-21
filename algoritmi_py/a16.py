'''
Linda Rieksta, lr21050
A16. Dots naturāls skaitlis. Atrast dotā skaitļa ciparu vidējo aritmētisko. Skaitļa dalīšana ciparos jāveic skaitliski.
Programma izveidota: 2021/09/20
'''

a = 1
while (a == 1):
    num = int(input("Ievadi skaitli: "))
    sum = int(0) #summas un n(skaits) atskaites punkts sākas no 0
    n = int(0)

    while (num > 0): #ievadītajam skaitlim jābūt pozitīvam
        digit = int(num % 10) #definē pēdējo ciparu
        num = int(num / 10) 
        sum = sum + digit #kopējā ciparu summa (atskaites summa + pēdējais cipars)
        n = n + 1 #kopējais n(skaits)

    if (n > 0): result = sum / n
    print("Vidējais aritmētiskais: ", result)
    a = int(input("Vai turpināt (1) vai beigt (0)? "))
else: print("Paldies")



'''
 _______________________________________________________________________________________________________________________
| Datu ievade | Vēlamā reakcija |    Rezultāts C++      | Rezultāts Python                              | Vai pareizi?  |
|_____________|_________________|_______________________|_______________________________________________|_______________|
|     126     |        3        |            3          |       3.0                                     |        +      |
|    126.0    |kļūdas paziņojums| 3 (un pārtrauc ciklu) |invalid literal for int() with base 10: '126.0'|      - / +    |
|     127     |    3.3333(3)    |         3.33333       |      3.3333333333333335                       |        +      |
|      9      |        9        |            9          |       9.0                                     |        +      |
|     -25     |kļūdas paziņojums|            0          | name 'result' is not defined                  |      - / +    |
|      0      |  0  vai kļūda   |            0          | name 'result' is not defined                  |        +      |
|_____________|_________________|_______________________|_______________________________________________|_______________|

'''

