public class Euler_7 {
  public static boolean is_prime(int num) {
    int half_num = (int)Math.round(num / 2);
    int count = 0;
    for (int i = 1; i <= half_num; i++) {
      if (num % i == 0) {
        count += 1;
      }
      if (count == 2) {
        return false;
      }
    }
    return true;
  }

  public static void main (String args[]) {
    int primeCount = 1;
    int counter = 0;
    while (counter < 10002) {
      boolean primer = is_prime(primeCount);
      if (primer == true) {
        counter += 1;
      }
      primeCount += 1;
    }
    System.out.println(counter);
    System.out.println(primeCount - 1); //Because 1 doesnt count as prime
  }
}
