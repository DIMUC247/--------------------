from datetime import datetime
from pprint import pprint

from functions.animals import (
    show_all_anims,
    add_anims,
    add_anim,
    del_anim_by_name,
    del_anim_by_numb,
    show_sorted_anims,
    cured_anim,
    find_numb_anim_by_name,
    show_cured_anims,
    show_cure_history,
    find_palidrome,
)
from functions.employees import (
    add_employee,
    del_employee,
    show_employees,
    change_salary,
    change_position
)
from functions.password import is_verify_password, generate_password
from functions.reviews import add_review, find_repeated_chars
from files import list_files
from functions import open_files, save_files


def help():
    with open(list_files.help, "r", encoding="utf-8") as fh:
        print(fh.read())


def exit() -> None:
    print("До побачення")
    quit()


def show_log(log: list) -> None:
    pprint(log, width=200)


def show_most_using_commands(most_using_command: dict) -> None:
    pprint(most_using_command)


def unknowing_command() -> None:
    print("Невідома команда. Спробуйте ще раз.")


def main():
    animals = open_files.animals
    animals_cured = open_files.animals_cured
    reviews = open_files.reviews
    employees = open_files.employees
    log = open_files.log
    most_using_command = open_files.most_using_command

    user_name = input("Введіть свій логін: ")
    pass_word = employees.get(user_name, {}).get("password", "")

    while not pass_word:
        position = input("Введіть свою посаду: ")
        salary = input("Введіть свою ЗП: ")
        name = input("Введіть своє ім'я: ")
        employees[user_name] = {
            "position": position,
            "salary": salary,
            "name": name,
            "start_date": datetime.now().strftime("%d.%m.%Y")
        }

        command = input("Введіть 'create' для введення свого паролю;\nВведіть 'generate' для автоматичної генерації паролю.\nАбо будь який символ для виходу з програми\n-> ")
        if command == "create":
            password = input("Введіть пароль 8 і більше символів, цифра і буква: ")

            if is_verify_password(password):
                pass_word = password
            else:
                print("Пароль не пройшов перевірку")

        elif command == "generate":
            len_password = input("Введіть довжину пароля: ")
            if len_password.isdigit() and int(len_password) > 8:
                len_password = int(len_password)
            else:
                len_password = 8

            is_upper = input("Введіть 1 щоб використати великі букви: ")
            is_upper = True if is_upper == "1" else False
            is_punctuation = input("Введіть 1 щоб використовувати спецсимволи: ")
            is_punctuation = True if is_punctuation == "1" else False
            is_repeate = input("Введіть 1 щоб символи повторювались: ")
            is_repeate = True if is_repeate == "1" else False
            password = generate_password(len_password=len_password, is_upper=is_upper, is_punctuation=is_punctuation, is_repeate=is_repeate)
            if is_verify_password(password):
                pass_word = password
            else:
                print("Пароль не пройшов перевірку")

    else:
        print(f"\nВаш пароль '{pass_word}' успішно створено. Запам'ятайте його для входу в систему.\n")

    password = input("Введіть свій пароль для входу в систему: ")

    command = None
    while pass_word == password:
        if not command:
            log.append(f"Користувач з логіном '{user_name}' увійшов у систему: {datetime.now()}")
            print("Доброго дня. Вітаємо в нашій інформаційній системі")

        command = input("Введіть команду (help для допомоги): ")
        log.append(f"Користувач з логіном '{user_name}' ввів команду {command}: {datetime.now()}")

        if command in most_using_command:
            most_using_command[command] += 1
        else:
            most_using_command[command] = 1

        match command:
            case "show_all_anims":
                show_all_anims(animals)
            case "add_anim":
                animals = add_anim(animals)
            case "add_anims":
                animals = add_anims(animals)
            case "del_anim_by_name":
                animals = del_anim_by_name(animals)
            case "del_anim_by_numb":
                animals = del_anim_by_numb(animals)
            case "show_sorted_anims":
                show_sorted_anims(animals)
            case "cured_anim":
                animals, animals_cured = animals_cured(animals, animals_cured)
            case "find_numb_anim_by_name":
                find_numb_anim_by_name(animals)
            case "show_cured_anims":
                show_cured_anims(animals_cured)
            case "show_cure_history":
                show_cure_history(animals_cured)
            case "exit":
                save_files.save_animals(animals)
                save_files.save_employees(employees)
                save_files.save_log(log)
                save_files.save_most_using_command(most_using_command)
                save_files.save_animals_cured(animals_cured)
                save_files.save_reviews(reviews)
                exit()
            case "add review":
                reviews = add_review(reviews)
            case "find repeated chars":
                find_repeated_chars(reviews)
            case "find palidrome":
                find_palidrome(animals)
            case "add employee":
                employees = add_employee(employees)
            case "del employee":
                employees = del_employee(employees)
            case "show employees":
                show_employees(employees)
            case "change salary":
                employees = change_salary(employees)
            case "change position":
                employees = change_position(employees)
            case "show log":
                show_log(log)
            case "show most using commands":
                show_most_using_commands(most_using_command)
            case "help":
                help()
            case _:
                unknowing_command()

        input("\nНатисніть 'enter' для продовження\n")
    else:
        print("Пароль невірний, доступ заборонено")


if __name__ == "__main__":
    main()
