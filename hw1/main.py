# === ВАРИАНТ ===
# ДЗ1 · вариант для: VVD2409
# Календарь вашей планеты. Годы считаются с нулевого.
#
# Високосность: год високосный, если делится на LEAP_A, кроме тех,
# что делятся на LEAP_B, но делящиеся на LEAP_C — снова високосные.
LEAP_A = 5
LEAP_B = 70
LEAP_C = 280

# Месяцы по порядку: (название, дней в обычный год, дней в високосный год).
# Пользователь вводит номер месяца, первый месяц — номер 1.
MONTHS = [
    ("Жоситень", 37, 39),
    ("Рапетень", 34, 34),
    ("батень", 33, 35),
    ("Посодарь", 20, 20),
    ("Дипаполь", 28, 28),
    ("Лесуль", 38, 38),
    ("Витень", 30, 31),
    ("Бегура", 31, 31),
    ("Тёмноватикетень", 20, 20),
    ("  Зишотень  ", 35, 35),
    ("Лужурь", 21, 21),
    ("Бупедарь", 26, 26),
    ("РИШУР", 21, 21),
]

# Дни недели по порядку. Сколько названий — столько дней в неделе.
WEEKDAYS = [
    "Воруник", "Кежерник", "Жумонка", "Вованка", "Шадотень", "Зорник",
    "Золад", "Панунка", "Биветень", "Гогуник",
]

# Каким днём недели было 1-е число первого месяца года 0:
# индекс в списке WEEKDAYS (считая с нуля).
FIRST_WEEKDAY = 6

# Проверьте себя:
#   год 1890 — не високосный, в нём 374 дня;
#   год 4480 — високосный, в нём 379 дней;
#   1-е число месяца №12 в 2075 году — Вованка.
# === КОНЕЦ ВАРИАНТА ===

# Обработка предварительных данных
months_clean = [(i[0].strip().capitalize(), *i[1:]) for i in MONTHS]

print("-"*20)
# Создаем две переменные для ввода года и месяца    
my_year = int(input("Введите год: "))

# Создаем счетчик для количества дней в этом году
count_days = 0

# Создаем условие для определение типа года и количества дней в нем
if my_year < 0:
    print("Годы считаются с нулевого. Попробуй снова!)")
elif my_year % LEAP_A == 0 and (my_year % LEAP_B != 0 or my_year % LEAP_C == 0):
    for months in months_clean:
        count_days += months[2]
    print(f"Результат: год {my_year} - високосный, и в нем {count_days} дня(дней)")
else:
    for months in months_clean:
        count_days += months[1]
    print(f"Результат: год {my_year} -  не високосный, и в нем {count_days} дня(дней)")

print("-"*20, end="\n")

# Создаем календарь
calendar_year = int(input("Введите год: "))

if calendar_year < 0:
    print("Годы считаются с нулевого. Попробуй снова!)")

calendar_month = int(input("Введите месяц: "))

if calendar_month < 1 or calendar_month > len(months_clean):
    print("Такого месяца нет.")

# Расчет количества дней до (calendar_year - 1)
total_days = 0

if calendar_year > 0:
    for k in range(calendar_year):
        total_day_years = 0
        if k % LEAP_A == 0 and (k % LEAP_B != 0 or k % LEAP_C == 0):
            for months in months_clean:
                total_day_years += months[2]
        else:
            for months in months_clean:
                total_day_years += months[1]
        total_days += total_day_years
        
# Расчет количества дней в calendar_year до (calendar_month - 1)
total_days_ty = 0

if calendar_year % LEAP_A == 0 and (calendar_year % LEAP_B != 0 or calendar_year % LEAP_C == 0):
    for m in range(calendar_month - 1):
        total_days_ty += months_clean[m][2]
else:
    for m in range(calendar_month - 1):
        total_days_ty += months_clean[m][1]

total_days += total_days_ty

# Расчет дней заданного месяца 
if calendar_year % LEAP_A == 0 and (calendar_year % LEAP_B != 0 or calendar_year % LEAP_C == 0):
    my_months_days = months_clean[calendar_month - 1][2]
else:
    my_months_days = months_clean[calendar_month - 1][1]


# Теперь создаем календарь для вывода 

# Задаем столбец, в котором начинается первый день месяца
first_day_index = (FIRST_WEEKDAY + total_days) % len(WEEKDAYS)

# Задаем ширину столбца по названиям дней недели
weekday_labels = [name[:3] for name in WEEKDAYS]
widths = [max(len(label), 3) + 1 for label in weekday_labels]

# Задаем форматирование для вывода заголовка таблицы
month_name = months_clean[calendar_month - 1][0]
print()
print(f"{month_name} {calendar_year}".center(sum(widths)))

# Выводим заголовки дней недели
for i, label in enumerate(weekday_labels):
    print(label.rjust(widths[i]), end="")
print()

# Пустые ячейки до первого дня месяца
cells = [""] * first_day_index + list(range(1, my_months_days + 1))

# Дополняем пустыми ячейками до конца недели
cells += [""] * ((-len(cells))% len(WEEKDAYS))

# Выводим календарь
week_length = len(WEEKDAYS)

for start in range(0, len(cells), week_length):
    for column in range(week_length):
        cell = cells[start + column]
        print(str(cell).rjust(widths[column]), end="")
    print()

print()























