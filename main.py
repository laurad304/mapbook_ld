from utills.controller import get_user_info, add_user, remove_user, update_user, get_coordinates, get_map
from utills.model import users


def main():
    while True:
        print('==========MENU==========')
        print('0 - Exit')
        print('1 - Get user info')
        print('2 - Add user')
        print('3 - Remove user')
        print('4 - Update user')
        print('========================')

        choice = input('enter your choice ')
        if choice == '0':
            break
        if choice == '1':
            get_user_info(users)
        if choice == '2':
            add_user(users)
        if choi5ce == '3':
            remove_user(users)
        if choice == '4':
            update_user(users)


if __name__ == '__main__':
    main()
