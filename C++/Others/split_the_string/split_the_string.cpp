#include <iostream>
using namespace std;
string* split_str(string s, string del){
    static string arr[10000];
    int i;
    int oi=0;
    int ari=1;
    string slic;
    for(i=0; i<s.length(); i++){
        string ch(1,s[i]);
        if (ch == del){
            slic = s.substr(oi,i-oi);
            oi=i+1;
            arr[ari]=slic;
            ari++;
        }
        if (i==s.length()-1){
            arr[ari]=s.substr(oi,i-oi+1);
        }
    }
    string lenof = to_string(ari);
    arr[0]=lenof;
    return arr;
}
int main() {
    string aa;
    string l = "first second third forth";
    getline(cin, aa);
    string* array = split_str(aa, " ");
    int lenofar = stoi(array[0]);
    for(int i=1; i< lenofar+1; i++){
        cout<< array[i] << endl;
    }
}
