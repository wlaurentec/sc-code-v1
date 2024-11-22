public class Gato extends Animal {

  public Gato(String nombre, int edad) {
    // super(); estamos asignando la informacion de la clase padre
    super(nombre, edad);
  }

  @Override
  public String hacerSonido() {
    return "Miau";
  }

}
