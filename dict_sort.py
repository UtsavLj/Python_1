data=[
    {"roll":1,"age":19,"name":"rohan"},
    {"roll":2,"age":16,"name":"rohan"},
    {"roll":3,"age":122,"name":"rohan"},
    {"roll":4,"age":120,"name":"rohan"},
    {"roll":5,"age":12,"name":"rohan"},
    {"roll":6,"name":"rohan"},
    {"roll":7,"name":"rohan"},
    {"roll":8,"name":"rohan"},
    {"roll":9,"name":"rohan"},
     ]
data2=[x for x in data if "age" not in x]
data1=sorted([x for x in data if "age" in x],key=lambda x:x["age"])+data2
print(data1)
