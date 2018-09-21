public class Euler_10 {
  public static boolean is_prime(int num) {
    int half_num = (num + 1) / 2;
    for (int i = 3; i < half_num; i+=2) {
      if (num % i == 0) {
        return false;
      }
    }
    return true;
  }
  public static void main (String[] args) {
    int sumNum = 5;
    for (int i = 5; i < 2000000; i+=2) {
      boolean primez = is_prime(i);
      if (primez == true) {
        //System.out.println(i);
        sumNum += i;
      }
    }
    System.out.println(sumNum);
  }
}
