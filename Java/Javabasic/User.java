import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;

public class User {
    private String name;
    private LocalDate birthday;
    private ArrayList<Book> books  = new ArrayList<Book>();

    User(String name , String birthday)
    {
        this.name=name;
        this.birthday=LocalDate.parse(birthday);
    }
    public String getname()
    {
        return this.name;
    }
    public String getbirthday()
    {
        return this.birthday.toString();
    }

    public String borrowedbooks()
    {
        return this.books.toString();
    }

    public void borrow(Book book) 
    {
        this.books.add(book);
        // System.out.println(books + " "+ book);
    }

    public int age(){
        int age = (Period.between(this.birthday, LocalDate.now())).getYears();
        // System.out.println(age);
        return age;
    }
}
