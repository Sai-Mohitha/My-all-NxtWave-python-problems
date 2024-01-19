def shuffle_string(string, indices_list):
    new_string = ""
    indices_list = indices_list.split()
    
    for index in indices_list:
        index = int(index)
        new_string += string[index]

    return new_string

string = input()
indices_list = input()

result = shuffle_string(string, indices_list)
print(result)