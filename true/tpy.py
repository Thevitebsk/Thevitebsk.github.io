import sys
try:code=open(sys.argv[1]).read()
except:print(f"Usage: py {__file__.split(chr(0x5c))[-1]} \"(file name)\"");exit()
targ="";c="";sub=tp=p=0;ts=[];s=[];ld=[]
print("true")
while 1:
 try:
  if code[p]=='"':
   while code[p+1]!='"':p+=1;ts.append(code[p])
   s.append("".join(ts));ts.clear();p+=1
  elif code[p]=='.':print(s.pop(),end="")
  elif code[p]in list(map(str,range(10))):s.append(int(code[p]))
  elif code[p]==',':c=input()
  elif code[p]==':':s.append(s[-1])
  elif code[p]=="'":s.append(c[0]);c=c[1:]
  elif code[p]=='»':
   targ=code[p+1];tp=p;sub=1
   while 1:
    if code[p]==targ and code[p+1]==":":p+=1;break
    if len(code)-2==p:p=0
    p+=1
  elif code[p]==";"and sub==1:p=tp
  elif code[p]=="\n":break
  elif code[p]=="-":s.pop()
  elif code[p]=="+":s.append(int(s.pop())+int(s.pop()))
  elif code[p]=="`":s.append(int(s.pop())*-1)
  elif code[p]=="(":
   while code[p+1]!=")":ts.append(code[p+1]);p+=1
   ld.append("".join(ts))
  elif code[p]=="[":
   while code[p]!="]":p+=1
  if len(code)-1==p:
   while 1:
    if code[p]=="\n":break
    elif p==0:p=-1
  p+=1
 except IndexError:break
