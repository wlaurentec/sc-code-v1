public class Arreglos {
  public static void main(String[] args) throws Exception {

    // Arreglos: Colecciones de datos de un mismo tipo que se pueden almacenar en
    // una sola variable de tipo array o vector
    // Se distribuyen secuencialmente en memoria y se puede acceder a cada uno de
    // ellos mediante un índice
    // Los arreglos son también conocidos como matrices o vectores

    // Declarar un arreglo
    int[] numeros = new int[5];
    numeros[0] = 1;
    numeros[1] = 2;
    // numeros[2] = 3;
    numeros[3] = 4;
    numeros[4] = 5;

    for (int index = 0; index < numeros.length; index++) {
      System.out.println(numeros[index]);
    }


    // int[] numeros2 = new int[] { 1, 2, 3, 4, 5 };
    int[] numeros2 = { 10, 20, 30, 40, 50 };

    numeros2[0] = 100;

    // ForEach
    // Un bucle que recorre todos los elementos de un arreglo
    for (int numero : numeros2) {
      System.out.println(numero);
    }

    int indice = 0;
    for (int numero : numeros2) {
      System.out.println(numero);
      System.out.println(indice);
      indice++;
    }

    String palabra = "Abecedario";
    System.out.println(palabra.length());

  }
}
