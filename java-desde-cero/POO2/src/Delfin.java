import interfaces.Alimentable;
import interfaces.Comunicable;

public class Delfin extends CriaturasMarinas implements Comunicable, Alimentable {
  
  public Delfin(String nombre) {
    super(nombre);
  }

  @Override
  void nadar() {
    System.out.println(nombre + " está nadando en velocidad con su cola y saltando sobre el agua"); 
  }

  @Override
  public void comunicarse() {
    System.out.println(nombre + " emite sonidos y chasquidos para comunicarse");
  }
  
  @Override
  public void alimentar() {
    System.out.println(nombre + " se alimenta con peces y crustáceos");
  }

}
