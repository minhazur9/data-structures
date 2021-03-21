class Node {
    constructor(value) {
        this.left = null;
        this.value = value;
        this.right = null;
    }

    insert(value) {
        if (value < this.value) {
            if (!this.left) this.left = new Node(value);
            else this.left.insert(value)
        }
        else {
            if (!this.right) this.right = new Node(value);
            else this.right.insert(value)
        }
    }

    inOrderSearch(value) {
        if (value < this.value) {
            if (this.left)  this.left.inOrderSearch(value)
            else return false
        }
        else if (value === this.value) return this;
        else {
            if (this.right) this.right.inOrderSearch(value)
            else return false
        }
    }

    inOrderPrint() {
        if (this.left) this.left.inOrderPrint();
        console.log(this.value);
        if (this.right) this.right.inOrderPrint();
    }

    preOrderPrint() {
        console.log(this.value);
        if (this.left) this.left.preOrderPrint()
        if (this.right) this.right.preOrderPrint()
    }

    postOrderPrint() {
        if (this.left) this.left.postOrderPrint()
        if (this.right) this.right.postOrderPrint()
        console.log(this.value)
    }

    invert() {
        if (this.left) this.left.invert();
        if (this.right) this.right.invert();
        const leftVal = this.left;
        this.left = this.right;
        this.right = leftVal;

    }
}

const node = new Node(5);
node.insert(3)
node.insert(7)
node.insert(1)
node.insert(0)
node.insert(2)
node.insert(10)
node.insert(9)
node.insert(12)
node.invert()
node.inOrderPrint()