i="""@hi|#"""
p=m=0;s=[];ts=[]
while 1:
 if i[p]=="@":
  p+=1
  while 1:
   ts.append(i[p]);p+=1
   if i[p]=="|":break
  ts.reverse()
  while len(ts)>1:ts.append(str(ts.pop())+str(ts.pop()))
  s.append(ts[0]);ts.pop
 if i[p]=="#":s.reverse();print(s[0]);s.reverse();s.pop()
 elif i[p]=="ƒ":s.reverse();print(s[0],end="");s.reverse();s.pop()
 elif i[p]=="~":m=1
 p+=1
 if p==len(i) and m==0:break
 elif p==len(i) and m==1:
  while 1:
   p-=1
   if i[p]=="\n":m=0;break
   elif p==0:m=0;break
