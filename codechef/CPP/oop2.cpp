#include<iostream>
using namespace std;
class pizza 
{
    //

     public :
     
        string size;        //private
        int ctopping;
        int ptopping;
        int htopping;

    //
   
    public: double calccost()           //calculation
    {
        double bill=0;

        if(size == "small")
        {
            bill+=10 + 2*(ctopping+ptopping+htopping);
        }
        else if(size == "medium")
        {
            bill+=12 + 2*(ctopping+ptopping+htopping);
        }
        else{
            bill+=14 + 2*(ctopping+ptopping+htopping);
        }
        return bill;
    }
    public: void getdescripction()                          //display func
    {
        cout<<"pizza size -"<<size<<endl;
        cout<<"number of ctopping-"<<ctopping<<endl;
        cout<<"number of ptopping-"<<ptopping<<endl;
        cout<<"number of htopping-"<<htopping<<endl;
        cout<<"total bill -"<<calccost();
    }

};
int main()
{
    pizza obj;
    string size;
    int ctopping,ptopping,htopping;
    

    cout<<"Enter the pizza size-"<<endl;
    cin>>size;
    
    cout<<"enter number of ctopping"<<endl;
    cin>>ctopping;
    
    cout<<"Enter number of ptopping"<<endl;
    cin>>ptopping;
    
    cout<<"Enter number of htopping"<<endl;
    cin>>htopping;

    obj.getdescripction();
}


