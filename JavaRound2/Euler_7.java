public class Euler_7 {
  public static boolean is_prime (int num) {
    int half_num = (num + 1) / 2;
    for (int i = 3; i < half_num; i+=2) {
      System.out.println(i);
      if (num % i == 0) {
        return false;
      }
    }
    return true;
  }
  public static void main (String[] args) {
    int prime_num_count = 1;
    int prime_num_to_use = 0;
      for (int i = 1; prime_num_count < 102; i+=2){
        boolean primez = is_prime(i);
        if (primez == true) {
          System.out.println(i);
          prime_num_to_use = i;
          prime_num_count += 1;
        }
      }
    System.out.println(prime_num_to_use);
  }
}
