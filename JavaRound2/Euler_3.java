/*
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
*/
public class Euler_3 {

  public static boolean is_prime (long num) {
    long half_num = (num / 2);
    for (int i = 3; i <= half_num; i+=2) {
      if (num % i == 0) {
        return false;
      }
    }
    return true;
  }

  public static boolean is_factor (long factorNum, int i) {
    if (factorNum % i == 0) {
      return true;
    } else {
      return false;
    }
  }

  public static void main (String[] args) {

    long factorNum = 600851475143L;
    for (int i = 5; i < factorNum; i+=2) {
      if (i % 3 != 0) {
          boolean primez = is_prime(i);
          if (primez == true) {
            boolean factorz = is_factor(factorNum, i);
            if (factorz == true) {
              System.out.println(i);
            }
          }
      }
    }
  }
}
