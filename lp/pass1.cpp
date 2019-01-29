#include <bits/stdc++.h>
#include <stdio.h>
using namespace std;
void print(char symbol[],char opcode[],char operand[]){
    printf("\t%s\t%s\t%s\n",symbol,opcode,operand);
}
void scan(FILE *fp,char symbol[],char opcode[],char operand[]){
   fscanf(fp,"%s %s %s",symbol,opcode,operand);
}
int main(){
    FILE *input,*output,*s_table;
    char symbol[20],opcode[20],operand[20];
    int start_addr,location_counter;
    
    input=fopen("input.txt","r");
    s_table = fopen("symtab.txt","w");
    
    fscanf(input,"%s %s %d",symbol,opcode,&start_addr);
    
    if(strcmp(opcode,"START")==0)
   {
      location_counter=start_addr;
      printf("\t%s\t%s\t%d\n",symbol,opcode,start_addr);
   }
   else{
     location_counter=0;
   }
   
//   fscanf(input,"%s %s %s",symbol,opcode,operand);
   scan(input,symbol,opcode,operand);
//     print(symbol,opcode,operand);

   while(!feof(input))
  {
     
//     print(symbol,opcode,operand);
     cout << location_counter<<" ";
     print(symbol,opcode,operand);
     
      if(strcmp(symbol,"-")!=0)
     {
       fprintf(s_table,"\n%d\t%s\n",location_counter,symbol);
     }
     
     FILE *optab;
     char temp_opcode[20];
     optab = fopen("optab.txt","r");
     while(!feof(optab)){
      fscanf(optab,"%s",temp_opcode);
      if(strcmp(opcode,temp_opcode)==0){
        location_counter += 3;
        break;
      }
     }
     fclose(optab);
     
    if(strcmp(opcode,"WORD")==0)
    {
        location_counter += 3;
    }
    else if(strcmp(opcode,"RESW")==0)
    {
        int no_of_resw=atoi(operand);
        location_counter=location_counter+(3*no_of_resw);
    }
    else if(strcmp(opcode,"BYTE")==0)
      {
           if(opcode[0]=='X')
             location_counter=location_counter+1;
           else
           {
             int len=strlen(operand)-2;
             location_counter=location_counter+len;
           }
    }
    else if(strcmp(opcode,"RESB")==0)
    {
        int no_of_resb=atoi(operand);
        location_counter=location_counter+no_of_resb;
    }
    scan(input,symbol,opcode,operand);
      
   }
   
   if(strcmp(opcode,"END")==0)
    {
       printf("Length of program =%d",location_counter-start_addr);
    }
   
    fclose(input);
    fclose(s_table);  
       
   
}
