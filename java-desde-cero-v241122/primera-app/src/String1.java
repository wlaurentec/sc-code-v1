public class String1 {
  public static void main(String[] args) throws Exception {

      String texto = "Tienes que actuar y actuar ahora. Descubre lo que te distingue del resto";
      System.out.println(texto);

      int longitud = texto.length();
      System.out.println(longitud);

      char caracter = texto.charAt(70);
      System.out.println(caracter);

      String subcadena = texto.substring(0, 10);
      System.out.println(subcadena);

      boolean contiene = texto.contains("actuar");
      System.out.println(contiene);

      String minusculas = texto.toLowerCase();
      System.out.println(minusculas);

      String mayusculas = texto.toUpperCase();
      System.out.println(mayusculas);

      String reemplazar = texto.replace("actuar", "actuar ahora");
      System.out.println(reemplazar);

      int indice = texto.indexOf("actuar");
      System.out.println(indice);

      String[] palabras = texto.split(" ");
      System.out.println(palabras);
      for (String palabra : palabras) {
          System.out.println(palabra);
      }

  }
}
