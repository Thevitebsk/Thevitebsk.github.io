p=0;tv=0;tv2=0;s=[];num=list(map(str,range(10)))
c=""""""
while len(c)>p:
 if c[p]=="*":s.append(input())
 elif c[p]=="`":
  if c[p+1]==",":s[-1]=int(s[-1])
  elif c[p+1]==".":s[-1]=float(s[-1])
  elif c[p+1]=="\"":s[-1]=str(s[-1])
 elif c[p]=="!":
  tv2=tv=s[-1]
  while tv2>1:tv2-=1;tv*=tv2
  s.append(tv)
 elif c[p]=="↑":print(s)
 elif c[p]=="↓":print(s.pop())
 elif c[p]=="[":
  while c[p]!="]":p+=1
 elif c[p]in num:s.append(int(c[p]))
 p+=1
