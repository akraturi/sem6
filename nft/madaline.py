def activation_function(x):
    if x >= 0:
       return 1
    else:
       return -1

w11 = 0.05
w21 = 0.2
b1 = 0.3
w12 = 0.1
w22 = 0.2
b2 = 0.15
v1 = 0.5
v2 = 0.5
b3 = 0.5
learning_rate = 0.1
patterns = []
def update_weights(i,zinp,t):
    global w11
    global w21
    global w12
    global w22
    global b1
    global b2
    if i == 1:
        w11 = w11 + learning_rate*(t-zinp)
        w21 = w21 + learning_rate*(t-zinp)
        b1 = b1 + learning_rate*(t-zinp)
    elif i==2:
        w12 = w12 + learning_rate*(t-zinp)
        w22 = w22 +learning_rate*(t-zinp)
        b2 = b2  + learning_rate*(t-zinp)
       
     
def update_weights_near_zeero(z1inp,z2inp,t):
    if abs(z1inp) > abs(z2inp):
       update_weights(1,z1inp,t)
    else:
       update_weights(2,z2inp,t)
          
def update_weights_where_pos_inp(z1inp,z2inp,t):
    if z1inp > 0:
       update_weights(1,z1inp,t)
    elif z2inp > 0:
       update_weights(2,z2inp,t)   
       
gate = int(input("Press 1 for AND\n Press 2:NAND\n Press 3:OR\n Press 4:XOR:"))
switcher = {
   1:"and_inp",
   2:"nand_inp",
   3:"or_inp",
   4:"xor_inp"
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
      iteration = iteration + 1
      print("Iteration#"+str(iteration))
      for pattern in patterns:
          x1,x2,t = pattern
          print("Pattern:"+str(pattern))
          z1inp = b1 + x1*w11 + x2*w21
          z2inp = b2 + x1*w12 + x2*w22
          z1 = activation_function(z1inp)
          z2 = activation_function(z2inp)
          
          yin = b3 + z1*v1 + z2*v2
          y = activation_function(yin)
          
          if t != y:
             if t == 1:
               update_weights_near_zeero(z1inp,z2inp,t)
             elif t == -1:
               update_weights_where_pos_inp(z1inp,z2inp,t)
          else:
             count = count +1
          print("Weights:")   
          print("w11:"+str(w11)+" w21:"+str(w21)+" w12:"+str(w12)+" w22:"+str(w22))           
      if count == len(patterns):
         break
      else:
         count = 0                

print("No. of iterations:"+str(iteration))
print("Final weights:")
print("w11:"+str(w11)+" w21:"+str(w21)+" w12:"+str(w12)+" w22:"+str(w22))                
