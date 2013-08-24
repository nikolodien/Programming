#include<iostream>
#include<string>

using namespace std;

void insert(int*,int*,int);

int* insertion_sort(int *a,int size){
	if(size!=1){
		insert(a,insertion_sort(a+1,size-1),size-1);
	}
	return a;
}

void insert(int *element,int *a,int size){
	if(size>0 && *element>*a){
		int temp=*element;
		*element=*a;
		*a=temp;
		insert(a,a+1,size-1);
	}
}

int main(){
	int size;
	cout<<"Enter size\n";
	cin>>size;
	int a[size];
	cout<<"Enter array\n";
	for(int i=0;i<size;i++)
		cin>>a[i];
	insertion_sort(a,size);
	cout<<"Sorted array\n";
	for(int i=0;i<size;i++)
		cout<<a[i]<<" ";
	cout<<endl;
	return 0;
}
