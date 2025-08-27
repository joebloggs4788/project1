from abc import ABCMeta, abstractmethod
from pathlib import Path

class Director(object, metaclass=ABCMeta):
    def __init__(self):
        self._builder = None
    def set_builder(self, builder):
        self._builder = builder

    @abstractmethod
    def construct(self, field_list):
        pass
    def get_constructed_object(self):
        return self._builder.constructed_object

class Builder(object, metaclass=ABCMeta):
    def __init__(self, constructed_object):
        self.constructed_object = constructed_object

class Product(object):
    def __init__(self):
        pass
    def __repr__(self):
        pass

class ConcreteBuilder(Builder):
    pass
class ConcreteDirector(Director):
    pass

# =======================
class AbstractFormBuilder(object, metaclass=ABCMeta):
    def __init__(self):
        self.constructed_object = None
    @abstractmethod
    def add_checkbox(self,dict):
        pass
    @abstractmethod
    def add_text_field(self,dict):
        pass
    @abstractmethod
    def add_button(self,dict):
        pass

class HtmlForm(object):
    def __init__(self):
        self.field_list = []
    def __repr__(self):
        return f"<form>{"\n".join(self.field_list)}</form>"

class HtmlFormBuilder(AbstractFormBuilder):
    def __init__(self):
        self.constructed_object = HtmlForm()

    def add_text_field(self, dict):
        self.constructed_object.field_list.append(
            f'{dict["label"]}:<br><input type="text" name="{dict["field_name"]}</br>'
        )

    def add_checkbox(self, dict):
        self.constructed_object.field_list.append(
            '<label><input type="checkbox" id="{0}" value="{1}"> {2}<br>'.format(
                dict['field_id'],
                dict['value'],
                dict['label']
            )      
        )

    def add_button(self, dict):
        self.constructed_object.field_list.append(
            '<button type="button">{}</button>'.format(dict['text'])
        )

class FormDirector(Director):
    def __init__(self):
        Director.__init__(self)

    def construct(self, field_list):
        for field in field_list:
            if field["field_type"] == "text_field":
                self._builder.add_text_field(field)
            elif field["field_type"] == "checkbox":
                self._builder.add_checkbox(field)
            elif field["field_type"] == "button":
                self._builder.add_button(field)

if __name__ == "__main__":
    director = FormDirector()
    builder = HtmlFormBuilder()
    director.set_builder(builder)

    field_list = [
        {
            "field_type": "text_field",
            "label": "Best text you have ever written",
            "field_name": "Field One"
        },
        {
            "field_type": "checkbox",
            "field_id": "check_it",
            "value": "1",
            "label": "Check for on",
        },
        {
            "field_type": "text_field",
            "label": "Another Text field",
            "field_name": "Field One"
        },
        {
            "field_type": "button",
            "text": "DONE"
        }
    ]

    director.construct(field_list)
    form_str = director.get_constructed_object()

    htmlfile = Path.joinpath(Path(__file__).resolve().parent, "form_file.html")
    with open (htmlfile, "w") as outputfile:
        outputfile.write(f"<html><body>{form_str}</body></html>")

