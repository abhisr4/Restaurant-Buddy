#include<bits/stdc++.h>
using namespace std;
#define MAX 100
int main()
{
    freopen("outfile.txt","r",stdin);
    freopen("result.txt","w",stdout);
    vector<vector<double>> v; //to store the location coordinates
    for(int i=0;i<6913;i++){
        double n,x,y; //n=location id(not required for this computatiion)
        //x=lat, y=long
        cin>>n>>x>>y;
        vector<double> temp={x,y};
        v.push_back(temp);
    }

    vector<vector<double>> distanceMatrix(v.size(),vector<double>(v.size())); //make the distance matrix
    vector<vector<int>> result;
    for(int i=0;i<v.size();i++){
        priority_queue<pair<double,int>> pq;
        for(int j=0;j<v.size();j++){
            double distance_x=v[i][0]-v[j][0];
            double distance_y=v[i][1]-v[j][1];
            double distance=sqrt(pow(distance_x,2)+pow(distance_y,2));
            if(distance!=0){
                pq.push(make_pair(distance,j));
                if(pq.size()>MAX){
                    pq.pop();
                }
            }
        }
        vector<int> temp;
        while(pq.size()>0){
            temp.push_back(pq.top().second);
            pq.pop();
        }
        result.push_back(temp);
    }
    for(int i=0;i<result.size();i++){
        for(int j=0;j<result[i].size();j++){
            cout<<result[i][j]<<" ";
        }
        cout<<endl;
    }
}