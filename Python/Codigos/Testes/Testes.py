frutas = {

"melancia": {"quantidade" : 4, "preco": 10},
"pera": {"quantidade": 2, "preco": 3},
"uva": {"quantidade" : 8, "preco" : 8},
"ameixa": {"quantidade": 5, "preco": 2},
"abacaxi": {"quantidade" : 15, "preco" : 4},
"banana": {"quantidade": 6, "preco": 4}
}

fruta = frutas.keys()

fruta_ = [fruta['quantidade'] for fruta in frutas]

print(fruta_)

# if fruta["quantidade"] <= 7]