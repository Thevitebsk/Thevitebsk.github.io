contohtml=async function(file){
    confile = await( await fetch(`./${file}`) ).text()
    console.log(confile)
}
