def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


# if __name__ == '__main__':
#     formatted_name = format_name("harsha","reddy")
#     print(formatted_name)



print(format_name(input("What is your first name?"), input("What is your last name")))

