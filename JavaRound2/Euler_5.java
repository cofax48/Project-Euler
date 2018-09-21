public class Euler_5 {
  public static boolean is_divisible (int givenNum) {
    for (int i = 1; i < 21; i++) {
      if (givenNum % i != 0) {
        return false;
      }
    }
    return true;
  }
  public static void main (String[] args) {
    int smallestNum = 0;

    for (int i = 0; i < 300000000; i+=10) {
      boolean numDivis = is_divisible(i);
      if (numDivis == true) {
        smallestNum = i;
      }
    }
    System.out.println(smallestNum);
  }
}
