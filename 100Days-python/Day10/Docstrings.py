from langchain.cli.create_repo.pypi_name import lint_name


def format_name(f_name, l_name):

    """Take a first and last name and format it to return the title case version of the name."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formatted_name = format_name(f_name="HaRsHa" l_name="HA")

lenght = len(formatted_name)

"""
hi my name is harsha
i am from vizag
i am working as devops enginner
""" ==> This formate is called as docstrings
