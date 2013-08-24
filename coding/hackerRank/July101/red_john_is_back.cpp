#include<iostream>

using namespace std;

int main(){
	int T,N;
	cin>>T;
	while(T>0){
		cin>>N;
		if(N<4){
			cout<<N-1<<endl;
		}else{
			int M=0;
			for(int i=1;i<=N/4;i++){
				M+=(N-(i*4)+1);
			}
			M++; // for all vertical
			int P=2;
			for(int i=5;i<=M;i++){
				bool prime=true;
				for(int j=2;j<i/2;j++){
					if(i%j==0){
						prime=false;
						break;
					}	
				}
				if(prime)
					P++;
			}
			cout<<P<<endl;
		}
		T--;
	}
}
