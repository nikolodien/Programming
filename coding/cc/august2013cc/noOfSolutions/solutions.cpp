#include<iostream>
#include<math.h>

using namespace std;

#define MAX 1000000007

typedef unsigned long long ull;

ull sol(ull upper,ull d,ull m,ull N){
	ull sum=0;
	for(ull x=0L;x<=upper;x++)
		for(ull y=0L;y<=upper;y++)
			for(ull z=0L;z<=upper;z++){
				if(x<=upper && y<=upper && z<=upper){
					ull eval = ull(pow(x,d) + pow(y,d) + pow(z,d));
					if(eval%N == m){
						sum++;
						sum=sum%MAX;
					}
				}
			}
	return sum;
}

int main(){
	int T;
	cin>>T;
	while(T-->0){
		ull upper,d,m,N;
		cin>>upper>>d>>m>>N;
		ull solution=sol(upper,d,m,N);
		cout<<solution<<endl;
	}
}
