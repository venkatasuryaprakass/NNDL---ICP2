def string_alternative(full_name):
    return full_name[::2]

full_name = input("enter the string:")
result = string_alternative(full_name)
print(result)