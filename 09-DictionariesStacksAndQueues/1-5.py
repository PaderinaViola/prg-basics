

countries = [
{"name":"Poland", "population":38000000},
{"name":"Ukraine", "population":37000000},
{"name":"Germany", "population":80000000},
{"name":"French", "population":20000000},
{"name":"Australia", "population":40000000},
]

print("COUNTRY  POPULATION")
for cont in countries:
    print(f"{cont['name']}: {cont['population']}")