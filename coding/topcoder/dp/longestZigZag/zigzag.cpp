#include<iostream>

using namespace std;

int main(){
	int T,L;
	cin>>T;
	while(T-->0){
		cin>>L;
		int a[L],prev[L],sign[L],longest[L];
		for(int i=0;i<L;i++){
			cin>>a[i];
			prev[i]=i;
			sign[i]=0;
			longest[i]=1;
		}
		for(int i=1;i<L;i++){
			for(int j=0;j<i;j++){
				if(sign[j]<0 && a[j]>a[i] && longest[j]+1>longest[i]){
					longest[i]=longest[j]+1;prev[i]=j;sign[i]=1;
				}else if(sign[j]>0 && a[j]<a[i] && longest[j]+1>longest[i]){
					longest[i]=longest[j]+1;prev[i]=j;sign[i]=-1;
				}else if(sign[j]==0){
					longest[i]=longest[j]+1;prev[i]=j;
					sign[i]=(a[j]>a[i])?1:-1;
				}
			}
			//cout<<"prev:"<<prev[i]<<",sign:"<<sign[i]<<",longest:"<<longest[i]<<endl;
		}
		cout<<"longest sequence length:"<<longest[L-1]<<endl;
	}
	return 0;
}
