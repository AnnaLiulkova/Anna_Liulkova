def split_strings_list():
    user_input = input("Введіть список рядків (або слів) через пробіл: ")
    original_list = user_input.split()
    
    list1 = []
    list2 = []

    for item in original_list:
        if original_list.count(item) == 1:
            list1.append(item)
        else:
            if item not in list2:
                list2.append(item)

    print(f"Початковий список: {original_list}")
    print(f"Список 1 (зустрічаються лише один раз): {list1}")
    print(f"Список 2 (зустрічаються більше одного разу): {list2}")

if __name__ == "__main__":
    split_strings_list()