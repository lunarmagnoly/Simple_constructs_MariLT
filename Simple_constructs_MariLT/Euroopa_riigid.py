from dictionary_functions import load_countries_and_capitals, get_capital_or_country, add_to_dictionary, correct_dictionary_entry, quiz

# Laadime andmed failist
load_countries_and_capitals('countries_and_capitals.txt')

while True:
    choice = input("\nVali tegevus: \n1. Kuva pealinn või riik\n2. Lisa sõnastikku\n3. Paranda sõnastiku kanne\n4. Viktoriin\n5. Välju\nSisesta oma valik: ")
    
    if choice == "1":
        name = input("Sisesta riik või pealinn: ")
        result = get_capital_or_country(name)
        if result:
            print(result)
        else:
            print(f"{name} ei leitud sõnastikust.")
            add_entry = input("Kas soovite selle sõnastikku lisada? (jah/ei): ")
            if add_entry.lower() == "jah":
                if input("Kas see on riik? (jah/ei): ").lower() == "jah":
                    capital = input("Sisesta pealinn: ")
                    add_to_dictionary(name, capital)
                else:
                    country = input("Sisesta riik: ")
                    add_to_dictionary(country, name)
    
    elif choice == "2":
        country = input("Sisesta riik: ")
        capital = input("Sisesta pealinn: ")
        add_to_dictionary(country, capital)
    
    elif choice == "3":
        old_name = input("Sisesta vana nimi: ")
        new_name = input("Sisesta uus nimi: ")
        is_country = input("Kas see on riik? (jah/ei): ").lower() == "jah"
        correct_dictionary_entry(old_name, new_name, is_country)
    
    elif choice == "4":
        quiz(10)
    
    elif choice == "5":
        break
    
    else:
        print("Vale valik. Palun proovi uuesti.")
