public class Ebook extends Book{
    private String format;
    
    Ebook (String title , String author , int pagecount,String format)
    {
        super(title, author, pagecount);    /// used to call costrctor of parent class
        this.format = format;
    }
}
