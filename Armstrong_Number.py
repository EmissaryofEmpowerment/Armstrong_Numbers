from itertools import cycle
import pdb


def arm_num(numberlist):
    sum = 0
    for i in range(len(numberlist)):
        try:
            print(f"{numberlist[i]} to the power of {len(numberlist)} equals {int(numberlist[i])**len(numberlist)}")
        except:
            print("\nInvalid literal but proceed anyway\n")#pdb.set_trace()
        sum += (int(numberlist[i]))**len(numberlist)
    print(f"Total: {sum}")
    return sum


def main(number):
    numberlist = list(number)
    if arm_num(numberlist) == int(number):
        print(f'{number} is an Armstrong number! :)')        
    else:
        print(f'{number} is not an Armstrong number :(')    
        rangge = 1
        what_next = input(f"\nIf you would like to find the closest integer to {number} type 'find', otherwise enter the next number to calculate\n> ")
        if what_next.isdigit() == False:
            while True:
                a_bit_hire = int(number) + rangge
                find_next = arm_num(list(str(a_bit_hire)))
                if find_next == a_bit_hire:
                    print(f'{a_bit_hire} is an Armstrong number! :)')
                    break
                a_bit_lower = int(number) - rangge
                find_next = arm_num(list(str(a_bit_lower)))
                if find_next == a_bit_lower:
                    print(f'{a_bit_lower} is an Armstrong number! :)')                
                    break
                rangge += 1
        else:
            return what_next
    return input("\nEnter another number to test or press 'q' to quit:\n> ")


### Lab 8b Exam 1 prep###
#Magenta 31#
print( ''' an Armstrong number occurs when each digit to the power of the  
number of its digits added up is the number
Example: 153 
1**3 + 5**3 + 3**3 = 153''')
number = input("\nEnter a number:\n> ")



while number.isdigit() == False: #1st time around it has to be a number
    number = input("\nThat was not a valid number, please choose a different number:\n> ")

while number.isdigit(): #now the user can quit if they want
    number = main(number)
print("Thanks for playing, see you next time!")
