d = { "Jabroni":"Patron Tequila", "School Counselor":"Anything with Alcohol", "Programmer":"Hipster Craft Beer",
"Bike Gang Member":"Moonshine", "Politician":"Your tax dollars", "Rapper":"Cristal"}

def get_drink_by_profession(param):
    if param.title() in dick:
        return dick[param.title()]
    else:
        return 'Beer'


print(get_drink_by_profession('Eric'))

