/*
public class Euler_1 {
  public static void main (String[] args) {

    int sumNum = 0;
    for (int i = 0; i < 1000; i++) {
      if (i % 3==0 || i % 5 == 0) {
        sumNum += i;
        System.out.println(i);
      }
    }
    System.out.println(sumNum);
  }
}

*/
public class Euler_1 {
  public static void main (String[] args) {

    int multSum = 0;
    for (int i = 0; i < 1000; i++) {
      if (i % 3 == 0 || i % 5 == 0) {
        //System.out.println(i);
        multSum += i;
      }
    }
    System.out.println(multSum);
  }
}
