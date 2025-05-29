a = input('Enter the statement: ')
  
########### To count number of words in the statement ##########
words = len(a.split(' '))
print ('Number of words in the statement are: %r' %words )
 
 ########### To count vowels in the statement ##########
 
print ('\n' "Below is the vowel's count in the statement" '\n')
vowels = 'aeiou'
for key in vowels:
    print ( key, '=', a.lower().count(key))