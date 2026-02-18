student={
    "name":"sameet",
    "age":21,
    "course":"python"
}
#add key
student["marks"]=90
#update value
student["age"]=22

#delete key
del student["course"]

#loop through dictionary
for key,value in student.items():
     print(key,":",value)
