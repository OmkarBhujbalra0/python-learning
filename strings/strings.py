# String

a = "Apple"
b = 'Banana'

print(a)
print(b)

# c = "This sentence contains "two double quotes" and will return an error."
# print(c)

# Escape Sequence

d = "This string consist \"double quotes\" within double quotes."
print(d)

# Adding new line in string
e = "This is first line. \nThis is second line."
print(e)

# Adding a tab in string
f = "This is line before space. \t This is line after space."
print(f)

# String Concatenation

g = "String One"
h = "String Two"
print(g + h)

# upper() -> Uppercase all letters

i = "apple"
i = i.upper()
print(i) # APPLE

# lower() -> Lowercase all the letters

j = "Banana"
j = j.lower()
print(j) # banana

# capitalize() -> Capitalizes the string
k = "CARROT"
k = k.capitalize()
print(k) # Carrot

# split() -> Splits the characters or group of characters by passing a argument

l = "Drumsticks and Eggplants"
l = l.split(" and ") # Splits the strings wherever " and " is present 
print(l) # ["Drumsticks","Eggplants"]

# strip() -> Strips all the given string before and after the actual string

m = " Figs "
m = m.strip(" ")
print(m) # "Figs"

# join() -> Joins the elements of the list into single string with the string used to join the list,

n = ["G","i","n","g","e","r"]
n = "".join(n) # Ginger
print(n)
n = ".".join(n) # G.i.n.g.e.r
print(n)

# replace() -> replaces the occurences of characters or group of characters

o = "Herbs"
o = o.replace("rbs","lp")
print(o)

# find() -> returns the index of first occurence of character or group of characters

p = "indigo"
p = p.find("i") # 0 since the 'i' occurs first at index 0
print(p)

# Looping through the list

for item in "apple":
    print(item)

# Membership Testing

if "app" in "Apple": # returns nothing since "app" is not present in "Apple"
    print(True) 

if "ban" in "banana": # returns True since "ban" is present in "banana"
    print(True)
