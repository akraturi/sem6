from time import sleep

# (x1,x2,b):t
logic_gate = {
  (1,1,1):1,
  (1,-1,1):1,
  (-1,1,1):1,
  (-1,-1,1):-1
}
print(logic_gate.items())
learning_rate = 0.1
tolerance_err = 1.4
w1 = 0.1
w2 = 0.1
bias_weight = 0.1
print("Initially:(w1 w2 b):(",w1,w2,bias_weight,")")

iteration = 0

cal_err = 1000

while  (cal_err > tolerance_err):
      
      cal_err = 0
      
      
      iteration = iteration + 1
      
      print("For iteration #",iteration)
      
      for data in logic_gate.items():
          x1,x2,b = data[0]
          print(x1,x2,b)
          t = data[1]
          print(t)
          yin = bias_weight + x1*w1 + x2*w2
          print("From last")
          print("w1:",w1," w2:",w2," bias_weight:",bias_weight,"error:",cal_err)
          w1 = w1 + x1*(t-yin)*learning_rate
          w2 = w2 + x2*(t-yin)*learning_rate
          bias_weight = bias_weight + learning_rate*(t-yin)
          cal_err = cal_err + (t-yin)*(t-yin)
          print("For input/output",data)
          print("w1:",w1," w2:",w2," bias_weight:",bias_weight,"error:",cal_err)
          #sleep(5)
          
      print("Total calculated error:",cal_err)    

print("Finally...")          
print("No. of iteration:",iteration)
print("w1:",w1," w2:",w2," bias_weight:",bias_weight)          
          


