class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class SLinkedList {
    constructor() {
        this.head = null
    }

    insert(value) {
        const newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;
    }

    listAll() {
        let node = this.head;
        while (node) {
            console.log(node.value);
            node = node.next;
        }
    }

    reverse() {
        let previous = null;
        let node = this.head;
        while (node) {
            const nextNode = node.next;
            node.next = previous;
            previous = node;
            node = nextNode;
        }
        this.head = previous;
    }

    size() {
        let node = this.head;
        let size = 0;
        while (node) {
            node = node.next
            size++
        }
        return size
    }
}
