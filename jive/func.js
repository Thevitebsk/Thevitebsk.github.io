function r(n, k) {
  return Array.from({length:k-n}, (_,i)=>n+i)
}
function fact(n){
  t2 = t = n ; while (t2 > 1){t2 -= 1;t *= t2}
  return t2
}
