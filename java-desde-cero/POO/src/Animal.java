public class Animal {

  String nombre;
  int edad;
  static int cantidadAnimales = 0;

  public Animal(String nombre, int edad) {
    this.nombre = nombre;
    this.edad = edad;
    cantidadAnimales++;
  }

  public String hacerSonido() {
    return "Hacer sonido genérico";
  }

  public static int getCantidadAnimales() {
    return cantidadAnimales;
  }

}
