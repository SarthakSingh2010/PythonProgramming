class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insertAtEnd(self,val):
        newnode=Node(val)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=newnode
        
    def insertAtBegin(self,val):
        newnode=Node(val)
        if self.head is None:
            self.head=newnode
            return
        newnode.next=self.head
        self.head=newnode
        
    def deleteAtEnd(self):
        if self.head is None:
            return -1
        if self.head.next==None:
            v=self.head.data
            self.head=None
            return v
        temp=self.head
        save=self.head
        while(temp.next!=None):
            save=temp
            temp=temp.next
        v=temp.data
        save.next=None
        return v
        
    def deleteAtBegin(self):
        if self.head is None:
            return -1
        v=self.head.data
        self.head=self.head.next
        return v
    
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=' --> ')
            temp=temp.next
        print('None')
        
if __name__=='__main__':
    ll=LinkedList()
    ll.insertAtEnd(1)
    ll.insertAtEnd(2)
    ll.insertAtEnd(3)
    ll.display()
    ll.insertAtBegin(0)
    ll.display()
    print(ll.deleteAtBegin())
    ll.display()
    print(ll.deleteAtEnd())
    ll.display()