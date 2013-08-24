#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define MIN(X,Y) ((X)<(Y)?(X):(Y))

typedef struct visitedStore visitedStore;
typedef visitedStore* visitedStoreptr;

struct visitedStore{
	int store;
	int time;
	visitedStoreptr next;
};

visitedStoreptr head=NULL,tail=NULL;

typedef struct store store;

struct store{
	int srno,x,y,a,b,c;
};

visitedStoreptr getNode(int store,int time){
	visitedStoreptr node=(visitedStoreptr)malloc(sizeof(visitedStore));
	node->next=NULL;
	node->store=store;
	node->time=time;
	return node;
}

void insert(int store,int time){
	visitedStoreptr node=getNode(store,time);
	if(head==NULL){
		head=node;
		tail=node;
	}else{
		tail->next=node;
		tail=node;
	}
}

int listcontains(int store){
	visitedStoreptr node=head;
	while(node!=NULL){
		if(node->store==store){
			return 1;
		}
		node=node->next;
	}
	return 0;
}

void displayList(){
	visitedStoreptr temp=head;
	while(temp!=NULL){
		printf("%d %d\n",temp->store,temp->time);
		temp=temp->next;
	}
}

void clearList(){
	visitedStoreptr temp=head;
	while(temp!=NULL){
		visitedStoreptr next=temp->next;
		free(temp);
		temp=next;
	}
	head=NULL;
}

void displayStores(store* ptr,int n){
	while(n-->0){
		printf("%d,%d,%d,%d,%d\n",ptr->x,ptr->y,ptr->a,ptr->b,ptr->c);
		ptr++;
	}
}

int main(){
	int testcases;
	int testcase=0;
	scanf("%d",&testcases);
	int t=testcases;
	while(testcase++<testcases){
		//printf("Case #%d of %d\n",testcase,testcases);
		int n,m;
		scanf("%d%d",&n,&m);
		store stores[n];
		int i=0;
		for(;i<n;i++){
			int x,y,a,b,c;
			scanf("%d%d%d%d%d",&x,&y,&a,&b,&c);
			stores[i].srno=i+1;
			stores[i].x=x;
			stores[i].y=y;
			stores[i].a=a;
			stores[i].b=b;
			stores[i].c=c;
		}
		int p,q;
		scanf("%d%d",&p,&q);
		int p1=p,q1=q;
		// At any instant, find out which store will give max of
		// a-b*time and has highest c value
		int time=0;
		while(time<=m){
			// printf("Current Position:(%d,%d)\n",p1,q1);
			// Manhattan distance to a store will give the amount of
			// time required to reach that store
			int j=0,index=-1,maxrs=0,maxcs=0,distance=0,distanceToHome=0;
			for(;j<n;j++){
				int manhattan=abs(stores[j].x-p1)+abs(stores[j].y-q1);
				// printf("manhattan=%d\n",manhattan);
				testcases=testcases;
				int rs=stores[j].a-stores[j].b*(time+manhattan);
				int distanceFromHome=abs(stores[j].x-p)+abs(stores[j].y-q);
				int cs=stores[j].b*MIN(stores[j].c,m-distanceFromHome-time-manhattan);
				// printf("rs=%d,cs=%d\n",rs,cs);
				if((rs>maxrs)?1:(cs>maxcs && cs<=rs)?1:0){
					// printf("distanceFromHome=%d\n",distanceFromHome);
					if(time+manhattan+1+distanceFromHome<=m && !listcontains(j+1)){
						maxrs=rs;
						maxcs=cs;
						index=j;
						distance=manhattan;
						distanceToHome=distanceFromHome;
					}
				}
			}
			if(index==-1)
				break;
			//printf("store selected = %d\n",index+1);
			p1=stores[index].x;
			q1=stores[index].y;
			time=time+distance;
			//printf("%d %d %d\n",time,m-distanceToHome-time,stores[index].c);
			insert(stores[index].srno,MIN(m-distanceToHome-time,stores[index].c));
			time=time+MIN(m-distanceToHome-time,stores[index].c);
		}
		printf("%d\n",testcase);
		displayList();
		clearList();
		printf("0 0\n");
	}
}
