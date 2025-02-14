function main(){
  code = document.getElementById("program").value ; input = document.getElementById("input").value.split("\n")
  p = 0 ; output = '' ; s = [] ; ts = [] /*; m = 0*/ ; cons = output+'\nSTACK: ['+s+']\nTEMPSTACK: ['+ts+']\nBYTES: '+code.length
  num = ["0","1","2","3","4","5","6","7","8","9"] ; perma = encodeURIComponent(document.getElementById("program").value)
  while (code.length>p){
    //i will focus on the strings later
    //if (code[p]=='"'){ m=1 ; p++ };
    //while (m==1){ ts.push(code[p]) ; p++ ; if (code[p+1]!=='"'){ break } }
    if (code[p]in num /*&& m==0*/){ s.push(code[p]) }
    else if (code[p]=="."){ if (s.length>0){ output += s.pop() } else { break } }
    else if (code[p]=="-"){if (s.length>0){ s.pop()} else { break } }
    else if (code[p]=="\n"){ break }
    p++; if (perma){ cons += "\nPERMALINK: "+perma }
  } ; document.getElementById("console").innerHTML=cons
}
