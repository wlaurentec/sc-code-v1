import java.util.List;
import java.util.Vector;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Bienvenidos a la fiesta de los superhéroes!");

        List<String> superHeroes = new Vector<>();

        superHeroes.add("Superman");
        superHeroes.add("Batman");
        superHeroes.add("Aquaman");
        superHeroes.add("Flash");
        superHeroes.add("Wolverine");
        superHeroes.add("Green Lantern");
        superHeroes.add("Hulk");
        superHeroes.add("Spiderman");

        // Despues llego tarde nuestro superheroe estrella
        superHeroes.add("Ironman");

        if (superHeroes.contains("Spiderman")) {
            System.out.println("Spiderman está en la fiesta");
        }

        System.out.println("El superheroe ebrio es:" + superHeroes.get(2));

        superHeroes.set(8, "Tony Stark");
        System.out.println("El identidad de Ironman es: " + superHeroes.get(8));

        superHeroes.remove(2);

        if (!superHeroes.contains("Hulk")) {
            System.out.println("Hulk se ha ido dela fiesta");
    }

    // Fue y volvio tan rapido

    superHeroes.add("Superman");
    superHeroes.add("Superman");
    superHeroes.add("Superman");



    if(superHeroes.isEmpty()) {
        System.out.println("La fiesta se acabó, no hay nadie en la fiesta");
    } else {
        System.out.println("La fiesta sigue con " + superHeroes.size() + " superhéroes");
    }

    System.out.println("Los superhéroes de la fiesta son:");
    for (String superHeroe : superHeroes) {
        System.out.println(superHeroe);
    }
}
}