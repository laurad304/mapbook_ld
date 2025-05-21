def get_user_info(users_data: list[dict]) -> None:
    for user in users_data:
        print(f'Twój znajomy: {user["name"]} z {user["location"]} opublikował {user["posts"]}')


def add_user(user_data: list[dict]) -> None:
    tmp_name: str = input('podaj imię: ')
    tmp_location: str = input('podaj miejsce: ')
    tmp_posts: int = int(input('podaj liczbę postów: '))
    user_data.append({'name': tmp_name, 'location': tmp_location, 'posts': tmp_posts})



def remove_user(users_data: list[dict]) -> None:
    user_name = input('Podaj imię użytkownika do usunięcia: ')
    for user in users_data:
        if user['name'] == user_name:
            users_data.remove(user)


def update_user(users_data: list[dict]) -> None:
    user_name = input('Podaj imię użytkownika do zmodyfikowania: ')
    for user in users_data:
        if user['name'] == user_name:
            user['name'] = input('Podaj nowe imię: ')
            user['location'] = input('Podaj nową lokalizację: ')
            user['posts'] = input('Podaj nową liczbę postów: ')


def get_coordinates(location_name: str) -> list:
        import requests
        from bs4 import BeautifulSoup
        adres_url: str = f'https://pl.wikipedia.org/wiki/{location_name}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')

        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),

        ]
def get_map(users_data:list[dict])->None:
    import folium
    map = folium.Map(location=[52.3 , 21.0], zoom_start=10, tiles='OpenStreetMap')
    for user in users_data:
        print(get_coordinates(user['location']))
        folium.Marker(
            location=get_coordinates(user['location']),
            popup=f'<h5>{user['location']}</h5><brt/>{user['name']}<brt/>{user['posts']}'
        ).add_to(map)
    map.save('map.html')


