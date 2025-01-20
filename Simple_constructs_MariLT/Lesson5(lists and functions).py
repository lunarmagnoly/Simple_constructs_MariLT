# new_list=[]# empty list
# numbers=[1,2,3,4,5]
# abc=['Abc','b','c']# words and letters are written inside ''
# word="Programing"
# word_list=list(word)
# print(word)
# print(word_list)

# while True:
#  print("1 - add letter to the list \n2 - merge lists \n3 - add letter to i position \n4 - delete element ")
#  print("\n5 - count elements in the list \n6 - search letter index \n7 - sort list \n8 - reverce list" )
#  print("\n9 - join letters in line \n10 - split string")

#  choise=int(input())
#  if choise==1:
#      a=input("Insert letter ")
#      word_list.append(a)#or word_list.append(input("Insert letter "))
#      print(f"Added {a} new list: ", word_list)
#  elif choise==2:
#      word_list.extend(abc)
#      print(word_list)
#  elif choise ==3:
#      a=input("Enter letter that you want to add ")
#      i=int(input("Add position, where letter must be added "))
#      word_list.insert(i-1,a)#correction for normal person i starts with 0, but for normal person start is 1
#      print(word_list)
#  elif choise ==4:
#      a=input("Enter letter that you want to delete ")
#      n=word_list.count(a)
#      if n>0:
#          for i in range(n):
#             word_list.remove(a)
#      else:
#          print("Letter does not exist")
#      print(word_list)
#  elif choise ==5:
#      a=input("Enter letter that you want to count ")
#      n=word_list.count(a)
     
#      print(n)
# Lõvi, Elevand, Jääkaru, Gepard, Kaelkirjak, Tiiger, Panda, Känguru, Vares, Ninasarvik

import random

zoo = []

while True:
    print("\nVali tegevus:")
    actions = [
        "Lisa loom(kui mitu loomi kasuta ',')", "Näita kõiki loomi", "Eemalda loom", "Tühjenda kõik loomad",
        "Otsi looma", "Kuva loomade arv", "Sorteeri loomad", "Pööra loomade järjestus",
        "Asenda loom", "Vali juhuslik loom", "Lõpeta"
    ]
    
    for i in range(len(actions)):
        print(f"{i + 1}. {actions[i]}")
    
    if zoo:
        print("\nPraegused loomad:")
        for i, animal in enumerate(zoo, 1):
            print(f"{i}. {animal}")
    else:
        print("\nLoomi ei ole.")

    try:
        choice = int(input("\nSisesta tegevuse number: ")) - 1
    except ValueError:
        print("Vale sisestus. Palun sisestage number.")
        continue

    if choice == 0:
        animals = input("Sisesta loomade nimed, eraldatuna komadega: ").split(',')
        zoo.extend(animals)
        print("Loomad lisatud.")
    elif choice == 1:
        print("\nKõik loomad:")
        for i, animal in enumerate(zoo, 1):
            print(f"{i}. {animal}")
    elif choice == 2:
        if zoo:
            animal_index = int(input("Sisesta eemaldatava looma number: ")) - 1
            if 0 <= animal_index < len(zoo):
                removed_animal = zoo.pop(animal_index)
                print(f"Loom '{removed_animal}' eemaldatud.")
            else:
                print("Vale number. Palun proovi uuesti.")
        else:
            print("Loomi ei ole.")
    elif choice == 3:
        zoo.clear()
        print("Kõik loomad tühjendatud.")
    elif choice == 4:
        animal_name = input("Sisesta otsitava looma nimi: ")
        if animal_name in zoo:
            print(f"Loom '{animal_name}' leiti nimekirjast.")
        else:
            print(f"Looma '{animal_name}' ei leitud nimekirjast.")
    elif choice == 5:
        print(f"Praegu on nimekirjas {len(zoo)} looma.")
    elif choice == 6:
        zoo.sort()
        print("Loomad on sorditud.")
    elif choice == 7:
        zoo.reverse()
        print("Loomade järjestus on pööratud.")
    elif choice == 8:
        animal_index = int(input("Sisesta asendatava looma number: ")) - 1
        if 0 <= animal_index < len(zoo):
            new_animal = input("Sisesta uus looma nimi: ")
            zoo[animal_index] = new_animal
            print("Loom asendatud.")
        else:
            print("Vale number. Palun proovi uuesti.")
    elif choice == 9:
        if zoo:
            random_animal = random.choice(zoo)
            print(f"Juhuslikult valitud loom: {random_animal}")
        else:
            print("Loomi ei ole, et valida juhuslikult.")
    elif choice == 10:
        break
    else:
        print("Vale valik. Palun valige uuesti.")


