for i in [4,6,3,5,6,7]:
    print(i)

friendsList = ['Harshada','Manisha','Sumedha','Vaishali','Deepika']
for j, f in enumerate(friendsList):
    print(j,f)
    
text = '''Make blogging beautiful with a personalized template . - and free custom domain. Powering -. Over 2 Million Websites
Worldwide. #1 In Speed and \Security. Get Started. eCommerce Plans. 1-Click WordPress Install. Money Back Guarantee.
Fully ' 'Customizable.'''
print(text)

for char in '#-.\n''\'':
    text = text.replace(char,' ')
print(text)

print(text.split(' ')[0:30])
