name = "sri"
age = 25
hobby = "playing"
# multiline 
print("Name:", name, "Age:", age)
# f string
print(f"{name} is {age} and {hobby}")
# % operator
print("%s is %d years old." % (name, age))
# sring format
print("{} is {} years old.".format(name, age))
#seprator
print("Hello", "World", sep="-")  
#end
print("hello", end=",")
print("world!")
# get the deatils from file and change and read the file
# Open the file in write mode
with open("output.txt", "w") as f:
    print("Hello, World!", file=f)
    print("This is a second line.", file=f)
    print("And this is the third line.", file=f)

# Optionally, read back the contents to verify
with open("output.txt", "r") as f:
    contents = f.read()
    print("Contents of the file:")
    print(contents)




