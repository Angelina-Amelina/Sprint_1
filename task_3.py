world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
    2022: 'Аргентина'
}

for champions in world_champions.keys():
    print(champions, '-', world_champions[champions])

country = 'Италия'

if country in world_champions.values():
    print ('Италия cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print ('Италия не выигрывала чемпионат мира по футболу в 21 веке.')
