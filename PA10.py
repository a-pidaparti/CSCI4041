import traceback

#huffman_encode: Takes in a single String input_string, which is
# the string to be encoded.  Computes the optimal binary encoding
# of the string and encodes it, returning a String of 0s and 1s.
# This is not an actual Python binary string, just a normal String
# that happens to contain only 0s and 1s.
def sortList(nodeList):     #basic insertion sort based on frequency of characters

    for i in range(1, len(nodeList)):

        key = nodeList[i]

        j = i-1
        while j >= 0 and key.freq < nodeList[j].freq :
                nodeList[j + 1] = nodeList[j]
                j -= 1
        nodeList[j + 1] = key

def combineSmallest(list):      #takes smallest (first 2) 2 objects and combines their characters and frequencies
    left = list[1]
    right = list[0]
    if list[0].freq <= list[1].freq:    #if freq of left is less than or equal to freq of right
        left = list[0]
        right = list[1]

    new = Node(left,right,left.ch + right.ch, left.freq + right.freq)   #adds characters to make super string, adds freq to make super freq
    outList = list[2:len(list)] #slice of list excluding first two nodes that were combined to make supernode
    outList.append(new)
    return outList

def encodeChar(node, input_char):
    outString = ""
    cur = node
    while cur.ch != input_char: #repeat until the current node has the desired character
        if input_char in cur.left.ch:   #determines if go left or go right and appends appropriate character (1 or 0)
            cur = cur.left
            outString += "0"
        elif input_char in cur.right.ch:
            cur = cur.right
            outString += "1"
        else:
            print("Char not found in given tree within function encodeChar")
            return
    return outString

def huffman_encode(input_string):
    freqDict = {}
    for ch in input_string:     #put all char into dictionary
        if ch in freqDict.keys():
            freqDict[ch] = freqDict[ch] + 1
        else:
            freqDict[ch] = 1

    nodeList = []
    for key in freqDict.keys():     #create list of nodes based on char and freq
        nodeList.append(Node(None, None, key, freqDict[key]))

    while len(nodeList) > 1:    #sort node list and combine smalles until only a single supernode
        sortList(nodeList)
        nodeList = combineSmallest(nodeList)
    root = nodeList[0]

    outString = ""
    for ch in input_string:     #encodes each character and appends to the returned string
        outString += encodeChar(root,ch)

    return outString

class Node:
    def __init__(self, left, right, ch, freq):
        self.left = left
        self.right = right
        self.ch = ch
        self.freq = freq



#  DO NOT EDIT BELOW THIS LINE

tests = ['message0.txt','message1.txt','message2.txt','message3.txt',
         'message4.txt','message5.txt']
correct = ['message0encoded.txt','message1encoded.txt',
           'message2encoded.txt','message3encoded.txt',
           'message4encoded.txt','message5encoded.txt']


#Run test cases, check whether encoding correct
count = 0

try:
    for i in range(len(tests)):
        ("\n---------------------------------------\n")
        print("TEST #",i+1)
        print("Reading message from:",tests[i])
        fp = open(tests[i])
        message = fp.read()
        fp.close()
        print("Reading encoded message from:",correct[i])
        fp2 = open(correct[i])
        encoded = fp2.read()
        fp2.close()
        output = huffman_encode(message)
        if i < 5:
            print("Running: huffman_encode on '"+message+"'\n")
            print("Expected:",encoded,"\nGot     :",output)
        assert encoded == output, "Encoding incorrect!"
        print("Test Passed!\n")
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)
except Exception:
    print("\nFAIL: ",traceback.format_exc())


print(count,"out of",len(tests),"tests passed.")
