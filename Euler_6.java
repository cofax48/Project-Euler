public class Euler_6 {
  public static void main (String args[]) {

    long squareSumz = 0;
    long sumNumz = 0;
    for (long i = 1; i < 101; i++) {
      long squarez = i * i;
      squareSumz += squarez;
      sumNumz += i;
    }
    long sumzSquared = sumNumz * sumNumz;
    System.out.println("Differnce is:");
    long diff = sumzSquared - squareSumz;
    System.out.println(diff);
  }
}
