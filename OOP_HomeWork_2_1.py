from pprint import pprint


cook_book = {}
with open("recipes.txt", "rt", encoding="utf-8") as file:
    dish = ""
    for x in file:
        x = x.strip()
        if x.isdigit():
            continue
        elif x and "|" not in x:
            cook_book[x] = []
            dish = x
        elif x and "|" in x:
            a, b, c = x.split(" | ")
            cook_book.get(dish).append(
                dict(ingredient_name=a, quantity=int(b), measure=c)
            )

pprint(cook_book)


def ingredients_list(dishes_list, person_count):
    shop_list = {}
    for dish in dishes_list:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient["ingredient_name"] in shop_list:
                    shop_list[ingredient["ingredient_name"]]["quantity"] += (
                        ingredient["quantity"] * person_count
                    )
                else:
                    shop_list[ingredient["ingredient_name"]] = {
                        "measure": ingredient["measure"],
                        "quantity": (ingredient["quantity"] * person_count),
                    }
        else:
            print("Такого блюда нет в книге")
    return shop_list


def create_shop_list():
    dishes_list = input("Выберети блюда: ").split(", ")
    person_count = int(input("Количества человек: "))
    pprint(ingredients_list(dishes_list, person_count))


create_shop_list()
