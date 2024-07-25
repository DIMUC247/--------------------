def show_all_anims(animals: list) -> None:
    template = "|{:^5}|{:<30}|"
    delimiter = "—" * 38
    head = template.format("№", "назва тварини")
    print(delimiter)
    print(head)
    print(delimiter)
    for i, product in enumerate(animals, start=1):
        print(template.format(i, product))

    print(delimiter)


def add_anim(animals: list) -> list:
    animal = input("Введіть новий тварину для додавання до списку: ")

    if animal not in animals:
        animals.append(animal)
        print(f"\nтварина '{animal}' доданий до списку")
    else:
        print("\nТака тварина вже є у списку")

    return animals


def add_anims(animals: list) -> list:
    anims = input("Введіть список тварин для додавання через пробіл\n-> ")
    anims = anims.split()
    animals.extend(anims)
    print("\nСписок тварин розширено")
    return animals


def del_anim_by_name(animals: list) -> list:
    animal = input("Введіть назву тварини для видалення зі списку тварин: ")

    if animal in animals:
        animals.remove(animal)
        print(f"\nТварину '{animal}' видалено зі списку")
    else:
        print("\nТакогї тварини немає у списку")

    return animals


def del_anim_by_numb(animals: list) -> list:
    index = input("Введіть номер тварини для видалення зі списку: ")

    if index and index.isdigit() and 0 < int(index) <= len(animals):
        animal = animals.pop(int(index) - 1)
        print(f"Тварину '{animal}' видалено зі списку")
    else:
        print("Ви ввели не вірний номер тварини")

    return animals


def show_sorted_anims(animals: list) -> None:
    anims = sorted(animals)
    for animal in anims:
        print(animal)


def cured_anim(animals: list, animals_cured: list) -> tuple[list, list]:
    animal = input("Введіть назву тварини для вилікування: ")

    if animal in animals:
        animals.remove(animal)
        animals_cured.append(animal)
        print(f"\nТварину '{animal}' вилілкувано. Натисніть 'Enter' для продовження ")
    else:
        print("\nТакої тварини немає у списку. Натисніть 'Enter' для продовження ")

    return animals, animals_cured


def find_numb_anim_by_name(animals: list) -> None:
    animal = input("Введіть назву тварини для пошуку: ")

    if animal in animals:
        index = animals.index(animal)
        print(f"Тварина '{animal}' знаходиться під номером {index + 1}.")
    else:
        print("\nТакої тварини немає у списку.")


def show_cured_anims(animals_cured: list) -> None:
    if not animals_cured:
        print("Список вилікуваних тварин пустий")

    for animal in animals_cured:
        print(animal)


def show_cure_history(animals_cured: list) -> None:
    anims_cured = animals_cured[::-1]
    for animal in anims_cured:
        print(animal)


def find_palidrome(animals: list) -> None:
    palin_anim = []
    for animal in animals:
        if animal.lower() == animal[::-1].lower():
            palin_anim.append(animal)

    message = f"В списку тварин є такі тварини-паліндроми:\n{palin_anim}" if palin_anim else "В списку тварин відсутні слова паліндроми."
    print(message)
