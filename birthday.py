import datetime

# Названия дней недели (в Python понедельник = 0, воскресенье = 6)
WEEKDAYS = ["понедельник", "вторник", "среда", "четверг",
            "пятница", "суббота", "воскресенье"]

# Шаблоны цифр для вывода "на табло": 5 строк в высоту, 3 символа в ширину
DIGITS = {
    '0': ["***", "* *", "* *", "* *", "***"],
    '1': ["  *", "  *", "  *", "  *", "  *"],
    '2': ["***", "  *", "***", "*  ", "***"],
    '3': ["***", "  *", "***", "  *", "***"],
    '4': ["* *", "* *", "***", "  *", "  *"],
    '5': ["***", "*  ", "***", "  *", "***"],
    '6': ["***", "*  ", "***", "* *", "***"],
    '7': ["***", "  *", "  *", "  *", "  *"],
    '8': ["***", "* *", "***", "* *", "***"],
    '9': ["***", "* *", "***", "  *", "***"],
    ' ': ["   ", "   ", "   ", "   ", "   "],  # пробел-разделитель
}


def get_weekday(day, month, year):
    """Определяет день недели для заданной даты."""
    date = datetime.date(year, month, day)
    return WEEKDAYS[date.weekday()]


def is_leap_year(year):
    """Определяет, является ли год високосным."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_age(day, month, year):
    """Вычисляет, сколько лет пользователю на сегодняшний день."""
    today = datetime.date.today()
    age = today.year - year
    # если день рождения в этом году ещё не наступил — вычитаем 1
    if (today.month, today.day) < (month, day):
        age -= 1
    return age


def render_big_date(day, month, year):
    """Возвращает дату в формате 'дд мм гггг', нарисованную звёздочками."""
    date_str = f"{day:02d} {month:02d} {year:04d}"
    rows = ["", "", "", "", ""]
    for char in date_str:
        pattern = DIGITS[char]
        for i in range(5):
            rows[i] += pattern[i] + " "
    return "\n".join(rows)


def main():
    print("Введите дату своего рождения.")
    day = int(input("День: "))
    month = int(input("Месяц: "))
    year = int(input("Год: "))

    # проверяем, что такая дата вообще существует
    try:
        datetime.date(year, month, day)
    except ValueError:
        print("Такой даты не существует. Перезапустите программу.")
        return

    print()
    print(f"День недели: {get_weekday(day, month, year)}")
    print("Год високосный" if is_leap_year(year) else "Год не високосный")
    print(f"Вам сейчас: {get_age(day, month, year)} лет")
    print()
    print("Ваша дата рождения:")
    print(render_big_date(day, month, year))


if __name__ == "__main__":
    main()
