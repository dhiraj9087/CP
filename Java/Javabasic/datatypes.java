public class datatypes {
    public static void main(String[] args) {
        byte num1=100;//-128 to 127
        short num2=20000; // -32768 to 32768
        int num3 = 2147483647; // -2147483647 to 2147483647
        long num4 = 9223372036854775807L ;  // -9223372036854775807 to 9223372036854775807
        double num5 = 1.2435;  // 4.9E-324 to 1.79.... very long range
        float num6  = 3.4028F;  // by deafult compoler takes double for float we need to declear it same for long 
        

        // typecasting
        int a=8;
        double b=a;   // we can chnge type from small to big but not from big to small (int->double possible)
        System.out.println(b); 
        double s=9.8;
        int s2=(int)s;  
          // you can chnge big to small but you need to declear small 
        System.out.println(++s2);  
        System.out.println(s2++); 
        System.out.println(s2); 


        // String name = new String("stwefdvc ");
        // System.out.println(name);
        String name = "sdjf";
        System.out.println(name.length());
        System.out.println(name.isBlank());
        System.out.println(name.isEmpty());
        System.out.println(name.toUpperCase());


    }
}
