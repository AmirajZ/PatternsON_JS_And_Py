let a = "+"
let b = " "
let n = prompt("Enter the number of row: ")
for(let i= 0;i<=n;i++){
  if(i==n){
    console.log(a.repeat([9]))
  }
  else{
    console.log(b.repeat([4])+a)
  }
}
for(let i= 0;i<=n-1;i++){
  console.log(b.repeat([4])+a)
}