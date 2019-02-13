import math
import time
def activation_function(x):
    if x >= 0:
       return 1
    else:
       return 0

def sigmoidal_activation_function(x):
    return 1/(1+math.exp(-x))       

w1 = -0.1
w2 = 0.1
bias = 0.3
learning_rate = 0.1
patterns = []
gate = int(input("Press 1 for AND\n Press 2:NAND\n Press 3:OR:"))
switcher = {
   1:"and_inp",
   2:"nand_inp",
   3:"or_inp"
}
inp_file = switcher.get(gate,-1)
if inp_file == -1:
   print("Invalid Choice.. Existing")
   exit()
      
with open(inp_file,"r") as inp:
     for line in inp:
         x1,x2,t = list(map(int,line.split()))
         patterns.append((x1,x2,t))
count=0
iteration = 0
while True:
     iteration = iteration+1
     print("FOR ITERATION#"+str(iteration))
     for pattern in patterns:
         a,b,t = pattern
         yin = round(a*w1+b*w2+bias,2)
         yout = activation_function(yin)
#         yout = sigmoidal_activation_function(yin)
         error = (t - yout)
         if error != 0:
            w1 = (w1 + round(learning_rate*error*a,2))
            w2 = (w2 + round(learning_rate*error*b,2))
            bias = (bias + round(learning_rate*error,2)) 
         else:
            count = count+1
            
         print("Pattern "+str(pattern))
         print("Yinp:"+str(yin))      
         print("w1:"+str(w1)+" w2:"+str(w2)+" b:"+str(bias))
         time.sleep(2)
           
     if count == len(patterns):
        break
     else:
        count = 0      
print("Final weights are")
print("w1:"+str(w1)+" w2:"+str(w2)+" b:"+str(bias))             
         
