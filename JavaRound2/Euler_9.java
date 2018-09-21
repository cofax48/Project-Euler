public class Euler_9 {
  public static boolean is_pythag(int numa, int numb, int numc) {
    int numa_prod = numa * numa;
    int numb_prod = numb * numb;
    int numc_prod = numc * numc;
    if (numa_prod + numb_prod == numc_prod) {
      return true;
    }
    return false;
  }

  public static void main (String[] args) {
    outerLoop:
    for (int c = 3; c < 10000; c++) {
      for (int b = 2; b < c; b++) {
        for (int a = 1; a < b; a++) {
          boolean pythagT = is_pythag(a, b, c);
          if (pythagT == true) {
            if (a + b + c == 1000) {
              int ptythag_prod = a * b * c;
              System.out.println(ptythag_prod);
              break outerLoop;
            }
          }
        }
      }
    }
  }
}
