#include <bits/stdc++.h>
using namespace std;
int main(){
    string file_name,line;
    int count=0;
    cout << "Enter a file name in the same directory\n";
    cin >> file_name;
    ifstream file(file_name);
    while(getline(file,line)){
    count++;
    }
    cout << "No. of lines in the given file:"<<count<<"\n";
    
}
