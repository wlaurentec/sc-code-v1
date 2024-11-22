public class App {
  public static void main(String[] args) throws Exception {

    Animal animal = new Animal("Bestia", 200);
    Gato gato = new Gato("Gatito", 5);
    Perro perro = new Perro("Perrito", 10);

    System.out.println(animal.hacerSonido());
    System.out.println(gato.hacerSonido());
    System.out.println(perro.hacerSonido());

    System.out.println(Animal.getCantidadAnimales());

    System.out.println(Veterinaria.nombre);
  }
}
