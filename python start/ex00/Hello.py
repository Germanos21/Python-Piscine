ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

lst = list(ft_tuple)
lst[1] = "United Arab Emirates!"
ft_tuple = tuple(lst)

ft_set.remove("tutu!")
ft_set.add("Abu Dhabi!")

ft_dict.update({"Hello" : "42 Abu Dhabi!"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)