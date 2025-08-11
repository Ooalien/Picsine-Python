ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[-1] = "World!"


ft_tuple = list(ft_tuple)
ft_tuple[-1] = "Maroc!"
ft_tuple = tuple(ft_tuple)

list_tmp = (list(ft_set))
if list_tmp[-1] == "tutu!":
    list_tmp[-1] = "BenGuerrir!"
else:
    list_tmp[0] = "BenGuerrir!"
ft_set = set(list_tmp)


ft_dict['Hello'] = "1337-BG!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
