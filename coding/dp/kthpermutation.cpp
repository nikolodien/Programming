#include<string>
#include<stack>
#include<iostream>

using namespace std;

class Solution {
public:
    string getPermutation(int n, int k) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        bool taken[n+1];
        int no=0;
        for(int i=1;i<=n;i++)taken[i]=false;
        for(int i=1;i<=n;i++){
            taken[i]=true;
			stack<int> q;
			q.push(i);
            string kth=getpermutation1(n,k,taken,q,&no);
            if(kth.length()>0)return kth;
			q.pop();
            taken[i]=false;
        }
        return "";
    }
    
    string getpermutation1(int n,int k,bool taken[],stack<int> q,int *no){
		if(q.size()==n){
			*no = *no + 1;
			if(*no==k){
				return getString(q);
			}else
				return "";
		}
        for(int i=1;i<=n;i++){
            if(!taken[i]){
                taken[i]=true;
                q.push(i);
                string kth=getpermutation1(n,k,taken,q,no);
                if(kth.length()>0)return kth;
                q.pop();
                taken[i]=false;
            }
        }
        return "";
    }
    string getString(stack<int> s){
		stack<int> s1;
		while(s.size()>0){
				s1.push(s.top());
				s.pop();
		}
		string ss="";
		while(s1.size()>0){
			ss+=(48+s1.top());
			s1.pop();
		}
		return ss;
	}
};

int main(){
	Solution sl;
	cout<<sl.getPermutation(3,4);
	return 0;
}
