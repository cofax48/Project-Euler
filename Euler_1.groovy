def sumNum = 0;
for (int i = 0; i < 1000; i++) {
  if (i % 3 == 0) {
    sumNum += i;
  } else if (i % 5 == 0) {
    sumNum += i;
  }
}
println sumNum

def c = {
  println it
}
1.upto(4, c)

def newSumNum = 0
//the 1 represents the starting number, the 999 reprsents the number going up to
1.upto(999, {
  if (it % 3 == 0) {
    newSumNum += it
  } else if (it % 5 == 0) {
    newSumNum += it
  }
})
println newSumNum

//if we want to iterate over steps we set the increment as the (2 in this example)
0.step 5, 2, {
  println it
}
