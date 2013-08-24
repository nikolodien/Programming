#include<stdio.h>
#include<stdlib.h>

typedef struct node node;
typedef struct node* nodeptr;

struct node{
	int a;
	nodeptr next;
};

nodeptr head=NULL;

// Function to get a new node
nodeptr get_node(int key){
	nodeptr temp=(nodeptr)malloc(sizeof(node));
	temp->a=key;
	temp->next=NULL;
}


// Append to linked list
void add(int key){
	nodeptr node=get_node(key);
	if(head==NULL){
		head=node;
	}else{
		nodeptr temp=head;
		while(temp->next!=NULL){
			temp=temp->next;
		}
		temp->next=node;
	}
}

// Insert into linked list 
void insert(int key, int pos){
	nodeptr node=get_node(key);
	if(head==NULL){
		head=node;
	}else{
		nodeptr temp=head;
		while(temp->next!=NULL && --pos>1){
			temp=temp->next;
		}
		if(temp->next==NULL){
			temp->next=node;
		}else{
			nodeptr temp1=temp->next;
			temp->next=node;
			node->next=temp1;
		}
	}
}

// Delete from linked list
void delete(int pos){
	if(head!=NULL && pos>0){
		if(pos==1){
			nodeptr temp=head;
			head=head->next;
			free(temp);
			return;
		}
		nodeptr temp=head;
		while(temp->next!=NULL && --pos>1){
			temp=temp->next;	
		}
		// Now we have to delete temp
		nodeptr temp1=temp->next;
		if(temp1!=NULL){
			// Make the node's next the previous node's next
			temp->next=temp1->next;
			// Free the space allocated for this node
			free(temp1);
		}
	}
}

// Reverse linked list
void reverse(){
	if(head!=NULL){
		nodeptr p=head,q=p->next,r;
		head->next=NULL;
		while(q!=NULL){
			r=q->next;
			q->next=p;
			p=q;
			q=r;
		}
		// Update the head
		head=p;
	}
}

// Reverse linked list recursively
void rec_reverse(nodeptr node){
	if(node->next!=NULL){
		rec_reverse(node->next);
		node->next->next=node;
		node->next=NULL;
	}else{
		head=node;
	}
}

// Pairwise reverse
nodeptr pair_reverse(nodeptr head){
	if(head!=NULL){
		nodeptr p,q,r;
		p=head;
		q=head->next;
		if(q==NULL){
			return p;
		}else{
			r=q->next;
			q->next=p;
			p->next=pair_reverse(r);
			return q;
		}
	}else{
		return NULL;
	}
}

// Display linked list
void display(){
	if(head!=NULL){
		printf("%d",head->a);
	}else{
		return;
	}
	nodeptr temp=head->next;
	while(temp!=NULL){
		printf("-->%d",temp->a);
		temp=temp->next;
	}
	printf("\n");
}

int main(int argc, char* argv){
	insert(1,1);display();
	insert(2,1);display();
	insert(100,1);display();
	reverse();display();
	insert(2,3);display();
	insert(4,4);display();
	insert(5,5);display();
	printf("Recursively reverse\n");
	rec_reverse(head);display();
	printf("Pairwise reverse\n");
	head=pair_reverse(head);display();
	return 0;
}
