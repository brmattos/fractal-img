class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newVal):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newVal)
        else:
            t = BinaryTree(newVal)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newVal):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newVal)
        else:
            t = BinaryTree(newVal)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    def __str__(self):
        result = str(self.key)
        if self.leftChild is not None:
            result += '[' + str(self.leftChild) + ']'
        else:
            result += '[]'

        if self.rightChild is not None:
            result += '[' + str(self.rightChild) + ']'
        else:
            result += '[]'
        return result


if __name__ == '__main__':
    r = BinaryTree('a')
    print(r)
    r.insertLeft('b')
    r.insertRight('c')
    print(r)
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    print(r)
    print(r.getRootVal())
    print(r.getLeftChild())
    print(r.getRightChild())
