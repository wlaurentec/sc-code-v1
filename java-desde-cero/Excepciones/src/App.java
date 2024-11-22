import Excepcions.CalculadoraException;
// import Excepcions.DividirPorCeroExcepcion;

public class App {
    public static void main(String[] args) throws Exception {
        
        int numero1 = 10;
        int numero2 = 5;
        int resultado;

        Calculadora calculadora = new Calculadora();

        try {
            resultado = calculadora.dividir(numero1, numero2);
            System.out.println("El resultado es: " + resultado);
        } catch (CalculadoraException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("Se ejecuta siempre sea que haya un error o no");
        }


        System.out.println("Fin del programa");
    }
}
