import numpy as np
import math

inps = [
[0.6,0.1,1,0],
[0.2,0.3,0,1]
]

w1 = [
 [0.1,-0.2,0.1],
 [0,0.2,0.2],
 [0.3,-0.4,0.5]
]

w2 = [
 [-0.4,0.1,0.6,-0.1],
 [0.2,-0.1,-0.2,0.6]
]

w1=np.array(w1)
w2=np.array(w2)

learning_rate = 0.1
#w=np.dot(w1,w2)
#print(w)

def update_weights():
    pass

def round_x(x):
    return round(x,2)

def multiply(weights,inputs):
    inputs = np.transpose(inputs)
    print("Multiplying..")
    print(weights)
    print("And")
    print(inputs)
    return np.dot(weights,inputs)

def sigmoid(x):
    return round(1/(1+math.exp(-x)),2)

def arr_sigmoid(arr):
    result = []
    for i in arr:
        result.append(sigmoid(i))
#    result = np.array(result)
#    return np.transpose(result)
    return result
              
            
flag = 0

while True:
      for inp in inps:
          inputs = inp[0:2]
          targets = inp[2:]
          print("Pattern:"+str(inp))
          print("Inputs without 1:"+str(inputs))
          print("Targets:"+str(targets))
          inputs.append(1)
          print("Inputs with 1:"+str(inputs))          
          inp1 = multiply(w1,inputs) 
          out1 = arr_sigmoid(inp1)
          out1.append(1)
          out1 = np.transpose(np.array(out1))
          inp2 = multiply(w2,out1)
          out2 = arr_sigmoid(inp2)
          print("out2:"+str(out2))
          flag = 1
      if flag != 0:
         break; 

      
      


