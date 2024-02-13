# list datastructure
my_list = ["Kenya", "Nigeria", "Tanzania", "Uganda", "Brazil", "Sweden"]
my_num = [2, 8, 1, 34, 27, 9, 0, -1, 23]
my_num.sort()
my_list.sort()
print(my_list)
my_list[2] = "South Africa"
print(my_list[2])
print(f"i am from {my_list[0]}")
print(f"Is {my_list[4]} in Africa?")
print(my_num)

# tuple datastructures
my_tuple = ("Banana", "Apple", "Orange", "Watermelon")
# my_tuple[1]="Guava"
print(my_tuple)

# set datastructures
my_set = {"Toyota", "Nissan", "BMW", "Mercedes", "Subaru"}
my_set.add("Defender")
print(type(my_set))
print(my_set)
print(len(my_set))

# dictionaries datastructure
my_dic = {"name": "Martin", "age": 82, "gender": "Male"}
print(my_dic)
print(f"My age is {my_dic['age']}")
