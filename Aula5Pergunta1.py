produtos = [
    {"Prot":"Tv 50 polegadas","marca":"Samsung"},
    {"Prot":"Micro-ondas 10 litros", "marca":"Panasonic"},
    {"Prot": "Iphone 15 pro max", "marca": "Apple"},
    {"Prot": "Smartphone redmi note 13", "marca": "Xiaomi"},
    {"Prot":"Lavadora 10 kg", "marca": "Brastemp"}

]
for produto in produtos:
    nome = produto["Prot"]
    marca = produto["marca"]

    print(f"Produto = {nome}, Marca = {marca}")
