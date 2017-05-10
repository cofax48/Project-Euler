#! Euler number 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

#MY Answer
def multiples_of_three():
    """Finds the sum of all multiples of 3 and 5 below 1000"""
    sum_list = []
    for i in range(0, 1000):
        three_result = int(i * 3)
        if three_result < 1000:
            sum_list.append(three_result)
    for i in range(0, 1000):
        five_result = int(i * 5)
        if five_result < 1000:
            if five_result not in sum_list:
                sum_list.append(five_result)

    super_sum = 0
    for a in sorted(sum_list):
        print(a)
        super_sum += a
    print(super_sum)

multiples_of_three()

#Shortest Answer
def euler001(limit):
    return sum(n for n in range(limit) if n % 3 == 0 or n % 5 == 0)

print(euler001(1000))

"""
//This is the solution to Euler problem 1 in JavaScript
/*
succes_list = [];
i = 0;
var three = 3;
var five = 5;
while (i < 1000) {
  if (i % 15 == 0) {
    succes_list.push(i);
    i += 1;
  }
  else if (i % 3 == 0) {
    succes_list.push(i);
    i += 1
  }
  else if (i % 5 == 0) {
    succes_list.push(i);
    i += 1;
  }
  else {
    i += 1;
  }
}

new_value = 0;
for (i in succes_list) {
  value = succes_list[i];
  new_value += value;
}
console.log("The sum of all multiples of 3 and 5 beneath 1000 are " + new_value);
"""
