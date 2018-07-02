str_list = ["43", "efwer", "", "wetefd", ""]

str_list = list(filter(lambda x: not x, str_list))

print(str_list)