# Dictionary is nothing but key value pairs
#d1 = {}
#print(type(d1))
d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
d2["Ankit"] = "Junk Food"
d2[420] = "Kebabs"
#print(d2)
#del d2[420]
#print(d2)
#print(d2["Shubham"])
#d4=d2.copy()
#d3 = d2


#del d3["Harry"]
#print(d4)
#print(d2)
d2.update({"Leena":"Toffee"})
#print(d2)
#print(d2.keys())
print(d2.items())
