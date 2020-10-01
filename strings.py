triple_quote = """Triple quotes allow you to embed "double quotes"
as well as 'single quotes'
and can work across multiple lines"""

print(triple_quote)

# strings are immutable so cannot be changed once initiated
# you must create a new string to in order to incorporate any changes
# eg:
# triple_quote[35] = "'"

triple_quote_new = triple_quote[0:35] + "'ouble qu'" + triple_quote[43:]
print(triple_quote_new)

snack = "Chocolate cookie."
print(snack[0])
print(snack[9])
print(snack[-1])

#Range index [Start index (included): Stop index (excluded)]
print(snack[10:16])
#prints 10 - 15 inclusive
print(snack[10:-1])
print(snack[0:]) #prints whole string
print(snack[:-1]) #prints whole string minus last letter
print(snack[:]) #prints whole string

number_string = '1020304050'
print(number_string[0:-1:2]) #2 is the stride
print(number_string[::-1]) #reverses string using stride
print(number_string[::-2]) #prints all zeros
print(number_string[-2::-2]) #prints 54321

string1 = 'Chocolate'
string2 = 'cookie'
cost = 15

#must cast cost to string to print
snack = string1 + ' ' + string2 + ' ' + str(cost)
print(snack)

single_word = 'hip '
line1 = single_word * 2 + 'hurray!'
print(line1)

sub_string1 = 'ice'

if sub_string1 in 'ice cream' :
    print('There is ' + sub_string1 + " in icecream")

print(str.capitalize('cookie').islower())
str1 = '    I got you a cookie, do you like cookies?'
str2 = 'cook'
str3 = '   '
str4 = '\t'

print(str1.find(str2))
print(str1.count(str2))
print(str3.isspace()) #returns true if all whitespace
print(str4.isspace()) #also returns true for special chars
print(str1.lstrip()) #strips all leading whitespace
print(number_string.isdigit()) #returns true if all digits
print(str1.replace('cookie', 'face', 1)) #terrifying
print(len(str1)) #length of string
