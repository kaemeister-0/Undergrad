'''n=input('')
count=0
for i in n:
    if i=='0'or i=='1':
        count+=1
if count==len(n):
    print('Binary number')
else:
    print('Not a binary number')'''

test_str = input('')

# using naive method to get count 
# of each element in string 
all_freq = {} 

for i in test_str: 
	if i in all_freq: 
		all_freq[i] += 1
	else: 
		all_freq[i] = 1

# printing result 
print ("Count of all characters in GeeksforGeeks is :\n "
										+ str(all_freq)) 