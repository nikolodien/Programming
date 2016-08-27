/*Department of Computer Engineering has student's club named 'Pinnacle Club'.
Students of Second, third and final year of department can be granted membership on request.
Similarly one may cancel the membership of club. First node is reserved for president of club
and last node is reserved for secretary of club. Write C++ program to maintain club member‘s
information using singly linked list. Store student PRN and Name. Write functions to
a) Add and delete the members as well as president or even secretary.
b) Compute total number of members of club
c) Display members
d) Display list in reverse order using recursion
e) Two linked lists exists for two divisions. Concatenate two lists. */



#include <iostream>
using namespace std;

/*
Points to a node of the list
*/
class pinnacle
{
	public:
		string name; // name of the student
		string prn;	// prn of the student
		pinnacle* next;	// pointer to the next element of the list
};

class SLL
{
	public:
		pinnacle *head,*last; // pointers to the first and last element of the list
		// Function declarations
		void create();
		void display();
		void insert(string, string);
		void deleete();
		void count();
		void reverse();
		void concatenate();
		SLL()
		{
			// Initialize head and last to NULL
			head=last=NULL;
		}

};

int main()
{
	// Create a next instance of the list
	SLL list;
	// temporary pointer to a list node or node of type pinnacle
	pinnacle* temp;
	// variable to store the user choice input
	int choice=0;
	list.create();
	bool quit = false;
	// Infinite loop. Will execute till the user enters quit(7)
	while(true){
		cout<<"Menu"<<endl;
		cout<<" 1. Insert \n 2. Delete \n 3. Display \n 4. Count \n 5. Reverse \n 6. Concatenate \n 7. Quit\n";
		cout<<"Enter your choice:";cin>>choice;
		switch(choice)
		{
			case 1:
				list.create();
				break;
			case 2:
				list.deleete();
				break;
			case 3:
				list.display();
				break;
			case 4:
				list.count();
				break;
			case 5:
				list.reverse();
				break;
			case 6:
				list.concatenate();
				break;
			case 7:
				quit = true;
				break;
			default:
				cout<<"Wrong input"<<endl;
		}
		// Exit the loop 
		if(quit)break;
	}
	return 0;
}

void SLL::create()
{
	// Create a new node of type pinnacle and inserts it at the end of the list
	pinnacle* temp;
	string name,prn;
	cout<< "Enter the name" << endl;
	cin>>name;
	cout<<"Enter the PRN number"<<endl;
	cin>>prn;
	insert(name,prn);
}

void SLL::display()
{
	// displays the entire linked list
	// Start from the head
	pinnacle* temp=head;
	cout<<"Linked list is \n";
	// while temp != NULL, continue displaying the students
	while(temp!=NULL)
	{
		cout<<"("<<temp->name<<","<<temp->prn<<")"<<"->";
		// Get the next elemnt using the next pointer of the node
		temp=temp->next;
	}
	cout<<"NULL"<<endl;
}

void SLL::insert(string name, string prn)
{
	pinnacle* temp=new pinnacle;
	temp->name=name;
	temp->prn=prn;
	temp->next=NULL;
	if(head==NULL)
	{
		// If head==NULL, set head and last to the node
		head=last=temp;
	}
	else
	{
		// else, add the node to the end of the list
		// For this, we just update the next pointer of the last node
		// and set the last node to temp
		last->next=temp;
		last=temp;
	}
}

void SLL::deleete()
{
	string name,prn;
	cout<< "Enter the name" << endl;
	cin>>name;
	cout<<"Enter the PRN number"<<endl;
	cin>>prn;
	pinnacle *temp = head, *prev = NULL;
	// We need to find the node with the name and prn as the user entered to delete the node
	// But this a singly linked list, so we also need a prev pointer, so that we can update 
	// the next pointer of the prev node of the node to be deleted.

	/*
		To understand this,

		Consider the following linked list,

		(a,1)->(b,2)->(c,3)->NULL

		let us assume that the user enters (b,2)

		In the loop, we get to (b,2) but to delete (b,2) we need to update the next pointer of
		(a,1) to (c,3) to give the following list,

		(a,1)->(c,3)->NULL

		This is only possible if we save a reference to the prev node of (b,2). Hence, we always
		save the prev node of node while looping
	*/
	while(temp!=NULL){
		if(temp->name==name && temp->prn==prn){
			break;
		}
		prev=temp;
		temp=temp->next;
	}
	if(prev==NULL){
		// It means that we have to delete the head
		// In that case, change the head to point to the next element
		head = temp->next;
		if(head==NULL){
			// This means there was only one element
			// So, also set the last pointer to NULL
			last=NULL;
		}
	}else{
		// In this case, just change the next pointer of prev element
		prev->next = temp->next;
		// And the delete the temp element
		delete temp;
	}
}

void SLL::count(){
	cout<<"Not implemented"<<endl;
}

void SLL::reverse(){
	cout<<"Not implemented"<<endl;
}

void SLL::concatenate(){
	cout<<"Not implemented"<<endl;
}