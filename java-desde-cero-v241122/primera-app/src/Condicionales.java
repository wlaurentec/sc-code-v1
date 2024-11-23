// import java.util.Scanner;

public class Condicionales {

  public static void main(String1[] args) {

   /*  int edad = 18;

    if (edad >= 18) {
      System.out.println("Eres mayor de edad");
    } else {
      System.out.println("Eres menor de edad");
    } */

    /* Scanner scanner = new Scanner(System.in);

    System.out.println("Introduce tu bebida favorita");
    String bebida = scanner.nextLine();

    switch (bebida) {
      case "Cerveza":
        System.out.println("Bebida alcoholica");
        break;
      case "Agua":
        System.out.println("Bebida no alcoholica");
        break;
      default:
        System.out.println("No conozco la bebida");
        break;
    }
    scanner.close(); */

    /* int i;
    int j;
    int k;

    for (i = 0; i < 10; i++) {
      for (j = 0; j < 5; j++) {
        for (k = 0; k < 3; k++) {
          System.out.println("i = " + i + ", j = " + j + ", k = " + k);
        }
      }
    } */


  /*   int contador = 0;

    while (contador < 10) {
      System.out.println("contador = " + contador);
      contador++;
    } */


    /* int contador = 0;

    do {
      System.out.println("contador = " + contador);
      contador++;
    } while (contador < 10); */


    int i = 0;

    for (i = 0; i < 10; i++) {
      if (i == 5) {
        break;
      }
      System.out.println("i = " + i);
    }

    for (i = 0; i < 10; i++) {
      if (i == 5) {
        continue;
      }
      System.out.println("i = " + i);
    }


    for (i = 0; i < 10; i++) {
      if (i == 5) {
        return;
      }
      System.out.println("i = " + i);
    }


  }

}
