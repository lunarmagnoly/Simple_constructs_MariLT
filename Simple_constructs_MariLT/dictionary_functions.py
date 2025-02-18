import random

# Sõnastik riikide ja pealinnadega
countries_and_capitals = {}

# Funktsioon andmete laadimiseks failist
def load_countries_and_capitals(file_path):
    global countries_and_capitals
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            country, capital = line.strip().split('-')
            countries_and_capitals[country] = capital


# Funktsioon pealinna või riigi kuvamiseks
def get_capital_or_country(name):
    if name in countries_and_capitals:
        return countries_and_capitals[name]
    for country, capital in countries_and_capitals.items():
        if capital == name:
            return country
    return None

# Funktsioon uue kirje lisamiseks sõnastikku
def add_to_dictionary(country, capital):
    countries_and_capitals[country] = capital
    print(f"Lisatud: {country} - {capital}")

# Funktsioon sõnastiku kirje parandamiseks
def correct_dictionary_entry(old_name, new_name, is_country=True):
    if is_country:
        if old_name in countries_and_capitals:
            countries_and_capitals[new_name] = countries_and_capitals.pop(old_name)
            print(f"Parandatud: {old_name} -> {new_name}")
        else:
            print(f"{old_name} ei leitud sõnastikust.")
    else:
        for country, capital in countries_and_capitals.items():
            if capital == old_name:
                countries_and_capitals[country] = new_name
                print(f"Parandatud: {old_name} -> {new_name}")
                return
        print(f"{old_name} ei leitud sõnastikust.")

# Funktsioon teadmiste kontrollimiseks
def quiz(total_questions):
    correct_answers = 0
    
    for i, (country, capital) in enumerate(random.sample(list(countries_and_capitals.items()), total_questions), start=1):
        answer = input(f"({i}/{total_questions}) Mis on {country} pealinn? ")
        if answer.lower() == capital.lower():
            print("Õige!")
            correct_answers += 1
        else:
            print(f"Vale! Õige vastus on {capital}.")
    
    score = (correct_answers / total_questions) * 100
    print(f"Sinu tulemus: {score:.2f}%")

