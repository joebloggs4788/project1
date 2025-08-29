# initial grouping of functions

# def main(name):
#     print(get_message(name))

class GreetingView():
    def __init__(self):
        pass

    def generate_greeting(self, name, instore):
        if name == 'lion':
            return f'roooarrr\n'
        elif instore:
            return f"Welcome back, {name}\n"
        else:
            return f"Glad to have you onboard, {name}\n"
        
    def update_view(self, greeting):
        print(greeting, sep='\n')

