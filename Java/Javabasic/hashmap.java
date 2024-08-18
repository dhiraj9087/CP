import java.util.*;
public class hashmap {
    public static void main(String[] args) {
        HashMap<String,Integer> d = new HashMap<>();
        d.put("a", 23);
        d.put("b", 46);
        d.put("t", 245);
        d.put("i", 25);
        d.replace("a",23,90);
        d.putIfAbsent("d", 876543);
        System.out.println(d);
        System.out.println(d.getOrDefault("e", -1));   
        d.forEach((i,j) ->{
            System.out.println(i+" "+j);
        });
        d.forEach((i,j) ->{
            d.replace(i, j+10);
        });
        System.out.println(d);
    }
}
