="""@helo!|#"""
p=0;s=[];ts=[];m=0
while True:
 if i[p]=="@":
  p+=1
  while 1:
   ts.append(i[p]);p+=1
   if i[p]=="\n" or i[p]=="|":break
  while len(ts)>1:a=str(ts[0])+str(ts[1]);ts.pop(0);ts.pop(0);ts.reverse();ts.append(a);ts.reverse()
  s.append(ts[0]);ts.pop
 if i[p]=="#":s.reverse();print(s[0]);s.reverse();s.pop()
 elif i[p]=="ƒ":s.reverse();print(s[0],end="");s.reverse();s.pop()
 elif i[p]=="~":m=1
 p+=1
 if p==len(i) and m==0:break
 elif p==len(i) and m==1:
  while True:
   p-=1
   if i[p]=="\n":break
   elif p==0:break