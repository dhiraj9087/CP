public class AudioBook extends Book{
    private int runtime;
    
    AudioBook (String title , String author , int pagecount,int runtime)
    {
        super(title, author, pagecount);    /// used to call costrctor of parent class
        this.runtime = runtime;
    }
    
}
