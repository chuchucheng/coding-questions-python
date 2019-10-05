name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# 制表符\t
# 换行符\n

name.rstrip()  #right
name.lstrip()  #left
name.strip()   #both

3 ** 3

str(23)

#list
names = ["peter",'mary','jack']
names.append('lisa')
names.insert(0,'ella')
del names[0]


popped_names = names.pop()
print(names)
print(popped_names)
names.pop(0)


nocome = 'jack'
 names.remove(nocome)
print(names)
print("\n" + nome.title() + " is not coming.")

names.sort() # permanant sorting
names.sort(reverse=True)

print(sorted(cars)) # temporary sorting
print(sorted(cars, reverse = True))

names.reverse()  #reverse original order

print('I am goint to ' + str(len(places)) + ' places.')
