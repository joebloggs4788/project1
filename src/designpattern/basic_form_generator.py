import os
from pathlib import Path


def get_cwd():
    htmlfile = Path.joinpath(Path(__file__).resolve().parent, "form_file.html")
    print(htmlfile)

def generate_webform(field_list:list) -> str:
    generated = "\n".join(
        map(lambda x: '<br>{0}:<input type="text" name="{0}"<br>'.format(x),
            field_list
        )
    )
    return '<form>\n{fields}\n</form>'.format(fields = generated)

def build_html_form(fields):
    cwd = os.path.dirname(os.path.abspath(__file__))

    # script_directory = Path(__file__).resolve().parent

    # htmlfile = os.path.join(cwd,"form_file.html")
    # with open(htmlfile, "w") as f:
    with open(f"{cwd}/form_file.html", "w") as f:
    
        f.write(
        "<html><body>{}</body></html>".format(generate_webform(fields))
        )


if __name__ == '__main__':
    # field_list = ["name", "age", "email", "telephone"]
    # build_html_form(field_list)

    # html = generate_webform(field_list)
    # print(html)

    get_cwd()

