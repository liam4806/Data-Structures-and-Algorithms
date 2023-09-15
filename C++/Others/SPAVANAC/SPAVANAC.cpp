#include <iostream>
using namespace std;

int main() {
    int hr,min;
    cin >> hr >> min;
    if (min-45 <0){
        min = 60-(min-45)*-1;
        if(hr-1 <0){
            hr=23;
        }else{
            hr=hr-1;
        }
    }else{
        min=min-45;
    }
    cout<<hr<< " " << min << endl;
}
