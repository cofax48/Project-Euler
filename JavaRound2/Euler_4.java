public class Euler_4 {
  public static void main (String[] args) {
    int largestPalindrome = 0;

     for (int i = 999; i > 800; i--) {
       for (int q = 999; q > 800; q--) {
         int sumNum = i * q;
         String sumNumString = Integer.toString(sumNum);
         if (sumNumString.charAt(0) == sumNumString.charAt(5)) {
           if (sumNumString.charAt(1) == sumNumString.charAt(4)) {
             if (sumNumString.charAt(2) == sumNumString.charAt(3)) {
               if (sumNum > largestPalindrome) {
                 largestPalindrome = sumNum;
               } 
             }
           }
         }
       }
     }
     System.out.println(largestPalindrome);
  }
}
