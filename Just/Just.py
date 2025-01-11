i=""""""
p=m=0;s=[];ts=[]
while 1:
 if i[p]=="\"":
  p+=1
  while 1:
   ts.append(i[p]);p+=1
   if i[p]=="\"":break
   elif i[p]=="\n":break
  ts.reverse()
  while len(ts)>1:ts.append(str(ts.pop())+str(ts.pop()))
  s.append(ts[0]);ts.pop
 if i[p]=="#":print(s.pop())
 elif i[p]=="k":print(s[-1])
 elif i[p]=="~":m=1
 elif i[p]=="␀":
  if i[p+1]=="␅":s.append(0)
  else:...
 elif i[p]=="␁":
  if i[p+1]=="␅":s.append(1)
  else:s.append(input())
 p+=1
 if p==len(i) and m==0:break
 elif p==len(i) and m==1:
  while 1:
   p-=1
   if i[p]=="\n":m=0;break
   elif p==0:m=0;break
