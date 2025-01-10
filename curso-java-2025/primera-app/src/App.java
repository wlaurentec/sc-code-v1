public class App {
    public static void main(String[] args) throws Exception {

        String texto = "Tienes que creer en lo que haces para obtener lo que quieres";

        System.out.println(texto);

        int longitud = texto.length();

        System.out.println("La longitud es: " + longitud);

        char primeraLetra = texto.charAt(0);

        System.out.println("La primera letra es: " + primeraLetra);

        String subString = texto.substring(0, 6);

        System.out.println("El substring es: " + subString);

        int indice = texto.indexOf("c");

        System.out.println("El indice es: " + indice);

        String mayusculas = texto.toUpperCase();

        System.out.println("El texto en mayusculas es: " + mayusculas);

        String reemplazado = texto.replace("creer", "cree");

        System.out.println("El texto reemplazado es: " + reemplazado);

        boolean contiene = texto.contains("creer");

        System.out.println("El texto contiene la palabra 'creer': " + contiene);

        String sinEspacios = texto.trim();

        System.out.println("El texto sin espacios es: " + sinEspacios);
    }
}
