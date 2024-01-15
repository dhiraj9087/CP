#include<iostream>
using namespace std;
class pizza 
{
    private:
        string size;        //private
        int ctopping;
        int ptopping;
        int htopping;

     public :
        pizza(){
       ctopping = 0;

       ptopping = 0;

       htopping = 0;

       size = "small";
    }
   
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
        cout<<"pizza size -"<<size;
        cout<<"number of ctopping-"<<ctopping;
        cout<<"number of ptopping-"<<ptopping;
        cout<<"number of htopping-"<<htopping;
        cout<<"total bill -"<<calccost();
    }

};
int main()
{
    pizza obj;
    

    cout<<"Enter the pizza size-"<<endl;
    cout<<"enter number of ctopping"<<endl;
    cout<<"Enter number of ptopping"<<endl;
    cout<<"Enter number of htopping"<<endl;
    obj.getdescripction();
}


