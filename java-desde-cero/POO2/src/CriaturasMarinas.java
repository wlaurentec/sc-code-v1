public abstract class CriaturasMarinas {

  // Atributos
  String nombre;

  // Constructor
  public CriaturasMarinas(String nombre) {
    this.nombre = nombre;
  }

  // Esto obliga a sobrescribir en las clases que hereden de criaturas marinas
  abstract void nadar();
   
}