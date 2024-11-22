import interfaces.Alimentable;
import interfaces.Comunicable;

public class Pulpo extends CriaturasMarinas implements Comunicable, Alimentable {

  int cantTentaculos;
  
  public Pulpo(String nombre, int cantTentaculos) {
    super(nombre);
    this.cantTentaculos = cantTentaculos;
  }
  @Override
  void nadar() {
    System.out.println(nombre + " está nadando con sus" + cantTentaculos + " tentáculos");
  }

  @Override
  public void comunicarse() {
    System.out.println(nombre + " saluda con sus " + cantTentaculos + " tentáculos");
  }

  @Override
  public void alimentar() {
    System.out.println(nombre + " se alimenta con sus " + cantTentaculos + " tentáculos");
  }
}
