let a = ["*", "*", "*", "*", "*"]
 for (let i = 0; i < 5; i++) {
   c = a.join("")
   console.log(c)
   a.splice(0, 0, " ")
}