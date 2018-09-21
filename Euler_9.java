public class Euler_9 {
  public static void main(String args[]) {

    //Finds numbers that when added together = 1000;
    for (int a = 0; a < 1001; a++) {
      for (int b = 0; b < 1001; b++) {
        for (int c = 0; c < 1001; c++) {
          if (a + b + c == 1000) {
            //Tests to see whether a < b < c
            if (a < b) {
              if (b < c) {
                //Finds the square roots
                int asq = a * a;
                int bsq = b * b;
                int csq = c * c;
                //Tests whether its a pythag_trip
                if (asq + bsq == csq) {
                  int prod = a * b * c;
                  //Prints the rsult
                  System.out.println(prod);
                }
              }
            }
          }
        }
      }
    }
  }
}
