import random
n=2
combinations = [("00","0"),("01","1"),("10","1"),("11","1")]
#random_weights = [2,3,1,4]
flag = 0
choosen_weights = (None,None)
while True:
     count = 0 
     for (inp,out) in combinations:
       temp = [1,-1]
       w1 = random.choice(temp)*random.choice(range(1,5))
       w2 = random.choice(temp)*random.choice(range(1,5))
       choosen_weights = (w1,w2)
       print(choosen_weights)
       yin = int(inp[0])*w1+int(inp[1])*w2
       arr = [w1,w2]
       neg_count = len(list(filter(lambda x: (x < 0), arr))) 
       pos_count = len(list(filter(lambda x: (x >= 0), arr)))
       theta = 2*pos_count-neg_count
       print("theta:")
       print(theta)
       if yin >= theta:
          result = "1"
       else:
          result = "0"
       if result == out:
          count += 1       
     
     if count == len(combinations):
        flag = 1
        break;   

if flag == 1:
   print("Weights:")
   print(choosen_weights)
else:
   print("Not possible with the given weights")   
#print(weights)

  
