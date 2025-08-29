from pprint import *

def main(username,email):
    try:
        users = {}
        with open('names_data.txt', 'r') as name_file:
            for line in name_file.readlines():
                user = line.strip().split(',')
                if len(user) == 2:
                    # users[user[0]] = user[1]
                    users.update({user[0] : user[1]})
    except  FileNotFoundError:
        with open('names_data.txt', 'w') as name_file:
            # name_file.write(f'{username},{email}')
            # users = {username : email}
            pass

    pprint(users)
    if username in users:
        print(f"welcome back {username}: {users[username]}")
    else:
        users.update({username:email})
        with open('names_data.txt','a') as name_file:
            name_file.write(f'{username},{email}\n')
    pprint(users)

if __name__ == "__main__":
    while True:
        answer = input("type in your information to register: <name>,<email>: ")
        if answer == 'q':
            break
        name, email = answer.split(',')
        main(name,email)

    



