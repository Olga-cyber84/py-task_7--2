from pprint import pprint
file_name = 'recipes.txt'

cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}


def get_shop_list_by_dishes(dishes, person_count):
    dishes_ingredients = []  # список всех ингредиентов из заказанных блюд
    for item in dishes:
        dishes_ingredients.extend(cook_book[item])
    # pprint(dishes_ingredients)

    ingredients_uniq = set()

    for item in dishes_ingredients:
        ingredients_uniq.add(item['ingredient_name'])
    # print('ingredients_uniq', ingredients_uniq)

    products = {}
    for uniq in ingredients_uniq:
        product_quant = 0
        for item in dishes_ingredients:
            if item['ingredient_name'] == uniq:
                product = uniq
                product_quant += item['quantity']*person_count
                products[product] = {
                    'measure': item['measure'], 'quantity': product_quant}

    pprint(products)


dishes = ['Омлет']  # список блюд
person_count = 2

get_shop_list_by_dishes(dishes, person_count)
