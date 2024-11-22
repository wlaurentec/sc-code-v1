public class Persona {

  // Atributos (estado/caracteristicas)

  private String nombre;
  private String apellido;
  private int edad;

  // Constructor

  public Persona(String nombre, String apellido, int edad) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.edad = edad;
  }


  // Metodo (funcionalidad)

  public String darNombreCompleto() {
    // return apellido + ", " + nombre;
    return getApellido() + ", " + getNombre();
  }

  public String enviarSaludo(String saludado) {
    if (edad > 40)
      return "Buenos dias, querido " + saludado + ".";
    return "Hola, ¿cómo estas " + saludado + "?";
  }


  // Getters y Setters

  public String getNombre() {
    return nombre;
  }


  public void setNombre(String nombre) {
    this.nombre = nombre;
  }


  public String getApellido() {
    return apellido;
  }


  public void setApellido(String apellido) {
    this.apellido = apellido;
  }


  public int getEdad() {
    return edad;
  }


  public void setEdad(int edad) {
    this.edad = edad;
  }



  
}