import java.util.Scanner;

public class Ahorcado {
  public static void main(String[] args) throws Exception {

    // Clase scanner para capturar la palabra
    Scanner scanner = new Scanner(System.in);

    // Declaracion de variables
    String palabraSecreta = "atributos";
    int intentosMaximos = 10;
    int intentos = 0;
    boolean palabraAdivinada = false;

    // Arreglos
    char[] letrasAdivinadas = new char[palabraSecreta.length()];

    // Estructura de control
    for (int i = 0; i < letrasAdivinadas.length; i++) {
      letrasAdivinadas[i] = '_';
      // System.out.print(letrasAdivinadas[i]);
    }

    // Estructura de control: Iterativa (Bucle)

    while (!palabraAdivinada && intentos < intentosMaximos) {
      System.out.println(
          "Palabra a adivinar: " + String.valueOf(letrasAdivinadas) + " (" + palabraSecreta.length() + " letras)");
      System.out.println("Introduce una letra, por favor:");

      // Usamos la clase scanner para pedir una letra
      // char letra = scanner.next().charAt(0);
      char letra = Character.toLowerCase(scanner.next().charAt(0));
      
      boolean letraCorrecta = false;

      // Estructura de control: Iterativa (For)

      for (int i = 0; i < palabraSecreta.length(); i++) {
        // Estructura de control: Condicionales

        if (palabraSecreta.charAt(i) == letra) {
          letrasAdivinadas[i] = letra;
          letraCorrecta = true;
        }
      }

      if (!letraCorrecta) {
        intentos++;
        System.out.println("¡Incorrecto! Te quedan " + (intentosMaximos - intentos) + " intentos");
      }

      if (String.valueOf(letrasAdivinadas).equals(palabraSecreta)) {
        palabraAdivinada = true;
        System.out.println("¡Felicitaciones! Has adivinado la palabra secreta: " + palabraSecreta);
      }

    }

    if (!palabraAdivinada) {
      System.out.println("¡Perdiste! GAME OVER");
    }

    scanner.close();

  }
}