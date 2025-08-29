
import sys
import mvc_two_models_model as model
import mvc_two_models_view


class GreetingController(object):
    def __init__(self):
        self.name_model = model.NameModel()
        self.time_model = model.TimeModel()
        self.view = mvc_two_models_view.GreetingView()
    def handle(self, request):
        if request in self.name_model.get_name_list():
            self.view.generate_greeting(
            name=request,
            time_of_day=self.time_model.get_time_of_day(),
            known=True
            )
        else:
            self.name_model.save_name(request)
            self.view.generate_greeting(
            name=request,
            time_of_day=self.time_model.get_time_of_day(),
            known=False
            )

def main(name):
    request_handler = GreetingController()
    request_handler.handle(name)

if __name__ == "__main__":
    main(sys.argv[1])

