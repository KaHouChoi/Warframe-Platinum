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
    
    items = {}
    dict_filter = re.compile(r'''
        ^\A'thumb':\s'(.+\bpng)
        .+\bid':\s'(.+)
        ',\s'url_name':\s'(.+)
        ',\s'item_name':\s'(.+)'
    ''',re.VERBOSE                       
    )                       
    f = open("items.txt", "r")
    while line := f.readline():
        mo = dict_filter.search(line)
        if mo: 
            temp_dict = {
                "thumb": mo.group(1),
                "id": mo.group(2),
                "url_name": mo.group(3)
            }
            items[mo.group(4)] = temp_dict
    return items
