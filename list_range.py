cities_list = ["New York", "Nairobi", "Berlin", "Frankfurt", "London"] 
print(cities_list[0:4])
print(cities_list[-4:])
#negative indexes
#To list the last items, use negative index followed by a full colon sign eg print(cities_list[-4:].)
print(cities_list[-3:-1])
cities_list[1:3] = "Toronto","Manitoba", 
print(cities_list)
cities_list.insert(0, "California")
print(cities_list)