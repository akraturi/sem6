#include <bits/stdc++.h>
using namespace std;
bool visited[1000];
vector<int> graph[1000]];
bool dfs(int u,int v){
      vector<int> paths;
      
      visited[u]=true;
      for(int i=0;i<graph[u].size();i++){
         
         bool result;
         if(!visited[graph[u][i]]){
             
            
           if(graph[u][i]==v){
             result = true;
           }
           else
            {
             result = dfs(graph[u][i]);
            }
            if(result){
             cout << u << " ";
            }
         } 
      }
      
      if(reached_destination)
      {  
         cout << "Path to destinated state is"
      }
      
}
int main(){
    int n;
    cout << "No. of states-->\n";
    cin >> n;
    int u,v;
    cout << "Enter the states between which there is a direct route e.g- (state1,state2)\n";
    for(int i=0;i<n;i++){
     cin >> u >> v;
     graph[u].push_back(v);
     graph[v].push_back(u);
    }
    cout << "Enter the initial state and goal state\n";
    cin >> u >> v;
    // apply dfs from goal to initial state 
    dfs(u,v);
    

}
