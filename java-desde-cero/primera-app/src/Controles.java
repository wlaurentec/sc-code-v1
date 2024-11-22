public class Controles {
  public static void main(String[] args) throws Exception {

    int i;

    System.out.println("***** break ******");

    for (i = 1; i <= 10; i++) {
      System.out.println(i);

      if (i == 5) {
        break; // Salir del bucle
      }
    }

    System.out.println("***** continue ******");

    for (i = 1; i <= 10; i++) {
      System.out.println(i);

      if (i == 5) {
        continue; // Saltea las lineas siguientes al bucle
      }

      System.out.println("Alguito mas sucede " + i);
    }


    System.out.println("***** return ******");

    for (i = 1; i <= 10; i++) {
      System.out.println(i);

      if (i == 5) {
        return; // Saltea las lineas siguientes al bucle
      }

      System.out.println("Alguito mas sucede " + i);
    }

  }
}
