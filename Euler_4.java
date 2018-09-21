//Imports list features
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Euler_4 {
  //Makes an equality test
  public static boolean is_pallindrome(String zero_i, String one_i) {
    if (new String(zero_i).equals(one_i)){
      return true;
    }
    else {
      return false;
    }
  }

  public static void main (String args[]) {

    //Initializes the list of products
    ArrayList<Integer> prodList = new ArrayList<Integer>(100);

    //Also works maybe?
    //ArrayList palindromes = new ArrayList();
    //palindromes.add(product);

    //No point in searching lower than 500
    for (int i = 500; i < 999; i++){
      for (int q = 500; q < 999; q++) {
        //Finds the poduct
        int intProd = i * q;
        //Makes the product into a string
        String numProd = Integer.toString(intProd);
        //Gets the value at each position
        String zeroPos = Character.toString(numProd.charAt(0));
        String onePos = Character.toString(numProd.charAt(1));
        String twoPos = Character.toString(numProd.charAt(2));
        String threePos = Character.toString(numProd.charAt(3));
        String fourPos = Character.toString(numProd.charAt(4));
        String fivePos = Character.toString(numProd.charAt(5));

        boolean outterNum = is_pallindrome(zeroPos, fivePos);
        if (outterNum == true) {
          boolean midNum = is_pallindrome(onePos, fourPos);
          if (midNum == true) {
            boolean innerNum = is_pallindrome(twoPos, threePos);
            if (innerNum == true) {
              prodList.add(intProd);
            }
          }
        }
      }
    }

    //sorts the list
    Collections.sort(prodList);
    //gets the last element in the list-which in this case is th biggest num
    int elem = prodList.get(prodList.size() - 1);
    System.out.println(elem);
    //System.out.println(prodList);
  }
}
