import re

def filter():
    f = open("items.txt", "r")
    items = f.read()
    f.close()

    str_filter = [", {", "{'payload': {'items': [{", "]"] 

    for i in str_filter:
        items = items.replace(i, "") 

    x = re.split("}",items)

    with open("items.txt", "w") as f:
        for i in x:
            print(i, file=f)