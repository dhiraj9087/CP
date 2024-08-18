import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.*;

public class array {
    public static void main(String[] args) {
        char vowel[] = new char[5];
        vowel[0]='a';
        vowel[1]='e';
        vowel[2]='i';
        vowel[3]='o';
        vowel[4]='u';
        Integer[] arr={1,2,3,4,5};
        // Arrays.sort(vowel);  // incresaing
        Arrays.sort(arr, Collections.reverseOrder());  // decreaing
        System.out.println(Arrays.toString(arr));
        System.out.println(arr.length);


        ArrayList<Integer> num = new ArrayList<Integer>();
        num.add(3);
        num.add(4);
        num.add(6);
        num.add(7);
        num.add(9);
        System.out.println(num);
        System.out.println(num.toString());
        System.out.println(num.get(0));
        num.remove(0);    // remove using index
        num.remove(Integer.valueOf(7));    // remove using value
        num.sort(Comparator.naturalOrder());
        num.sort(Comparator.reverseOrder());
        num.set(2, 89);     // to set something at pertiular index
        System.out.println(num);
        System.out.println(num.size());
        System.out.println(num.contains(6));
        num.forEach(i->{
            System.out.println(i+" "+num.indexOf(i));         // for i in a loop
        });
    }
}
