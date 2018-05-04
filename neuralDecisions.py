#Neural Network "Decision Maker"
import numpy as np

####################################################################################
# This program uses a basic method of evaluating a decision to determine whether a #
# choice is good or not. It is based off of a standard pros/cons list. In general, #
# there are five 'pros' and five 'cons' to all decisions- whether a choice will or #
# will not make you happier, healthier, wealthier- or if it is ethical or legal.   #
# Each of these values are a simple boolean, although more complicated models can  #
# be built on top of this structure to include more or less logical thought forms. #
####################################################################################

# input: x = (happier,healthier,wealthier,ethical,legal)
x = np.array([[0,0,0,0,0],
             [0,0,0,0,1],
             [0,0,0,1,1],
             [0,0,1,1,1],
             [0,1,1,1,1],
             [1,1,1,1,1],
             [1,1,1,1,0],
             [1,1,1,0,0],
             [1,1,0,0,0],
             [1,0,0,0,0]])
# output: (Yes/No)
y = np.array([[0],[0],[0],[1],[1],
              [1],[1],[1],[0],[0]])

class Neural_Network(object):
    def __init__(self):
        #parameters 
        self.inputSize = 5
        self.outputSize = 1
        self.hiddenSize = 6 #=inputSize+outputSize unless you want to rewrite the ENTIRE algorithm.
        #weights
        self.W1 = np.random.randn(self.inputSize, self.hiddenSize)
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize)

    def forward(self, x):
        #forward propagation through our network
        self.z = np.dot(x, self.W1) # dot product of x input and first weights
        self.z2 = self.sigmoid(self.z) #activation function
        self.z3 = np.dot(self.z2, self.W2) # dot product of hidden and second weights
        o = self.sigmoid(self.z3) #final activation function
        return o
        
    def sigmoid (self, s):
        #activation function
        return 1/(1+np.exp(-s))
    
    def sigmoidPrime(self, s):
    #derivative of sigmoid
        return(s * (1 - s))

    def backward(self, x, y, o):
        #backward propogate through network
        self.o_error = y - o # error in output
        self.o_delta = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error
        
        self.z2_error = self.o_delta.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
        self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error

        self.W1 += x.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
        self.W2 = self.W2 + self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights
        
    def train(self, x, y,i):
        i+=1
        o = self.forward(x)
        self.backward(x, y, o)
        
    def saveWeights(self):
        np.save("w1.npy",self.W1)
        np.save("w2.npy",self.W2)

    def predict(self,inputs):
        print "Predicted data based on trained weights: ";
        print "Input (scaled): \n" + str(inputs);
        print "Output: \n" + str(int(np.around(self.forward(inputs))));
        print "How Sure: " +str(int(np.around(self.forward(inputs)*100)))+"%"

NN = Neural_Network()

def initialTraining():
    for i in xrange(500): # trains the NN 500 times
        print "Run: "+str(i)
        print "Input: \n" + str(x)
        print "Actual Output: \n" + str(y)
        print "Predicted Output: \n" + str(np.around(NN.forward(x)))
        print "Loss: \n" + str(np.mean(np.square(y - NN.forward(x)))) # mean sum squared loss
        print "\n"
        NN.train(x, y,0)
    print("Training Complete.")
    while True:
        try:
            a = sanitize(raw_input("Save Weight File? Y/n\n>"))
            if a == 1:
                NN.saveWeights()
            else:
                return
        except ValueError as e:
            print(e)
            continue

def sanitize(i_string):
    o_string = ''
    if i_string in  ['1','Y','YE','YES','YEs','Yes','yes','ye','y','T','TRUE','True','t','true']:
        o_string = int(1)
    elif i_string in ['0','N','NO','No','no','n','F','FALSE','False','false','f','']:
        o_string = int(0)
    else:
        raise ValueError(i_string + " is not a valid answer.\nPlease Use Boolean Logic (e.g. Yes/No;1/0)")
    return o_string

# x = (happier,healthier,wealthier,ethical,legal)
def run():
    #weights file?
    print("Welcome To Noah's Neural Network Decision Maker!")
    title = raw_input("What Is Your Question? \n>")
    while True:
        print(title)
        try:
            #Get inputs, sanitize, and organize in array
            happy = sanitize(raw_input("Will This Make You Happier? \n>"))
            healthy = sanitize(raw_input("Will This Make You Healthier? \n>"))
            wealthy = sanitize(raw_input("Will This Make You Wealthier? \n>"))
            ethic = sanitize(raw_input("Is This Ethical? \n>"))
            legal = sanitize(raw_input("Is This Legal? \n>"))
            inputs = np.array([happy,healthy,wealthy,ethic,legal])
        except ValueError as e:
            print(e)
            continue
        try:
            #Open weights file, if exists, create if not
            NN.W1 = np.load("w1.npy")
            NN.W2 = np.load("w2.npy")
            print("Loaded Okay")
        except Exception, e:
            print(e)
            if e.errno == 2:
                initialTraining()
        break
    print("Now Processing Question: " + title)
    NN.predict(inputs)

while True:
    run()
#initialTraining()
