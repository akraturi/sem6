from random import shuffle
patterns = []
with open("three_inp_or","r") as inp:
     for line in inp:
         patterns.append(list(map(int,line.split())))

shuffle(patterns)
#patterns=patterns[::-1]         
#print(patterns)
data_train = patterns[0:6]
data_test = patterns[6:]
#print(data_train)
#print(data_test)
def class_prob(p_or_n):
    fav_outcomes = 0
    all_outcomes = len(data_train)
    for sample in data_train:
        x1,x2,x3,t = sample
        #print(x1,x2,x3,t)
        if p_or_n:
           if t == 1:
              fav_outcomes += 1
        else:
           if t == 0:
              fav_outcomes += 1
                    
    return fav_outcomes/all_outcomes    

def attr_prob(p_or_n,a,b,c):
    y_count = 0 
    n_count = 0
    x1_fav_out = 0
    x2_fav_out = 0
    x3_fav_out = 0
    
    for sample in data_train:
        x1,x2,x3,t = sample
        if t == 1:
           y_count += 1
           if p_or_n:
              if a == x1:
                 x1_fav_out += 1
              if b == x2:
                 x2_fav_out += 1
              if c == x3:
                 x3_fav_out += 1      
              
        else:
           n_count += 1
           if not (p_or_n):
              if a == x1:
                 x1_fav_out += 1
              if b == x2:
                 x2_fav_out += 1
              if c == x3:
                 x3_fav_out += 1             
    if p_or_n:
       all_out = y_count
    else:
       all_out = n_count
    
    return (x1_fav_out/all_out)*(x2_fav_out/all_out)*(x3_fav_out/all_out)          
           

def predict():
             
    y_prob = class_prob(True)
    n_prob = class_prob(False)
    #print(y_prob,n_prob)
    for i in range(len(data_test)):
        a,b,c,t=data_test[0]
        pos_class_prob=y_prob*attr_prob(True,a,b,c)
        neg_class_prob=n_prob*attr_prob(False,a,b,c)
    
        print("Probability for class(1):"+str(pos_class_prob))
        print("Probability for class(0):"+str(neg_class_prob))

        print("So..for the input sample")
        print("Orignal class:"+str(t))
        if pos_class_prob > neg_class_prob:
           print("Predicted class:1")
        else:
           print("Predicted class:0")   

         
y_prob = class_prob(True)
n_prob = class_prob(False)
#print(y_prob,n_prob)

#a,b,c,t=data_test[0]
a,b,c = list(map(int,input().split()))
#print(a,b,c)

pos_class_prob=y_prob*attr_prob(True,a,b,c)
neg_class_prob=n_prob*attr_prob(False,a,b,c)
    
print("Probability for class(1):"+str(pos_class_prob))
print("Probability for class(0):"+str(neg_class_prob))

print("So..for the input sample")
#print("Orignal class:"+str(t))
if pos_class_prob > neg_class_prob:
   print("Predicted class:1")
else:
   print("Predicted class:0")   

       
           
