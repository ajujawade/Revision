import re
str = "This is a normal\nstring" # \n for new line
print(str)

str = r"This is a raw\nstring"   # \n will not work
print(str)

str = "cat mat sat bat rat"

q1 = re.search(r"m\w",str)
print(q1.group())

q2 = re.search(r"m\w\w",str)
print(q1.group())

q3 = re.findall(r"m\w\w",str)
print(q3)


str2 = "map sun mop run"

q4 = re.match(r'm\w\w',str2)
print(q4.group())


str3 = "This is the code : 'Core' Python\'s book"
q5 = re.split(r"\W+",str3)
print(q5)


str4 = "Program will be conducted in Nagpur in India"

q6 = re.sub(r'Nagpur','Pune',str4)
print(q6)


st1 = "an apple a day keeps the doctor away"

out1 = re.findall(r'a\w+',st1)
print(out1)

for word in out1:
    print(word)

out2 = re.findall(r'\ba\w*\b',st1)
print(out2)

for word in out2:
    print(word)

# retriving Numbers from the string

st2 = "The meeting will be conducted on 1st and 21st of every month"

out3 = re.findall(r'\d\w*',st2)
print(out3)

for num in out3:
    print(num)

st3  = "one two three four five six seven"

out4 = re.findall(r'\b\w{5}\b',st3)
print(out4)

out4 = re.search(r'\b\w{5}\b',st3)
print(out4.group())

out5 = re.findall(r'\b\w{4,}\b',st3)
print(out5)

out6 = re.findall(r'\b\w{3,5}\b',st3)
print(out6)

st4  = "one two three four five six seven 8 9 10"

out7 = re.findall(r'\b\d\b',st4)
print(out7)

st5 = "one two three four five six seven"

out8 = re.findall(r's\w*\Z',st5)
out9 = re.findall(r'\Ao\w*',st5)

print(out8)
print(out9)



str5 = "Ajay Jawade : 7972235361"

res1 = re.search(r'\d+',str5)
print(res1.group())

res2 = re.search(r'\w+',str5)
print(res2.group())

res3 = re.search(r'\D+',str5)
print(res3.group())

str6 = "anil aman anand ajay arun arti abhijit ankur"
res4 = re.findall(r'\ba[nk]\w*\b',str6)
print(res4)

str7 = 'vijay 20 1-5-2001,rohit 21 22-10-1990,sita 22 15-09-2000'

res5 = re.findall(r'\d{2}-\d{2}-\d{4}',str7)
print(res5)

res6 = re.findall(r'\d+-\d+-\d+',str7)
print(res6)

res7 = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str7)
print(res7)


















