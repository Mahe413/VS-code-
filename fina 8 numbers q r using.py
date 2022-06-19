from itertools import permutations
from itertools import combinations
import math

perm = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)


for i in list(perm):
   

    
        # print (i)
        iList = list(i)
        
        A, B, C, D, E, F, q, r, y = [iList[j] for j in (0,1,2,3,4,5,6,7,8)]
            
        
        x = ((q*y)+r)
        
        S1 = (((A*y)/(B*x))+((C*y)/(D*x)))-((E*y)/(F*x)) 
        S2 = (((A*y)/(B*x))*((C*y)/(D*x)))/((E*y)/(F*x)) 
        S3 = ((A*y)/(B*x))+(((C*y)/(D*x))/((E*y)/(F*x)))  
        S4 = ((A*y)/(B*x))-(((C*y)/(D*x))/((E*y)/(F*x)))  
        S5 = ((A*y)/(B*x))+(((C*y)/(D*x))*((E*y)/(F*x)))   
        S6 = ((A*y)/(B*x))-(((C*y)/(D*x))*((E*y)/(F*x)))
        S7 = (((A*y)/(B*x))+((C*y)/(D*x)))+((E*y)/(F*x))
        S8 = (((A*y)/(B*x))-((C*y)/(D*x)))-((E*y)/(F*x))
        S9 = (((A*y)/(B*x))*((C*y)/(D*x)))*((E*y)/(F*x))
        S10 = (((A*y)/(B*x))/((C*y)/(D*x)))/((E*y)/(F*x))   
        # print(S1 + S2 + S3 + S4 + S5 + S6)
        q = x//y
        r = x%y
        
        
        if(S1 == 1 and x>y and r!= A and r!= B and r!= C  and r!= D and r!= E and r!= F and q!= A and q!= B and q!= C  and q!= D and q!= E and q!= F and q!= y and y!= 1 and r!= 0 and r!= q and r!= y):
            print("The variables are from S1 : " +  str(A) + " " + str(B)+ " " +str(C)+ " " +str(D)+ " " +str(E)+ " " +str(F)+ " " +str(x)+ " " +str(y))
        if(S2 == 1 and x>y and r!= A and r!= B and r!= C  and r!= D and r!= E and r!= F and q!= A and q!= B and q!= C  and q!= D and q!= E and q!= F and q!= y and y!= 1 and r!= 0 and r!= q and r!= y):
            print("The variables are from S2 : " +  str(A) + " " + str(B)+ " " +str(C)+ " " +str(D)+ " " +str(E)+ " " +str(F)+ " " +str(x)+ " " +str(y))
        if(S3 == 1 and x>y and r!= A and r!= B and r!= C  and r!= D and r!= E and r!= F and q!= A and q!= B and q!= C  and q!= D and q!= E and q!= F and q!= y and y!= 1 and r!= 0 and r!= q and r!= y):
            print("The variables are from S3 : " +  str(A) + " " + str(B)+ " " +str(C)+ " " +str(D)+ " " +str(E)+ " " +str(F)+ " " +str(x)+ " " +str(y))
        if(S4 == 1 and x>y and r!= A and r!= B and r!= C  and r!= D and r!= E and r!= F and q!= A and q!= B and q!= C  and q!= D and q!= E and q!= F and q!= y and y!= 1 and r!= 0 and r!= q and r!= y):
            print("The variables are from S4 : " +  str(A) + " " + str(B)+ " " +str(C)+ " " +str(D)+ " " +str(E)+ " " +str(F)+ " " +str(x)+ " " +str(y))
        if(S5 == 1 and x>y and r!= A and r!= B and r!= C  and r!= D and r!= E and r!= F and q!= A and q!= B and q!= C  and q!= D and q!= E and q!= F and q!= y and y!= 1 and r!= 0 and r!= q and r!= y):
            print("The variables are from S5 : " +  str(A) + " " + str(B)+ " " +str(C)+ " " +str(D)+ " " +str(E)+ " " +str(F)+ " " +str(x)+ " " +str(y))
        if(S6 == 1 and x>y and r!= A and r!= B and r!= C  and r!= D and r!= E and r!= F and q!= A and q!= B and q!= C  and q!= D and q!= E and q!= F and q!= y and y!= 1 and r!= 0 and r!= q and r!= y):
            print("The variables are from S6 : " +  str(A) + " " + str(B)+ " " +str(C)+ " " +str(D)+ " " +str(E)+ " " +str(F)+ " " +str(x)+ " " +str(y))
        if(S7 == 1 and x>y and r!= A and r!= B and r!= C  and r!= D and r!= E and r!= F and q!= A and q!= B and q!= C  and q!= D and q!= E and q!= F and q!= y and y!= 1 and r!= 0 and r!= q and r!= y):
            print("The variables are from S7 : " +  str(A) + " " + str(B)+ " " +str(C)+ " " +str(D)+ " " +str(E)+ " " +str(F)+ " " +str(x)+ " " +str(y))
        if(S8 == 1 and x>y and r!= A and r!= B and r!= C  and r!= D and r!= E and r!= F and q!= A and q!= B and q!= C  and q!= D and q!= E and q!= F and q!= y and y!= 1 and r!= 0 and r!= q and r!= y):
            print("The variables are from S8 : " +  str(A) + " " + str(B)+ " " +str(C)+ " " +str(D)+ " " +str(E)+ " " +str(F)+ " " +str(x)+ " " +str(y))
        if(S9 == 1 and x>y and r!= A and r!= B and r!= C  and r!= D and r!= E and r!= F and q!= A and q!= B and q!= C  and q!= D and q!= E and q!= F and q!= y and y!= 1 and r!= 0 and r!= q and r!= y):
            print("The variables are from S9 : " +  str(A) + " " + str(B)+ " " +str(C)+ " " +str(D)+ " " +str(E)+ " " +str(F)+ " " +str(x)+ " " +str(y))
        if(S10 == 1 and x>y and r!= A and r!= B and r!= C  and r!= D and r!= E and r!= F and q!= A and q!= B and q!= C  and q!= D and q!= E and q!= F and q!= y and y!= 1 and r!= 0 and r!= q and r!= y):
            print("The variables are from S10 : " +  str(A) + " " + str(B)+ " " +str(C)+ " " +str(D)+ " " +str(E)+ " " +str(F)+ " " +str(x)+ " " +str(y))
            
      
      
      # Python program to find the
# quotient and remainder
        # def find(x, y):
      
        #      # for quotient
                
        #         print("Quotient: ", q)
      
        #             # for remainder
                
        #         print("Remainder", r)
      
# Driver Code
# find(10, 3)
# find(99, 5)        
    
        
        # function to check the conditions
     
    #  for j in list(i):
    #         comb = combinations(i[j], 2)
    #     print (comb)
#     iList.multiply_value()
#     print(C)

# def multiply_values(A,B):

#     C = A * B 

# def check(A, B, C, D, E, F, x, y):
      
     
    #   S1 = [((A*y)/(B*x))+((C*y)/(D*x))]-[(E*y)/(F*x)] 
    #   if( S1 == 1 ):
    
      


#if value == 70:
#        print(' value ')
# third commit
