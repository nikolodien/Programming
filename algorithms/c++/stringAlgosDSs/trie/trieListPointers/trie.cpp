#include<iostream>
#include<string>

using namespace std;

// Trie node
// Every node contains a string which ends with a '\0'
// right now let's just make it a char
// next points to next node at this level
// and child points to the string/char succeeding this node
typedef struct node{
	char ch;
	struct node *next,*child;
}trieNode;

trieNode* getTrieNode(char ch){
	trieNode* node = new trieNode();
	node->ch=ch;
	node->next=NULL;
	node->child=NULL;
	return node;
}

void addNode(trieNode *root,string str){
	if(str.length()==0){
		return;
	}
	if(root->child!=NULL){
		if(root->child->ch==str[0]){
			str.erase(0,1);
			addNode(root->child,str);
			return;
		}else{
			// Move to the level below
			root=root->child;
			while(root->next!=NULL){
				root=root->next;
				if(root->ch==str[0]){
					str.erase(0,1);
					addNode(root,str);
					return;
				}
			}
			root->next = getTrieNode(str[0]);
			str.erase(0,1);
			addNode(root->next,str);
			return;
		}
	}
	// We couldn't find any node at this or next level
	// containing this char
	// Add the new node as a child of the root
	root->child = getTrieNode(str[0]);
	str.erase(0,1);
	addNode(root->child,str);
}

void display(trieNode *root, int level){
	if(root!=NULL){
		for(int i=0;i<level;i++)
			cout<<" ";
		cout<<root->ch<<endl;
		display(root->child,level+1);	
		display(root->next,level);
	}
}

int main(){
	trieNode* root = getTrieNode('\0');
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		string input;
		cin>>input;
		input.push_back('$');
		addNode(root,input);
	}
	display(root,0);
}
