class Pizza{

   String pizzasize;

   int cheese;

   int pepperoni;

   int mushroom;

   

   public Pizza(){

       cheese = 0;

       pepperoni = 0;

       mushroom = 0;

       pizzasize = "small";

   }

   

   public double CalculateCost(){

       double bill = 0;

       if(pizzasize.toLowerCase() == "small"){

           bill+=500 + 25*(cheese+pepperoni+mushroom);

       }

       else if(pizzasize.toLowerCase() == "medium"){

           bill+=650 + 25*(cheese+pepperoni+mushroom);

       }

       else{

           bill+=800 + 25*(cheese+pepperoni+mushroom);

       }

       return bill;

   }

   

   public void PizzaDescription(){

       System.out.println("Pizza size - "+pizzasize.toLowerCase());

       System.out.println("Number of cheese toppings - "+cheese);

       System.out.println("Number of pepperoni toppings - "+pepperoni);

       System.out.println("Number of mushroom toppings - "+mushroom);

       System.out.println("total bill= Rs."+CalculateCost());

   }

   

   public static void main(){

       Scanner sc = new Scanner(System.in);

       Pizza obj = new Pizza();

       System.out.println("Enter the pizza size - (small,medium or large)");

       obj.pizzasize = sc.nextLine();

       System.out.println("Enter the number of cheese toppings");

       obj.cheese = sc.nextInt();

       System.out.println("Enter the number of pepperoni toppings");

       obj.pepperoni = sc.nextInt();

       System.out.println("Enter the number of mushroom toppings");

       obj.mushroom = sc.nextInt();

       obj.PizzaDescription();

   }

}

