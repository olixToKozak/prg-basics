facebook = input('Do you have a facebook account? (True/False)')
twitter = input('Do you have a twitter account? (True/False)')
instagram = input('Do you have an instagram account? (True/False)')

count = 0
   
if facebook=='True':
    count+=1
if twitter=='True':
    count+=1
if instagram=='True':
    count+=1

if count>=2:
    print('Ur a good influencer')    
else:
    print('skill issue')
    