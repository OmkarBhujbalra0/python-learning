# Strings

Strings are basically collection of numbers, characters and symbols.
- It is defined by single or double quotes.

```
a = 'Single Quotes'
b = "Double Quotes"
print(a)
print(b)
```

Strings are immutable, meaning you cannot modify the string.
Even the string functions create new string instead of modifying the content of original string.

You can combine both single and double quotes for strings.

```
c = "'Insert an random quote' - User"
print(c)
```

- Note - If you try to use double quotes within double quotes or single quotes within single quotes, it will return error, because it can create two or more strings instead of single string plus also cause syntax error.
- In the code below, there is double quotes within double quotes due to which, `"This sentence contains "` becomes one string and `" and will return an error"` becomes another string, the `two double quotes` part returns error and trying to assign two strings to single variable will return an syntax error.
```
d = "This sentence contains "two double quotes" and will return an error."
print(d)
```

## Escape Sequences

As you seen above using single quotes within single quotes or double quotes within quotes will return syntax error, because each pair of quotes is considered as a separate string, escape sequences allow you to include such characters that will not work in intended in normal conditions.
- Escape sequences are used using `\`.

```
e = "This string consist \"double quotes\" within double quotes."
print(e)
```

- You can also include new line or tab in string using escape sequences.

```
f = "This is first line. \nThis is second line."
print(f)

g = "This is line before tab. \t This is line after tab."
print(g)
```

## Multiline String

- You can write a string contains multiple lines using triple single or double quotes.

```
h = '''This is a multiline string.
This is written using single quotes.
'''

i = """This is another multiline string.
This is written using double quotes.
"""

print(h)
print(i)
```

## String Concatenation

- You can join two strings by using `+` operator.

```
j = "String One"
k = "String Two"
print(j + k)
```

## String Functions

1. `upper()` function - The upper() function basically creates a new string with all the characters in uppercase.

```
l = "apple"
l = l.upper() # The new string in uppercase is created and assigned to variable l.
print(l)
```

2. `lower()` function - The lower() function basically creates a new string with all the characters in lowercase.

```
m = "Apple"
m = m.lower() # The new string in lowercase is created and assigned to variable m.
print(m)
```

3. `capitalize()` function - The capitalize() function basically creates a new string where first character is capitalized.

```
n = "apple"
n = n.capitalize() # The new capitalized string is created and assigned to variable n.
print(n)
```