import pulp

# Визначаємо змінні проблеми
model = pulp.LpProblem("Максимальна_кількість_продуктів", pulp.LpMaximize)

# Змінні представляють кількість вироблених одиниць кожного продукту
lemonade = pulp.LpVariable("Лимонад", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Фруктовий_сік", lowBound=0, cat='Integer')

# Функція цілі: максимізувати загальну кількість вироблених продуктів
model += lemonade + fruit_juice

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Вода"
model += 1 * lemonade <= 50, "Цукор"
model += 1 * lemonade <= 30, "Лимонний_сік"
model += 2 * fruit_juice <= 40, "Фруктове_пюре"

# Розв'язуємо проблему
model.solve()

# Виводимо результати
lemonade_units = lemonade.varValue
fruit_juice_units = fruit_juice.varValue
total_products = lemonade_units + fruit_juice_units

print("Кількість лимонаду:", lemonade_units)
print("Кількість фруктового соку:", fruit_juice_units)
print("Загальна кількість продукції:", total_products)
