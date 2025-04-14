def get_user_info (users_data:list[dict])->None:
    for user in users_data:
        print(f'Twój znajomy: {user["name"]} z miejscowości {user["location"]} opublikował {user["post"]} postów')

def add_user(user_data: list[dict])->None:
    tmp_name:str = input('podaj imię: ')
    tmp_location:str = input('podaj miejsce: ')
    tmp_posts:int = int( input('podaj liczbę postów: '))
    user_data.append ({'name': tmp_name, 'location': tmp_location, 'post': tmp_posts})

def remove_user(users_data: list[dict]) -> None:
    user_name = input('podaj imię użytkownika do usunięcia: ')
    for user in users_data:
        if user['name'] == user_name:
            users_data.remove(user)