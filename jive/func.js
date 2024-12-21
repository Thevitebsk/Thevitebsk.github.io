function r(n, k) {
  return Array.from({length:k-n}, (_,i)=>n+i)
}
function fact(n) {
  let t = 1;
  for (let t2 = n; t2 > 1; t2--) { t *= t2 }
  return t;
}
