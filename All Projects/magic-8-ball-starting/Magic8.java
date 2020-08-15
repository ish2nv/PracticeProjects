// import math to use random tool
import java.util.*;

public class Magic8 {

  public static void main(String[] args) {
    
    int randomgen = random8generator(1,8);
    // run the code in main and print out the randomly decided fortune-telling
    switch(randomgen) {
      
      case 1:
      System.out.println("The easiest way to grow, is to let Go. Knowing, that someone else is managing the show!");
      break;
      case 2:
      System.out.println("We light the oven so that everyone may bake bread in it.");
      break;
      case 3:
      System.out.println("What helps you persevere is your resilience and commitment.");
      break;
      case 4:
      System.out.println("Motivation gets you going; Inspiration keeps you going.");
      break;
      case 5:
      System.out.println("When all is said and done, more is said than done.");
      break;
      case 6:
      System.out.println("Dont wait for things to happen. Make them happen.");
      break;
      case 7:
      System.out.println("Divinely Fabulous Inside & Out!");
      break;
      case 8:
      System.out.println("If you are still living in sin, you are not saved.");
      break;
      default: 
      System.out.println("Value somehow went over the maximum value");
      break;
    }
    System.out.println("Value is: " + randomgen);

  }
    public static int random8generator(int min, int max) {
    Random random = new Random();
   int randomval= random.nextInt(max - min + 1) + min;
   return randomval;
  }
}