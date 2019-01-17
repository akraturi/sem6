#include <bits/stdc++.h>
using namespace std;
string trim(const string& str)
{
    size_t first = str.find_first_not_of(' ');
    if (string::npos == first)
    {
        return str;
    }
    size_t last = str.find_last_not_of(' ');
    return str.substr(first, (last - first + 1));
}
int main(){
    string file_name,line;
    // variable to track the number of lines in the program
    int count=0;
    int comment=0;
    int curly = 0;
    cout << "Enter a file name in the same directory\n";
    cin >> file_name;
    ifstream file(file_name);
    // counts the number of lines 
    while(getline(file,line))
    {
    cout << line <<"\n";
    string temp = trim(line);
    if(temp.rfind("//",0)==0){
    comment++;
    }
    if(temp.rfind("{",0)==0||temp.rfind("}",0)==0){
    curly++;
    }
    count++;
    }
    // final output
    cout << "No. of lines in the given file:"<<count<<"\n";
    cout << "No. of comments in the file:"<<comment<<"\n";
    cout << "No. of curly braces in the file:"<<curly<<"\n";
}
