#include<iostream>
#include<cstdlib>

using namespace std;

typedef struct generic generic;

struct generic{
	void* data;
	int size;
	struct generic* next;
};

generic *head,*tail;

generic* getNode(void* data,int size){
	generic* node = (generic *)malloc(sizeof(generic));
	node->data = data;
	node->size = size;
	node->next = NULL;
	return node;
}

void add(void *data, int size){
	if(head!=NULL){
		tail->next=getNode(data,size);
		tail=tail->next;
	}else{
		head=getNode(data,size);
		tail=head;
	}
}

void display(){
	while(head!=NULL){
		switch(head->size){
			case 1:
				cout<<*(char *)head->data<<endl;
				break;
			case 4:
				cout<<*(int *)head->data<<endl;
				break;
			case 8:
				cout<<*(float *)head->data<<endl;
		}
		head=head->next;
	}
}

int main(){
	int T;
	cin>>T;
	int size;
	void *data;
	while(T--){
		cin>>size;
		switch(size){
			case 1:
				data = malloc(size);
				char ch;
				cin>>ch;
				*(char *)data = ch;
				break;
			case 4:
				data = malloc(size);
				int number;
				cin>>number;
				*(int *)data = number;
				break;
			case 8:
				data = malloc(size);
				float dnumber;
				cin>>dnumber;
				*(float *)data = dnumber;
				break;
		}
		add(data,size);
	}
	display();
	return 0;
}
