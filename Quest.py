player = {
    "Имя": "Данил",
    "health": 200,
    "coins": 100,
    "turns": 0,
    "inventory": []
}

def show_status(player):
    print("\n--- Твои характеристики ---")
    for key, values in player.items():
        print(f"{key} - {values}")
    print("---------------------------")
    
def start():
    print("\nТы приехал за девяткой. Перед тобой стоит владелец и машина. Что будешь делать?:")
    print("1. Подойти к продавцу и поздороваться")
    print("2. Подойти к машине и рассмотреть её")
    print("3. Уйти, зачем она?")
    choice = input("\nТвой выбор (1, 2 или 3): ").strip()
    return choice

def lada_zubilo(player):
    print("\nТы подошел к машине и начал её осматривать. Какие твои первые действия?")
    print("1. Открыть капот")
    print("2. Открыть водительскую дверь и сесть в салон")
    print("3. Пойти смотреть под машину (там что-то блестит)")
    print("4. Отойти от машины назад")
    
    while True:
        choice = input("\nТвой выбор: ").strip()
        
        if choice == "1":
            print("Ты открыл капот. Двигатель весь в масле, но вроде работает. (Пока тут ничего нет)")
        elif choice == "2":
            print("Ты сел в салон. Пахнет старым освежителем и дедовскими духами. (Пока тут ничего нет)")
        elif choice == "3":
            print("\nТы полез под машину и увидел сабвуфер и чернитель резины.")
            print("Чтобы забрать чернитель, реши головоломку!")
            player = pokupka(player)
            return player
        elif choice == "4":
            print("\nТы отошел от машины.")
            return player
        else:
            print("Не понял тебя, введи 1, 2, 3 или 4.")

def pokupka(player):
    print("\nВведи слово-палиндром (читается одинаково в обе стороны, например 'казак' или 'шалаш').")
    print("(Введи 'выйти', чтобы отказаться и уйти)")
    
    while True:
        word = input("Твое слово: ").lower().strip()
        
        if word == "выйти":
            print("Ладно, оставил чернитель себе.")
            break
            
        # Проверяем, является ли слово палиндромом
        if word == word[::-1]: 
            print("Молодец! У тебя появился чернитель резины от Юры Волкова!")
            player["inventory"].append("Чернитель резины")
            break
        else:
            print("Братан, подумай лучше, это не палиндром.")
            
    return player


print()
print("*** Добро пожаловать в Челны! ***")
print()

while player["health"] > 0:
    player["turns"] += 1
    show_status(player)
    choice = start()

    if choice == "1":
        print("\nПродавец решил протянуть руку первым. 'Здарова, братан! Смотри, машина огонь, только подвеску глянь', - сказал он.")
        player = lada_zubilo(player)
        
    elif choice == "2":
        player = lada_zubilo(player)
        
    elif choice == "3":
        print("\nТы решил уехать, оставил честь! Игра окончена.")
        break                              

    else:
        print("\nНе получилось. Введи 1, 2 или 3.")

print("\nСпасибо за игру!")