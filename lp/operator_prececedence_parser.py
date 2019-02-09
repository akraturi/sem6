import re
  
          
class Matrix(dict):
      
      def __init__(self,rows,columns):
          self.rows = rows
          self.cols = columns
          for row in rows:
              self[row]={}
              for col in columns:
                  self[row][col]=None
     
      def initialise_with(self,value):
          for row in self.rows:
              for col in self.cols:
                  self[row][col]=value
                               
                  
          
class Productions:
      
      TERMINAL_STRING=0
      NT_TERMINAL_STRING=1
      STRING_TERMINAL=2
      STRING_TERMINAL_NT=3
      
      def __init__(self,terminals,start_symbol):
         self.start_symbol = start_symbol
         self.productions = {}
         self.terminals = terminals
      
      def print_productions(self):
          for key,value in self.productions.items():
              print(key+"-->",end="")
              for rhs in value:
                  print(rhs+"|",end="")   
              print()
      
      def add(self,key,value):
           if key not in self.productions.keys():
              self.productions[key]=[value]
           else:
              self.productions[key].append(value)
      
      def get_terminals(self):
           return self.terminals
      
      def get_non_terminals(self):
          return list(self.productions.keys())
          
      def split_rhs(self,rhs):
          result = []
          val = ""
          for symbol in rhs:
              val = val + symbol
              if val in self.get_terminals():
                 result.append(val)
                 val = ""
              elif val in self.get_non_terminals():
                 result.append(val)
                 val = ""   
          return result
      
      def separate_terminal_and_non_terminals(self,item_list):
          terminals = []
          non_terminals = []
          for item in item_list:
              if item in self.get_terminals():
                  terminals.append(item)
              else:
                  non_terminals.append(item)
                  
          return terminals,non_terminals
                      
      def get_terminals_at_same_level_of(self,terminal):
          result = []
#          print("Searching same level terminal for",terminal)
          for key,value in self.productions.items():
              for rhs in value:
                  splited_rhs = self.split_rhs(rhs)
                  terminals,non_terminals = self.separate_terminal_and_non_terminals(splited_rhs)
#                  print("Terminals in rhs ",rhs,terminals)
                  if terminal in terminals :
                     for item in terminals:
#                         print("Comparing ",terminal,item)
                         if splited_rhs.index(item) == splited_rhs.index(terminal)+2:
#                            print("They are diff appending to list")
                            result.append(item)
                         else:
                            pass
#                            print("They are same not appending")   
          return result           
                                
      def get_productions_matching(self,pattern,is_leading):
          result = {}
          pairs = []
          if is_leading:
             func = self.matches_pattern_lead
          else: 
             func = self.matches_pattern_trail
                
          for key,value in self.productions.items():
              for rhs in value:
                  is_matched,terminal = func(rhs,pattern)
#                  print("For pattern",pattern)
#                  print(key,rhs)
#                  print("matched... with:",terminal)
                  if is_matched:
                     if key in result.keys():
                        result[key].append(rhs)
                     else:
                        result[key]=[rhs]
                     pairs.append((key,terminal))      
                     
          return result,pairs       
      
      def get_nt_at_left_of(self,terminal):
          result = []
          for key,value in self.productions.items():
              for rhs in value:
                  splited_rhs = self.split_rhs(rhs)
                  terminals,non_terminals = self.separate_terminal_and_non_terminals(splited_rhs)
                  if terminal in splited_rhs:
                     left_index = splited_rhs.index(terminal)-1
                     
                     if left_index<len(splited_rhs):
                        left_item = splited_rhs[left_index]
                        if left_item in non_terminals:
                           result.append(left_item)
          return result
      
      
      def get_nt_at_right_of(self,terminal):
          result = []
          for key,value in self.productions.items():
              for rhs in value:
                  splited_rhs = self.split_rhs(rhs)
                  terminals,non_terminals = self.separate_terminal_and_non_terminals(splited_rhs)
                  if terminal in splited_rhs:
                     right_index = splited_rhs.index(terminal)+1
                     if right_index<len(splited_rhs):
                        right_item = splited_rhs[right_index]
                        if right_item in non_terminals:
                           result.append(right_item)
          return result
      
                     
      def get_lhs_with_nt(self,non_terminal,is_first_nt):
          result = []
          non_terminal_index = None
          if is_first_nt:
             non_terminal_index=0    
             
          for key,value in self.productions.items():
              for rhs in value:
                  if not is_first_nt:
                     non_terminal_index = len(rhs)-1
                  if rhs.find(non_terminal) == non_terminal_index:
#                     print("such production is..")
#                     print(key,value)
                     result.append(key) 
          return list(set(result))            
      
      def matches_pattern_lead(self,rhs,pattern):
          terminal_list = self.get_terminals()
          non_terminal_list = self.get_non_terminals()
                
            
             
          return_terminal = None
          
          for terminal in terminal_list:
              if rhs.find(terminal) == 0:
                 if pattern == self.TERMINAL_STRING:
                    return_terminal = terminal
                    return True,return_terminal
                                      
              for non_terminal in non_terminal_list:
                  if rhs.find(non_terminal) == 0 and rhs.find(terminal) == 1:   
                     if pattern == self.NT_TERMINAL_STRING:
                        return_terminal = terminal
                        return True,return_terminal
                           
          
          return False,return_terminal
          
      def matches_pattern_trail(self,rhs,pattern):
          terminal_list = self.get_terminals()
          non_terminal_list = self.get_non_terminals()                
            
          splited_rhs = self.split_rhs(rhs)
             
          return_terminal = None
          
          for terminal in terminal_list:
              try:
                 if splited_rhs.index(terminal) == len(splited_rhs)-1:
                   if pattern == self.STRING_TERMINAL:
                      return_terminal = terminal
                      return True,return_terminal
              except:
                  pass
                        
              for non_terminal in non_terminal_list:
                  try:
                      if splited_rhs.index(non_terminal) == len(splited_rhs)-1 and splited_rhs.index(terminal) == len(splited_rhs)-2:   
                         if pattern == self.STRING_TERMINAL_NT:
                            return_terminal = terminal
                            return True,return_terminal
                  except:
                      pass         
          
          return False,return_terminal
      
      def reduce_rhs(self,rhs_nt_list):
          for key,value in self.productions:
              for rhs in value:
                  if self.split_rhs() == rhs_nt_list:
                     return key 
          
          return None
             
      def __str__(self):
          return self.productions
                      
                         
                 
class Leading_Or_Trailing_Algorithm:

      def __init__(self,productions,is_leading):
          self.productions = productions
          self.is_leading = is_leading
          self.stack = []
          self.matrix = Matrix(self.productions.get_non_terminals(),self.productions.get_terminals())
          self.matrix.initialise_with(False)
#          print("Initially..")
#          print(self.matrix)                 
      
      def get_matrix(self):
           
           
           if self.is_leading:
              pattern1 = Productions.TERMINAL_STRING
              pattern2 = Productions.NT_TERMINAL_STRING
           else:
              pattern1 = Productions.STRING_TERMINAL
              pattern2 = Productions.STRING_TERMINAL_NT
                 
           a,pairs1 = self.productions.get_productions_matching(pattern1,self.is_leading)
           b,pairs2 = self.productions.get_productions_matching(pattern2,self.is_leading)
           a.update(b)
           all_pairs = pairs1+pairs2
#           print(all_pairs)
           for pair in all_pairs:
               self.install(pair)
           
           while len(self.stack)>0:
#                 print(self.stack)
                 B,a = self.stack.pop()
#                 print("Searching for "+B+" as the first non terminal in the productions")

                 non_terminal_list=self.productions.get_lhs_with_nt(B,self.is_leading)
              
#                 print("Non terminals")
#                 print(non_terminal_list)
                 for non_terminal in non_terminal_list:
#                     print("going to install")
#                     print(non_terminal,a)
                     self.install((non_terminal,a))
                 
           return self.matrix         
              
      def install(self,pair):
           A,a = pair
          
           if not self.matrix[A][a]:
#               print("The matrix while installing")
#               print(pair)
#               print(self.matrix)
               self.matrix[A][a]=True
               self.stack.append(pair)    
      
          
class Operator_Precedence_Table:
      
      GREATER = 2
      LESS = 1
      EQUAL = 0
      NOT_DEFINED = -1
      
      def __init__(self,productions,leading_matrix,trailing_matrix):
          self.terminals = productions.get_terminals()
          self.terminals_including_doller =self.terminals + ["$"]
          self.table = Matrix(self.terminals_including_doller,self.terminals_including_doller)
          self.table.initialise_with(Operator_Precedence_Table.NOT_DEFINED)
          self.productions = productions
          self.leading_matrix = leading_matrix
          self.trailing_matrix = trailing_matrix
      
      def get_table(self):
    
          for terminal in self.terminals:
              
              same_level_terminals=self.productions.get_terminals_at_same_level_of(terminal)
              
#              print("Terminals at the same level of:",terminal,same_level_terminals)
              
              for item in same_level_terminals:
                  self.table[terminal][item] = self.EQUAL
              
              left_non_terminals=self.productions.get_nt_at_left_of(terminal)
              
              
              for left_non_terminal in left_non_terminals:
                  for key,value in self.trailing_matrix[left_non_terminal].items():
                      if value:
                         self.table[key][terminal] = self.GREATER
              
              right_non_terminals=self.productions.get_nt_at_right_of(terminal)
              
              for right_non_terminal in right_non_terminals:
                  for key,value in self.leading_matrix[right_non_terminal].items():
                      if value:
                         self.table[terminal][key] = self.LESS
          
          
          lead_set = self.get_lead_for_nt(self.productions.start_symbol)
#          print("Lead set for",self.productions.start_symbol)
#          print(lead_set)
          for item in lead_set:
              self.table["$"][item] = self.LESS
          
          trail_set = self.get_trail_for_nt(self.productions.start_symbol)
#          print("Trail set for",self.productions.start_symbol)
#          print(trail_set)   
          for item in trail_set:
              self.table[item]["$"] = self.GREATER
                      
          return self.table
          
      def print_table(self):
          print(" ",end="")
          for key,value in self.table[self.terminals[0]].items():
              print(key+" ",end="")
           
          print()
           
          for key,value in self.table.items():
              print(key+" ",end="")
              for col,precedence in value.items():
                 if precedence == Operator_Precedence_Table.GREATER:
                     print("> ",end="")
                 elif precedence == Operator_Precedence_Table.LESS:
                     print("< ",end="")
                 elif precedence == Operator_Precedence_Table.EQUAL:
                     print("= ",end="")
                 else:
                     print("e ",end="")                
              print()    
                  
      def get_lead_for_nt(self,nt):
          result = []
          lead_set = self.leading_matrix[nt]
          for key,val in lead_set.items():
              if val:
                 result.append(key)
          
          return result        
      
      def get_trail_for_nt(self,nt):
          result = []
          trailing_set = self.trailing_matrix[nt]
          for key,val in trailing_set.items():
              if val:
                 result.append(key)
          
          return result        
              
          
          
          
              
                            
                                             
def main():

    n=int(input("Enter the number of grammer rules:"))
    
    terminals = input("Enter the terminals of the grammer separeted by space:").split()
    
    start_symbol=input("Enter the starting symbol of the grammer:")
    
    productions = Productions(terminals=terminals,start_symbol=start_symbol)
    
    print("Enter the productions for grammer")
    for i in range(n):
        lhs = input("LHS:")
        rhs = input("RHS:")
        productions.add(lhs,rhs)
    
    inp=input("Enter the string to be parsed with this grammer")
    
    print("\nEntered productions are--->")
    productions.print_productions()
    
    leading = Leading_Or_Trailing_Algorithm(productions=productions,is_leading=True)
    leading_matrix=leading.get_matrix()
#    print("Leading matrix")
#    print(leading_matrix)
#    
#    print("Trailing matrix")
    trailing = Leading_Or_Trailing_Algorithm(productions=productions,is_leading=False)
    trailing_matrix = trailing.get_matrix()
#    print(trailing_matrix)
    
    table = Operator_Precedence_Table(productions,leading_matrix,trailing_matrix)
    opp_table=table.get_table()
    print("Operator precedence table---->")
    table.print_table()
    
    opp = Operator_Precedence_Parser(productions,opp_table)
    print("Parsing string:",inp)
    if opp.parse(inp):
       print("String is syntactically correct")
    else:
       print("Syntax error in string")   


class Operator_Precedence_Parser:
      
      def __init__(self,productions,table):
          self.productions = productions 
          self.table = table
          self.stack = []
          self.stack.append("$")
      
      def parse(self,inp):
      
          inp = self.productions.split_rhs(inp)
          
#          print("Input after splitting into terminals")
          
#          print(inp)
          
          inp = inp + ["$"]
#          print(inp)
          i = 0
          while True:
                print("stack:",self.stack)
                print("input:",inp[i:])
                
                if self.stack[-1] == "$" and inp[i] == "$":
                   return True
                else:
                   a = self.stack[-1]
                   b = inp[i]
                
                   print("stack_top:",a)
                   print("input_symbol:",b)
        
                   if self.table[a][b] == Operator_Precedence_Table.LESS or self.table[a][b] == Operator_Precedence_Table.EQUAL:
                      self.stack.append(b)
                      i = i+1
                   elif self.table[a][b] == Operator_Precedence_Table.GREATER:
                      rhs=[]
                      while True:
                            recent = self.stack.pop()
                            top = self.stack[-1]
                            rhs=[recent]+rhs
                            
                            if self.table[top][recent] == Operator_Precedence_Table.LESS:
                               break  
                      
                      #self.productions.reduce_rhs(rhs)
                      print("Reducing handle")
                      print(rhs)
                   else:
                      return False   
                    

main()    
