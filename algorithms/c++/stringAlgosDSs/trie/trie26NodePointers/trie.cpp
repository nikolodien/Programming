#include<iostream>
#include<stack>

using namespace std;

#define MAX_NODES 26

typedef struct trieNode{
	int words;
	int prefixes;
	struct trieNode* child[MAX_NODES];
}trieNode;

trieNode* head=NULL;

trieNode* getNode(){
	trieNode* node=new(trieNode);
	node->words=0;
	node->prefixes=0;
	for(int i=0;i<MAX_NODES;i++)
		node->child[i]=NULL;
	return node;
}

void addNode(trieNode* vertex,string word){
	if(!vertex){
		vertex=getNode();
	}
	char firstChar=word[0];
	// We assume that the trie contains only lowercase characters
	trieNode* tn=vertex->child[firstChar-'a'];
	if(!tn){
		tn=getNode();
		vertex->child[firstChar-'a']=tn;
	}
	if(word.length()>1){
		word=word.erase(0,1);
		addNode(tn,word);
	}
}

// We will do a DFS traversal of the tree
void display(trieNode* vertex,int level){
	for(int i=0;i<MAX_NODES;i++){
		trieNode* child=vertex->child[i];
		if(child!=NULL){
			for(int j=1;j<level;j++)
				cout<<" ";
			cout<<char(i+'a')<<endl;
			display(child, level+1);
		}
	}
}

int main(){
	head=getNode();
	string input;
	int T,length;
	cin>>T;
	while(T-->0){
		cin>>input;
		addNode(head,input);
	}
	display(head,1);
	return 0;
}
