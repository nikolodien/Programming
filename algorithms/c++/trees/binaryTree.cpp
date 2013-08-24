#include<iostream>

using namespace std;

typedef struct node{
	int data;
	struct node *left;
	struct node *right;
}node;

node* getNode(int data){
	node* temp = new node();
	temp->data = data;
	temp->left = NULL;
	temp->right = NULL;
}

void addNode(node** root,int data){
	if(*root!=NULL)
		if((*root)->data>=data)
			addNode(&((*root)->left),data);
		else
			addNode(&((*root)->right),data);
	else
		*root = getNode(data);
}

node* lca(node* root,int int1,int int2){
	if(root){
		if(root->data >= int1 && root->data <=int2)
			return root;
		if(root->data < int1)
			return lca(root->right,int1,int2);
		else
			return lca(root->left,int1,int2);
	}else
		return NULL;
}

// swap the structure of the tree
void swap(node* root){
	
}

// Inorder traversal
void display(node* root,int level){
	if(root){
		display(root->right,level+1);
		for(int i=0;i<level;i++)
			cout<<"\t";
		cout<<root->data<<endl;
		display(root->left,level+1);
	}
}

int main(){
	int T;
	cin>>T;
	int num;
	node *root = NULL;
	while(T-->0){
		cin>>num;
		addNode(&root,num);
	}
	display(root,0);
	node* lcaNode = lca(root,2,3);
	if(lcaNode)
		cout<<lcaNode->data<<endl;
}
