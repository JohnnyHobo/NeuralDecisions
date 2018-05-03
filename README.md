# NeuralDecisions
Making Decisions With Machine Learning

## WHAT!?
Yes. This is a Neural Network using Machine Learning to help you make the best decisions possible.

## Why?
As much as humans like to imagine ourselves to be rational creatures, observations are continually disproving that hypothesis. Why do people respond differently in certain situations? Why do some people choose to do good things, bad things, or things that might harm them? How can we determine how 'rational' a particular individual is? What is the cut off for sanity? And perhaps, most importantly, how can you alter the internal algorithms of individuals to improve their lives? While these questions are well outside the scope of this program's current capabilities, it is my hope that this script, and systems like this can be modified to model the cognitive biases that cause individuals to react in manners that are neither individualisticly nor group beneficial.

## How Does It Work?
First, many thanks to [@shamdasami](https://github.com/shamdasani/shamdasani.github.io) for his ["Build a Neural Network with Python"](https://enlight.nyc/neural-network) tutorial which served as the backbone of this code, if you wish to learn more about neural networks, I highly recommend checking out his work, it's very interesting.

Now, before any programming could begin, I had to figure out what a 'purely rational' decision was, and I realized that perhaps the purest form of rationalization was the old "Pros and Cons" list. From this, I was able to use a boolean value of 1 to represent a pro, and a value of 0 for cons, and of course in making a 'decision' that answer tends to also be in a boolean format (e.g. yes/no). Then I needed to determine what a "pro" or a "con" was, I found that in every instance I could imagine, a "pro" fell into one of the below categories:
* Happiness
* Health
* Wealth
* Ethics
* Legality

And, since a **con** is the antithesis of a **pro**, these would just be the inverse of the other.
This set the framework for the first five "neurons" in my neural network. The *happiness* neuron, *health* neuron, *wealth* neuron, *ethics* neuron, and *legality* neuron. These neurons are then connected to another set of neurons known as the 'hidden layer', this layer will take the inputs of the first five neurons and multiply them by a set of weights. This is then repeated with a second 'hidden layer' before being passed to output. After we get the output, it is rounded to the nearest integer.

Training involves calculating the 'error' - the difference from desired vs actual output -, also known as the 'gradient of descent', then we alter the weights based on that gradient so they are as close as possible to the minimum value of the gradient.

[![Alt text](https://img.youtube.com/vi/IHZwWFHWa-w/0.jpg)](https://www.youtube.com/watch?v=IHZwWFHWa-w)
