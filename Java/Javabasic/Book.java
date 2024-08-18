public class Book {
    private String title;
    private String author;
    private int pagecount;

    Book (String title , String author , int pagecount)
    {
        this.title=title;
        this.author=author;
    }
    public String gettitle()
    {
        return this.title;
    }

    public String getauthor()
    {
        return this.author;
    }
    public String toString(){
        return String.format(this.title+" "+ this.author+""+this.pagecount);
    }
}
