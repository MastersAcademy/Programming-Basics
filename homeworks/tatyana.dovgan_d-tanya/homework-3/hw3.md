Модель з реального світу: Кава

Клас: Напій з кави який містить кавові зерна смажені мелені і гарячу воду

Обєкт: Кава американо

Наслідування: Кава американо з молоком і цукром

Інкапсуляція: Споживач може не знати скільки кавових зерен помелено для цієї чашки кави

Поліморфізм: Дія споживача з кавою - пити. Каву можна пити з чашки, або пити через трубочку

Принципи Solid:

Single responsibility: призначення кави - пити її

Open - closed: Кава відкрита до розширення - туди можна досипати цукру, налити молока чи вершків, але при цьому це залишиться кавою, а змінити її на чай уже не вийде

Liskov substitution: "Потомка" каву з цукром можна замінити її "предка" каву без цукру, при  цьому зберігається її основне призначення - каву без цукру також можна пити.

Interface segregation: каву можна пити напряму з чашки, можна через трубочку, можна набирати в ложку і пити з ложки

Dependency inversion: при створенні нових рецептів кави за основу беруть базовий рецепт кави (в новому напої повинні бути мелені смажені кавові зерна і вода) і потім до нього додають щось нове. Базовий рецепт кави не залежить від деталей реалізації "потомків" - наприклад, від рецепту кави Капучіно.
