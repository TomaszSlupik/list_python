# PYTHON LIST METHOD
# append - dodawanie
fruits = ['jabłko', 'banan', 'kiwi']
fruits.append('gruszka')

print(fruits)

print('---')

# extend - dodawanie kilku elementów
train = ['pływanie']
train.extend(['rower', 'bieg'])

print(train)

print('---')

# insert - dodawanie w wyznaczone miejsce w liście
my_name = ['t', 'o', 'e', 'k']

m_add = my_name.insert(2, 'm')

print(my_name)

print('---')
# remove - usuwanie z listy

phone = ['Iphone', 'Samsung', 'Telewizor']
phone.remove('Telewizor')
print(phone)

print('---')

# pop - usuwanie z konkretnego miejsca

name_students = ['Anna', 'Ola', 'Wiesław', 'Leszek', 'Darek']
name_students.pop(2)
print(name_students)

print('---')

# Count - zliczanie liczby elemntów w liście - ile razy występuje
alf = ['a', 'b', 'c', 'd', 'e', 'e', 'e', 'f', 'g']

print(alf.count('e'))

print('---')
# sort - sortowanie listy

test_alf = ['w', 'b', 'a', 'k', 't', 's']

test_alf.sort()

print(test_alf)

print('---')
# reverse - odwrócenie listy
xyz = ['x', 'y', 'z']

xyz.reverse()

print(xyz)

print('---')
# Split vs splitlines
# Split - załadowanie każdego słowa do listy
morning_swim = 'Dzisiaj byłem rano na basenie o 6:00. Było mało ludzi'

list_morning_swim = morning_swim.split()
print(list_morning_swim)

print('---')
# splitlines - załadowanie każdej lini tekstu do listy
text_hi = """
Cześć, 
jak masz na imię? 
Pozdrawiam, 
"""

list_text_hi = text_hi.splitlines()
print(list_text_hi)

print('---')

# Wyświetelenie jako zwykły tekst, z listy
list_text_ig = ['Nowe', 'logowanie', 'na',
                'Instagramie', 'z', 'urządzenia', 'Firefox']
text_ig = " ".join(list_text_ig)

print(text_ig)

print('---')

# lista trzech najlepszych wyników (sortuje i wyświetlam top3)
scorers = [27, 8, 15, 2, 9, 10, 21, 4, 20, 5]

sorted_scores = sorted(scorers, reverse=True)

print(sorted_scores[:3])

print('---')

# Dodanie do listy Durant i wstawienie na konkretne miejsce liczby 22
players = ['LeBron', 'Kobe', 'Jordan']
scores = [27, 18, 15]

players.append('Durant')
scores.insert(2, 22)

print(players)
print(scores)

print('---')

# usuń element 'Kobe' z listy players
# wykorzystując odpowiednią metodę usuń element z indeksem równym 1 z listy scores_v2
players_v2 = ['LeBron', 'Kobe', 'Jordan', 'Durant']
scores_v2 = [27, 18, 22, 15]

players_v2.remove('Kobe')
popped_score = scores_v2.pop(1)

print(players_v2)
print(scores_v2)
print(popped_score)

print('---')

# Dodawanie list do siebie
# Można to zrobić również za pomocą extend
players = ['LeBron', 'Kobe', 'Jordan', 'Durant']
scores = [27, 18, 22, 15]

new_players = ['LeBron', 'Kobe']
new_scores = [27, 18]

print(players + new_players)
print(scores + new_scores)

print('---')

"""
utwórz pustą listę o nazwie score_stack, która służy jako stos do przechowywania wyników meczu siatkówki
dodaj początkowy wynik '0-0' do stosu
odczytaj aktualny wynik (ostatni element w liście) i wydrukuj do konsoli
dokonaj aktualizacji wyniku i dodaj do stosu wartość '1-0'
odczytaj aktualny wynik (ostatni element w liście) i wydrukuj do konsoli
dokonaj aktualizacji wyniku i dodaj do stosu wartość '1-1' 
odczytaj aktualny wynik (ostatni element w liście) i wydrukuj do konsoli
dokonaj aktualizacji wyniku i dodaj do stosu wartość '1-2' 
odczytaj aktualny wynik (ostatni element w liście) i wydrukuj do konsoli
okazało się, że po decyzji sędziego poprzedni punkt zostaje anulowany, usuń ostatni element ze stosu
odczytaj aktualny wynik (ostatni element w liście) i wydrukuj do konsoli
"""
score_stack = []
score_stack.append('0-0')
print("".join(score_stack[-1:]))
score_stack.append('1-0')
print("".join(score_stack[-1:]))
score_stack.append('1-1')
print("".join(score_stack[-1:]))
score_stack.append('1-2')
print("".join(score_stack[-1:]))
score_stack.pop()
print("".join(score_stack[-1:]))

print('---')

"""
# dodawanie kilku elementów do listy 
# wyświetl bieżące zamówienie - początek kolejki
# przetwórz pierwsze zamówienie, usuwając je z kolejki
# wyświetl bieżące zamówienie - początek kolejki
# przetwórz pierwsze zamówienie, usuwając je z kolejki
"""

order_queue = []
order_v1 = 'Pen'
order_v2 = ('Book', 'Mouse')
order_v3 = ('Notebook', 'Pencil')

order_queue.extend([order_v1, order_v2, order_v3])

print(order_queue[0])

order_queue.pop(0)

print(order_queue[0])

order_queue.pop(0)

print(order_queue[0])


print('---')

menu = [
    [
        'Spaghetti Bolognese',
        12.99,
        [
            'spaghetti',
            'tomato sauce',
            'ground beef',
            'onion',
        ],
    ],
    [
        'Caesar Salad',
        8.99,
        [
            'romaine lettuce',
            'croutons',
            'parmesan cheese',
            'Caesar dressing',
        ],
    ],
    [
        'Margherita Pizza',
        14.99,
        [
            'pizza dough',
            'tomato sauce',
            'mozzarella cheese',
            'basil',
        ],
    ],
    [
        'Cheeseburger',
        10.99,
        [
            'beef patty',
            'cheddar cheese',
            'lettuce',
            'tomato',
            'bun',
        ],
    ],
]

# wyodrębnij listę składników dla pizzy Margherita.
# W odpowiedzi posortowaną listę składników wydrukuj do konsoli.

pizzaMargherita = [item for item in menu if 'Margherita Pizza' in item]
new_pizzaMargherita = []

for item in pizzaMargherita:
    new_pizzaMargherita.extend(item)

ingredients = new_pizzaMargherita[2]
sorted_ingredients = sorted(ingredients)

print(sorted_ingredients)

print('---')

# Do menu dodajemy kolejny składnik

next_ingredients = [
    'Chicken Alfredo',
    15.99,
    [
        'fettuccine',
        'alfredo sauce',
        'chicken',
    ],
]

menu.extend(next_ingredients)

count_menu = len(menu)

print(menu[4:])

print('---')

# Do listy składników sałatki Cezar dodaj kolejny składnik na koniec listy 'olive oil'.
# Dodatkowo dokonaj także aktualizacji ceny dla sałatki Cezar na wartość 9.99.
# W odpowiedzi wydrukuj drugi element listy menu do konsoli
next_menu = [
    [
        'Spaghetti Bolognese',
        12.99,
        [
            'spaghetti',
            'tomato sauce',
            'ground beef',
            'onion',
        ],
    ],
    [
        'Caesar Salad',
        8.99,
        [
            'romaine lettuce',
            'croutons',
            'parmesan cheese',
            'Caesar dressing',
        ],
    ],
    [
        'Margherita Pizza',
        14.99,
        [
            'pizza dough',
            'tomato sauce',
            'mozzarella cheese',
            'basil',
        ],
    ],
]

caesarSalad = next_menu[1]

item_caesarSalad = caesarSalad[2]
item_caesarSalad.append('olive oil')

price_cesar = next_menu[1]
price_cesar.pop(1)
price_cesar.insert(1, 9.99)

print(price_cesar)

print('---')

# znajdź czasy odlotów podanych lotów w postaci listy (zachowaj kolejność lotów)
flights = [
    [
        'United Airlines',
        'UA123',
        'New York',
        'Los Angeles',
        '10:00 AM',
    ],
    [
        'Delta Airlines',
        'DL456',
        'Chicago',
        'Houston',
        '11:30 AM',
    ],
    [
        'American Airlines',
        'AA789',
        'Dallas',
        'San Francisco',
        '2:15 PM',
    ],
    [
        'Southwest Airlines',
        'WN012',
        'Los Angeles',
        'Denver',
        '3:45 PM',
    ],
    [
        'JetBlue Airways',
        'B620',
        'New York',
        'Miami',
        '5:00 PM',
    ],
]

hour_flight = []

for pm in flights:
    hour_flight.append(pm[-1:])

hour_list = [item for hour in hour_flight for item in hour]

print(hour_list)

print('---')

# Wykonaj poniższe kroki:
# korzystając z odpowiedniej metody usuń drugi element listy flights i przypisz do zmiennej delta_airlines
# wydrukuj do konsoli liczbę elementów w liście flights
# dodaj usunięty element delta_airlines na koniec listy flights
# do konsoli wydrukuj z każdego lotu tylko numer lotu w podanej postaci -> UA123,AA789,WN012,DL456

my_flights = [
    [
        'United Airlines',
        'UA123',
        'New York',
        'Los Angeles',
        '10:00 AM',
    ],
    [
        'Delta Airlines',
        'DL456',
        'Chicago',
        'Houston',
        '11:30 AM',
    ],
    [
        'American Airlines',
        'AA789',
        'Dallas',
        'San Francisco',
        '08:15 AM',
    ],
    [
        'Southwest Airlines',
        'WN012',
        'Los Angeles',
        'Denver',
        '09:45 AM',
    ],
]

delta_airlines = my_flights.pop(1)
print(len(my_flights))
my_flights.append(delta_airlines)

# UNPACKING
one, two, three, four = my_flights
print(f"{one[1]}, {two[1]}, {three[1]}, {four[1]}")


