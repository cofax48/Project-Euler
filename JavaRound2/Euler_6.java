public class Euler_6 {
  public static int nat_nums (int num) {
    int numSum = 0;
    for (int i = 0; i < num; i++) {
      int iSum = i*i;
      numSum += iSum;
    }
    return numSum;
  }

  public static int square_num (int num) {
    int numSumSquared = 0;
    int numSum = 0;
    for (int i = 0; i < num; i++) {
      numSum += i;
    }
    numSumSquared = numSum * numSum;
    return numSumSquared;
  }

  public static void main (String[] args) {
    int difference = 0;
    int nat_nums_sum = nat_nums(101);
    int numSumSquared = square_num(101);
    difference = numSumSquared - nat_nums_sum;
    System.out.println(nat_nums_sum);
    System.out.println(numSumSquared);
    System.out.println(difference);

  }
}
