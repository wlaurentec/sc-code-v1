// import java.util.HashSet;
// import java.util.TreeSet;
import java.util.LinkedHashSet;
import java.util.Set;

public class CollectionSet {
    public static void main(String[] args) throws Exception {
        System.out.println("Bienvenidos a la fiesta de los superhéroes!");

        // Set<String> superHeroes = new HashSet<>(); // No acepta elementos duplicados sin importar el orden
        // Set<String> superHeroes = new TreeSet<>(); // Acepta elementos duplicados y los ordena de menor a mayor
        Set<String> superHeroes = new LinkedHashSet<>(); // Acepta elementos duplicados y los ordena en el orden en el que fueron añadidos


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

        superHeroes.remove("Hulk");

        if (!superHeroes.contains("Hulk")) {
            System.out.println("Hulk se ha ido de la fiesta");
    }

    // Fue y volvio tan rapido

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