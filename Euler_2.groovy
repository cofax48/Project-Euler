def num1 = 1
def num2 = 2

def sumNum = 2

while ({
  def num3 = num1 + num2
  println num3
  if (num3 % 2 == 0) {
    sumNum += num3
  }
  num1 = num2
  num2 = num3

  sumNum < 4000000
}()) continue
println sumNum

def sumNum2 = 0
for(;;){ // infinite for

    if( sumNum2 == 100 ){ //condition to break, oppossite to while
        break
    }
    else {
      sumNum2 += 10
      println sumNum2
    }
}
