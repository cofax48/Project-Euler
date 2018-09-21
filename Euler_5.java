public class Euler_5 {
  public static void main(String args[]) {

    long unixTime1 = System.currentTimeMillis();
    //Inelegent but very quick in java
    for (int i = 20; i < 100000000000000L; i += 20) {
      if (i % 19 == 0) {
        if (i % 18 == 0) {
          if (i % 17 == 0) {
            if (i % 16 == 0) {
              if (i % 15 == 0) {
                if (i % 14 == 0) {
                  if (i % 13 == 0) {
                    if (i % 12 == 0) {
                      if (i % 11 == 0) {
                        if (i % 10 == 0) {
                          if (i % 9 == 0) {
                            if (i % 8 == 0) {
                              if (i % 7 == 0) {
                                if (i % 6 == 0) {
                                  if (i % 5 == 0) {
                                    if (i % 4 == 0) {
                                      if (i % 3 == 0) {
                                        if (i % 2 == 0) {
                                          System.out.println(i);

                                          long currentTime = System.currentTimeMillis();
                                          long totalTime = currentTime - unixTime1;
                                          System.out.println(totalTime);
                                          break;
                                        }
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
