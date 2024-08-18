// import java.time.LocalDate;

// public class HelloWorld {
//     public static void main(String[] args) {

//         User user = new User("fgdbf","1935-01-23");
//         // user.name="fgdbf";
//         // user.birthday = LocalDate.parse("1935-01-23");
//         System.out.printf(user.getname() + "->" + user.getbirthday()+"  "+user.age()+"\n");

//         Book book = new Book("book 1","author x1",290);
//         AudioBook book2= new AudioBook("book 2","author x2",0,30000);
//         Ebook book3 = new Ebook("book 3","author x3 ",280,"pdf");
//         // book.title = "book 1";
//         // book.author = "author x1";
//         System.out.printf(book.gettitle() + " -> " + book.getauthor() + "\n");
    
//         user.borrow(book); 
//         System.out.println(user.borrowedbooks().toString());

//         System.out.println(book2);
//         System.out.println(book3);
//     }
// }
// package Java;

import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.*;;

class HelloWorld
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t>0) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            int maxi = Math.max(a,Math.max(a,b));
            if (maxi<=(a+b+c-maxi)) {
                System.out.println("Yes");
            }   
            else System.out.println("No");
            t--;
        }
        sc.close();

	}
}
