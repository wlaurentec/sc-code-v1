public class Arreglos {
  public static void main(String[] args) throws Exception {

      int[] numeros = new int[5];
      numeros[0] = 1;
      numeros[1] = 2;
      numeros[2] = 3;
      numeros[3] = 4;
      numeros[4] = 5;

      System.out.println(numeros);
      System.out.println(numeros.length);
      System.out.println(numeros[0]);

      for (int i = 0; i < numeros.length; i++) {
          System.out.println(numeros[i]);
      }

      for (int numero : numeros) {
          System.out.println(numero);
      }

      String[] frutas = {"manzana", "banana", "pera", "naranja", "kiwi"};

      for (int i = 0; i < frutas.length; i++) {
          System.out.println(frutas[i]);
      }

      String palabra = "Abecedario";

      System.out.println(palabra.length());
  

  }
}
