from math import *




#print("Arvuta peast! ...4*100-55")

#o_vastus=4*100-55
#vastus=int(input("Lahenda ülesanne ... "))
#k=1
#while True:
    
#    if vastus!=o_vastus:

#        print("Viga! Sisesta Õige vastus on ...", )

#        vastus=int(input("Sisesta vastus ..."))
#        k+=1
#    else: 

#        print("Õige vastus! Katsed oli ...",k )
#        break


#for x in range(1,31,2):

        #print(x, end=" ")

#while True:

#    input("Введите 15 чисел:\n")

print("*** KÜSIMUSTE MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisesta täisarv => ")))) #Скобки были не закрыты
        break
    except ValueError:
         print("See pole täisarv.")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi teha.")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju on paaris- ja mitu paaritut numbrit")
    print()
    c=b=a
    paaris=0        #Тут везде стояло 2 знака равно
    paaritu=0 
    while b > 0: #Стоял не верный знак
            if b % 2 == 0:

                    paaris += 1
            else:
                    paaritu += 1
            b = b // 10
    print("Paaris arv:",paaris) # Была добавлена запятая
    print("Paaritu arv:",paaritu) #Была добавлена запятая
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake ümber* sisestatud arv")
    print()
    b=0
    while a > 0: #Конструкция while была нарушена
        number = a % 10
        a = a // 10
        b = b * 10
        b += number
    print("*Muudetud* arv", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Uurime Syracuse hüpoteesi") # Была удалена лишняя скобка
    print()
    if c % 2 == 0:
        print("с - Paaris arv. Jagame 2.")
    else:
        print("с -Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")
    while c != 1:
            if c % 2 == 0:
                    c = c / 2
            else:
                    c = (3*c + 1) / 2
            print(round(c), end=" ")
    print()
    print("Hüpotees on õige") #Неверный знак стоял