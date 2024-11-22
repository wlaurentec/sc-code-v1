public class App {
    public static void main(String[] args) throws Exception {

        Circulo circulo = new Circulo(5);
        Rectangulo rectangulo = new Rectangulo(10, 5);
        
        circulo.imprimirInfornmacion();
        System.out.println("El area del circulo es: " + circulo.calcularArea());
        rectangulo.imprimirInfornmacion();
        System.out.println("El area del rectangulo es: " + rectangulo.calcularArea());


    }
}
