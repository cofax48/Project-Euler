// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//
// Find the sum of all the primes below two million.
import java.math.BigInteger;


public class Euler_10 {
  public static boolean is_prime(long num) {
    long half_num = num / 2;
    long primeSum = 0;
    for (long i = 1; i < half_num; i+=2) {
      if (num % i == 0) {
        primeSum += 1;
      }
      if (primeSum == 2) {
        return false;
      }
    }
    return true;
  }

  public static void main(String args[]) {
    BigInteger primeSum = BigInteger.valueOf(-5); //because 1 doesn't count and 4 is treated as prime by prime function
    for (long i = 1; i < 2000001; i++) {
      boolean primer = is_prime(i);
      if (primer == true) {
        //System.out.println(i);
        primeSum = primeSum.add(BigInteger.valueOf(i));
      }
    }
    System.out.println(primeSum);
  }
}
