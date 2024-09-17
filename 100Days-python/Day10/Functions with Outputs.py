def format_name(f_name, l_name):
    print(f_name.title())  ## This title case use to print the first letter captial letter and rest all the letters are small
    print(l_name.title())

format_name(f_name="harsha", l_name="HARSHA")


def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return (f"{formated_f_name} {formated_l_name}")

print(format_name(f_name="ReDdY", l_name="REDDY"))



def function_1(text):
    return text + text
## The output will be "hellohello"


def function_2(text):
    return text.title()

output = function_2(function_1("hello"))  ## here this statement help us to print the function_1 result to the function_2
print(output)


