from utills.controller import get_user_info
from utills.model import users


def main():
    while True:
        print('==========MENU==========')
        print('0 - Exit')
        print('1 - Get user info')
        print('========================')

        choice = input ('enter your choice ')
        if choice == '0':
            break
        if choice == '1':
            get_user_info(users)



if __name__ == '__main__':
    main()