#include<iostream>
#include<string>
#include<map>

using namespace std;

int main(){
	int T;
	string s,a,b;
	cin>>T;
	while(T>0){
		cin>>s;
		int length=s.length();
		int mismatches=0;
		if(!(length%2)){
			// Proceed only if length is even
			a=s.substr(0,length/2);
			b=s.substr(length/2,length);
			map<char,int> charmap;
			for(int i=0;i<a.length();i++){
				int count=(*charmap.find(a[i])).second;
				charmap[a[i]]=count+1;
			}
			for(int i=0;i<b.length();i++){
					int count=(*charmap.find(b[i])).second;
				if(count<=0)
					mismatches++;
				else
					charmap[b[i]]=count-1;
			}
			
		}else{
			mismatches=-1;
		}
		T--;
		cout<<mismatches<<endl;
	}
}
