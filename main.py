users:list[dict] =[
    {'name': 'Laura', 'location': 'Łuków', 'post': 500, },
    {'name': 'Wika', 'location': 'Radzyń Podlaski', 'post': 450, },
    {'name': 'Daria', 'location': 'Łosice', 'post': 300, }
]


for user in users:
    print(f'Twój znajomy: {user["name"]} z miejscowości {user["location"]} opublikował {user["post"]} postów')
