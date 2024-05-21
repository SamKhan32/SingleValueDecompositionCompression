import random
import Cigar
def main():
    




    is_weekend = bool(input("Is it the weekend? "))
    num_of_cigars = int(input("How many cigars? "))
    cigars = []
    for i in num_of_cigars:
        rand_num = int(random() * 100 +1)
        if(rand_num <= 40):
             cigars.add(Cigar("Good"))
        else:   
            cigars.add(Cigar("Bad"))
    if is_weekend == False:
        
        if cigars >= 40 and cigars <= 60:
            print("Let's this started!")
    elif cigars >= 40:
            print("everyone and they mama up in here")
def countCigarQuality(cigars):
     return 

main()

