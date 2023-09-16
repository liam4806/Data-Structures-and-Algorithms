#include <iostream>
using namespace std;

int main() {
    int arr1len, arr2len, i, arr1num, arr2num,y;
    int flag=0;
    cout << "Enter Arr1: ";
    cin >> arr1len;
    int arr1[arr1len];
    for(i=0; i<arr1len; i++){
        cin >> arr1num;
        arr1[i]=arr1num;
    }
    cout << "Enter Arr2: ";
    cin >> arr2len;
    for(i=0; i<arr2len; i++){
        cin >> arr2num;
        for(y=0; y<arr1len; y++){
            if(arr1[y]==arr2num){ 
                arr1[y]=0;
                flag++;
                break;
            }else{
                continue;
            }
        }
    }
    if(flag == arr1len){
        cout <<"Array B covers array A" << endl;
    }else{
        cout <<"Array B does not covers array A" << endl;
    }

    return 0;
}
