import random
i=0
j=0
k=0
t=0

a=map(str, random.sample(list(range(10)), k=4))
numbers=list(a)
b=map(str, numbers)
ng="".join(b)
lst1=['It starts with ' + numbers[0], 'The second digit is ' + numbers[1], 'The third digit is ' + numbers[2], 'It ends with ' + numbers[3]]

print('COWS AND BULLS')
print("here's how the game works:")
print('For every digit that you guess correctly in the correct place, you have a “cow”.') 
print('For every digit you guess correctly in the wrong place is a “bull”.')
print('REMEMBER: all the digits are different in the number, no same digit is used twice.')
print('type "exit" to exit, type "hint" if yu want a hint')

ask=list(input('guees the number '))
if ask==numbers:
        print('Yes, it was exactly ' + ng)
        print("Congratulations,you've won the game and you have spent only one try to do it ")
        

while ask != numbers:
    i=0
    j=0
    t=0
    k=k+1
    
    while len(ask)!=4:
        ask=list(input('Please, enter a 4-digit number '))
        while ask==['h', 'i', 'n', 't']:
            t=t+1
            print(random.choice(lst1))
            ask=list(input('Try it now '))   
    while ask==['h', 'i', 'n', 't']:
        t=t+1
        print(random.choice(lst1))
        ask=list(input('Try it now '))
        while len(ask)!=4:
            ask=list(input('Please, enter a 4-digit number '))    
    if ask==['e', 'x', 'i', 't']:
        print('The end(')
        break    
    if ask==numbers:
        print('Yes, it was exactly ' + ng)
        print("Congratulations,you've won the game")
        print('and you have spent '+ str(k+1) + ' tries and ' + str(t+1) + ' hints to do it')   
        break  
    if len(ask)==4:
        if ask[0]==numbers[0]:
            i=i+1
        if ask[1]==numbers[1]:
            i=i+1
        if ask[2]==numbers[2]:
            i=i+1
        if ask[3]==numbers[3]:
            i=i+1
        if ask[0] in numbers and ask[0]!=numbers[0]:
            j=j+1
        if ask[1] in numbers and ask[1]!=numbers[1]:
            j=j+1
        if ask[2] in numbers and ask[2]!=numbers[2]:
            j=j+1
        if ask[3] in numbers and ask[3]!=numbers[3]:
            j=j+1 
    k=k+1
    print(str(i) + " cow(s), " + str(j) + 'bull(s)')
    ask=list(input('guees the number again '))
    if ask==numbers:
        print('Yes, it was exactly ' + ng)
        print("Congratulations,you've won the game")
        print('and you have spent '+ str(k+1) + ' tries and ' + str(t+1) + ' hint(s) to do it')   
        break
