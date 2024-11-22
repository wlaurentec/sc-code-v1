public class For {
  public static void main(String[] args) throws Exception {

    // for(initialization; condition; actualization (increment/decrement))
    for (int i = 0; i < 10; i++) {
      System.out.println(i);
    }

    int i;

    for (i = 0; i < 10; i++) {
      System.out.println(i);
    }

    System.out.println("El valor en el cual se terminó i es: " + i);

    int j;

    for (i = 1; i <= 10; i++) {
      for (j = 1; j <= 10; j++) {
        System.out.println(i + " x " + j + " = " + (i * j));
      }
    }


  }
}
