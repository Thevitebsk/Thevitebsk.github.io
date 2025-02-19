i=''''''
targ="";c="";sub=tp=p=0;ts=[];s=[];ld=[]
print("true")
while 1:
 try:
  if i[p]=='"':
   while i[p+1]!='"':p+=1;ts.append(i[p])
   s.append("".join(ts));ts.clear();p+=1
  elif i[p]=='.':print(s.pop(),end="")
  elif i[p]in list(map(str,range(10))):s.append(int(i[p]))
  elif i[p]==',':c=input()
  elif i[p]==':':s.append(s[-1])
  elif i[p]=="'":s.append(c[0]);c=c[1:]
  elif i[p]=='»':
   targ=i[p+1];tp=p;sub=1
   while 1:
    if i[p]==targ and i[p+1]==":":p+=1;break
    if len(i)-2==p:p=0
    p+=1
  elif i[p]==";"and sub==1:p=tp
  elif i[p]=="\n":break
  elif i[p]=="-":s.pop()
  elif i[p]=="+":s.append(int(s.pop())+int(s.pop()))
  elif i[p]=="`":s.append(int(s.pop())*-1)
  elif i[p]=="(":
   while i[p+1]!=")":ts.append(i[p+1]);p+=1
   ld.append("".join(ts))
  elif i[p]=="[":
   while i[p]!="]":p+=1
  if len(i)-1==p:
   while 1:
    if i[p]=="\n":break
    elif p==0:p=-1
  p+=1
 except IndexError:break
