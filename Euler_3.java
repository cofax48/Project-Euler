public class Euler_3 {
  public static boolean is_prime(long num) {
    //holds number of factors
    int factorSum = 0;
    long half_num = (num / 2);
    boolean primez = false;
    //chcks to see if factors are prime
    for (int prime_factor = 1; prime_factor <= half_num; prime_factor++) {
      //checks if there's a remainder when inputted num is divided by I,
      //if so than factorSum is updated Pimes will have fewer 2
      if (num % prime_factor == 0) {
        factorSum += 1;
      }
      //If it's not a prime it will return that it is not prime
      if (factorSum > 2) {
        return primez;
      }
    }
    primez = true;
    return primez;
  }

  //Function to check whether a number is a factor
  public static boolean is_factor(double factor, long bigNum) {
    if (bigNum % factor == 0) {
      //If thre is no remainder its a factor so it's sturned as true
      return true;
    }
    else {
      //If thre is a remainder its not a factor so it's returned as flase
      return false;
    }
  }

  //Gets the party started
  public static void main (String args[]){
    int factorSum = 0;
    //The number we're starting with
    long bigNum = 600851475143L;
    //chcks to see if numbers beneath starting number are prime
    for (long num = 1; num <= bigNum; num++) {
      //checks if num_prime is true as it is a prime then
      boolean num_prime = is_prime(num);
      if (num_prime == true){
        //if num_prime is true then factors are detemrined
        boolean factorized = is_factor(num, bigNum);
        if (factorized == true) {
          System.out.println(num);
        }
      }
    }
    }
  }
