dict={'andhra':'telugu','tamilnadu':'tamil','banglore':'kannada','kerala':'malayalam'}
# print(dict['andhra'])
# print(dict.keys())
# print(dict.values())
print(dict.get('andhra'))
#print(dict['china'])#error

print(dict.get('china'))
####Method
dict.update({'punjab':'punjabi'})
print(dict)
dict.update({'andhra':'sanskrit'})
print(dict)
dict['andhra']='hindi'
print(dict)
#### to get all items in dictionary
print(dict.items())

####removing keys
fruits={'apple':'1kg','banana':'1/2dozen','mango':'2kg','grapes':'2kg'}
print(fruits.pop('banana'))
print(fruits)
fruits.update({'pear':'3kg'})
print(fruits)
#replace key value .but usually if we try to change key value it throws an error
fruits['plums']=fruits['apple']
del fruits['apple']
print(fruits)
fruits.popitem()##it removes last item from the dictionary
print(fruits)
fruits.setdefault('sapota')
print(fruits)


#####
x={'one','two','three','four','five'}
y={1,2,3,4,5,}
z=dict.fromkeys(x, y)
print(z)


z.clear()
print(z)

diccopy=fruits.copy()
print(diccopy)