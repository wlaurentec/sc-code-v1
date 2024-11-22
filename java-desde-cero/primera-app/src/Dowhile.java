public class Dowhile {
  public static void main(String[] args) throws Exception {

    // while(initialization; condition; actualization (increment/decrement))

    int contador = 1;

    do {
      System.out.println(contador);
      contador++;
    } while (contador <= 10);

    System.err.println("El valor en el cual se terminó el contador es: " + contador);  
  }
}
