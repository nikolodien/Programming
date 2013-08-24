#include<iostream>
#include<cmath>
#include<cstring>

using namespace std;

#define MAX_INT 5001

int rem;

long bananas(int index,bool* m,int M){
	// First count how many on left are true
	long count=0;
	for(int i=index-1;i>=0;i--){
		if(m[i]) count++;
		else break;
	}
	// Now count how many on right are true
	for(int i=index+1;i<M;i++){
		if(m[i]) count++;
		else break;
	}	
	m[index]=false;
	return count;
}

long sol(int M,int Z,bool* m,bool *z, int* r,int low, int high){
	if(rem!=0 && low<high and high>0){
		// find which monkey is closest to the middle
		int mid=(low+high+1)/2,closest=MAX_INT,index=-1;
		// cout<<mid<<" "<<low<<" "<<high<<endl;
		for(int i=0;i<Z;i++){
			if(z[i]){
				int diff=(int)abs(double(r[i]-mid));
				if(diff<closest){
					closest=diff;
					index=i;
				}
			}
		}
		// Now remove that monkey and add to the count
		rem--;
		z[index]=false;
		// cout<<"Monkey no. "<<r[index]<<endl;
		return bananas(r[index]-1,m,M)+sol(M,Z,m,z,r,low,mid-1)+sol(M,Z,m,z,r,mid+1,high);
	}else{
		return 0;
	}
}

int main(){
	int N;
	cin>>N;
	while(N--){
		int M,Z;
		cin>>M>>Z;
		bool monkeys[M],z[Z];
		memset(monkeys,true,M);
		memset(z,true,Z);
		int removal[Z];
		for(int i=0;i<Z;i++){
			cin>>removal[i];
		}
		rem=Z;
		cout<<sol(M,Z,monkeys,z,removal,1,M)<<endl;
	}
}
