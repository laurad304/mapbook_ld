def get_user_info (users_data:list[dict])->None:
    for user in users_data:
        print(f'Twój znajomy: {user["name"]} z miejscowości {user["location"]} opublikował {user["post"]} postów')
