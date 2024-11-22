// import java.util.HashMap;
// import java.util.TreeMap;
import java.util.LinkedHashMap;
import java.util.Map;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Bienvenidos a nuestra verduleria!");

        // Map<String, Double> inventario = new HashMap<>(); // HashMap sin orden
        // Map<String, Double> inventario = new TreeMap<>(); // TreeMap con orden alfabetico
        Map<String, Double> inventario = new LinkedHashMap<>(); // LinkedHashMap con orden de insercion

        inventario.put("Pera", 0.90);
        inventario.put("Piña", 1.50);
        inventario.put("Naranja", 0.70);
        inventario.put("Sandia", 1.20);
        inventario.put("Melon", 2.50);
        

        System.out.println("Este es nuestro inventario:");
        
        // keySet() nos permite recorrer las claves del inventario
        for (String fruta : inventario.keySet()) {
            // get() nos permite obtener el valor de la clave
            System.out.println(fruta + ": $" + inventario.get(fruta));
        }
        

        String frutaBuscada = "Melon";

        System.out.println("Se acerca un cliente que quiere comprar " + frutaBuscada);

        if (inventario.containsKey(frutaBuscada)) {
            System.out.println("Tenemos " + frutaBuscada + " en nuestro inventario");
        } else {
            System.out.println("No tenemos " + frutaBuscada + " en nuestro inventario");
        }

        String sinStock = "Melon";
        inventario.remove(sinStock);

        System.out.println("Se ha agotado " + sinStock);


        System.out.println("Este es nuestro inventario actualizado:");
        for (String fruta : inventario.keySet()) {
            System.out.println(fruta + ": $" + inventario.get(fruta));
        }

        System.out.println("La cantidad total de frutas es: " + inventario.size());
        System.out.println("Gracias por visitarnos!");
    }
}
