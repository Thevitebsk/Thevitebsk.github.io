"in progress"
import sys
try:code=open(sys.argv[1]).read()
except:print(f"Usage: python {__file__.split(chr(0x5c))[-1]} \"(file name)\"");exit()
p=0;ts=[];s=[]
while 1:
  if code[p] == '"' :
    p+=1;s.append(code[p : code.index('"', p)])
    p=code.index('"', p)
  elif code[p] == "." : print(s.pop())
  elif code[p] == "," : s.append(input())
  if code[p] == "\n" : break
  p+=1
