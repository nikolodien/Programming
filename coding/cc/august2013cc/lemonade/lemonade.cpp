#include<iostream>
#include<cstdlib>

using namespace std;

#define parent(i) ((i)-1)/2
#define left(i) (2*(i)+1)
#define right(i) (2*(i)+2) 

typedef unsigned int ui;

class room{
	public:
		ui *bc; // capacity of bottles
		ui no; // no of bottles	
};

void maxHeapify(ui *a,ui i,ui length){
	ui lefti=left(i),righti=right(i),largest=i;
	if(lefti<length && a[largest]<a[lefti]){
		largest=lefti;
	}
	if(righti<length && a[largest]<a[righti]){
		largest=righti;
	}
	if(largest!=i){
		// Swap a[i] and a[largest]
		a[i]=a[i]^a[largest];
		a[largest]=a[i]^a[largest];
		a[i]=a[i]^a[largest];
		maxHeapify(a,largest,length);
	}
}

int getMax(ui *a,ui length){
	ui largest=0;
	if(length>0){
		largest=a[0];
		if(length>1){
			a[0]=a[length-1];
			maxHeapify(a,0,length-1);
		}
	}
	return largest;
}

void buildMaxHeap(ui *a,ui length){
	for(ui i=length/2-1;i>=0 && i<length;i--){
		maxHeapify(a,i,length);
	}
}

int main(){
	int T;
	cin>>T;
	while(T-->0){
		int n,m;
		cin>>n>>m;
		int seq[m];
		room rooms[n];
		int volumeSum=0;
		for(int i=0;i<m;i++){
			cin>>seq[i];
		}
		for(int i=0;i<n;i++){
			cin>>rooms[i].no;
			rooms[i].bc = (ui *)malloc(sizeof(ui)*rooms[i].no);
			for(int j=0;j<rooms[i].no;j++){
				cin>>rooms[i].bc[j];
			}
			buildMaxHeap(rooms[i].bc,rooms[i].no);
		}
		for(int i=0;i<m;i++){
			int length = rooms[seq[i]].no;
			int maxVol = getMax(rooms[seq[i]].bc,length);
			volumeSum+=maxVol;
			if(length>0)
				rooms[seq[i]].no = length-1;
		}
		cout<<volumeSum<<endl;
	}
	return 0;
}
