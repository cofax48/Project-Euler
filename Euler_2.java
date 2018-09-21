public class Euler_2 {
  public static void main (String args[]){
    int fib1 = 1;
    int fib2 = 2;
    int newFib = 0;
    int evenSumNum = 2;
    while (newFib < 4000000) {
      //finds the next num in the fib sequence
      newFib = fib1 + fib2;
      //updates positions
      fib1 = fib2;
      fib2 = newFib;
      //Finds if the newest fib num elem is even and adds to evenSumNum
      if (newFib % 2 == 0) {
        evenSumNum += newFib;
      }
    }
  //Prints the sum of all Even fib nums under 4 million
  System.out.println(evenSumNum);
  }
}
