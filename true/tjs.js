function main(){
  p = 0 ; output = '' ; s = [] ; ts = [] //; m = 0
  num = ["0","1","2","3","4","5","6","7","8","9"] ; code = document.getElementById("program").value ; input = document.getElementById("input").value.split("\n");
  while (code.length>p){
    //i will focus on the strings later
    //if (code[p]=='"'){ m=1 ; p++ };
    //while (m==1){ ts.push(code[p]) ; p++ ; if (code[p+1]!=='"'){ break } }
    if (code[p]in num /*&& m==0*/){ s.push(code[p]) }
    else if (code[p]=="."){ if (s.length>0){ output += s.pop() } else { break } }
    else if (code[p]=="-"){if (s.length>0){ s.pop()} else { break } }
    else if (code[p]=="\n"){ break }
    p++
  } ; document.getElementById("console").innerHTML=output+'\nSTACK: ['+s+']\nTEMPSTACK: ['+ts+']\nBYTES: '+code.length+'PERMALINK: '+"https://thevitebsk-github-io.vercel.app/true/ti.html/?c="+encodeURIComponent(document.getElementById("program").value)
}
