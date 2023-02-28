#while creating LL we gonna do it in ascending order
#one prog multiple concepts

class Node:
    def __init__(self, data):
        self.data = data
        self.next =None

class LinkedList:
    def __init__(self):
        self.head =None

    def printList(self):
        temp= self.head
        if not temp:
            print('list is empty')
            return
        else:
            print('Start:', end=' ')
        while temp:
            print(temp.data, end=' ->')
            temp=temp.next
        print('end')

    def insert(self,data):
        new_node= Node(data)

        #if the linked list is empty
        if self.head is None:
            self.head= new_node

        #if the data is smaller than the head
        elif self.head.data >= new_node.data:
            new_node.next=self.head
            self.head=new_node

        else:
            #locate the node before the insertion point
            current=self.head
            while current.next and new_node.data > current.next.data:
                current = current.next

                #insertion
            new_node.next=current.next
            current.next =new_node

    def delete(self,key):
        #if list is empty
        if self.head is None:
            print('deletion error: the list is empty')
            return

        #if the key is in head
        if self.head.data ==key:
            self.head =self.head.next
            return

        #find possition of first occurance of the
        current = self.head
        while current:
            if current.data ==key:
                break
            previous= current
            current=current.next

            #if the key value is not found
        if current is None:
                print('deletion error: key not found.')
        else:
                previous.next=current.next

#__name is python special variable
if __name__=='__main__':
    #create an object
    LL=LinkedList()
    print('')
    #insert some nodes
    LL.insert(10)
    LL.insert(12)
    LL.insert(8)
    LL.insert(11)
    LL.insert(10)
    
    LL.printList()
    LL.delete(12)
    LL.delete(8)
    LL.delete(10)
    LL.printList()

    
