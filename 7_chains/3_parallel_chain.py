import sys,os
sys.path.append(os.path.abspath(".."))
from load_model import *
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel 

model1 = Tiny_llm()

model2 = Tiny_llm()

prompt1 = PromptTemplate(
    template = 'Generate a short and simple notes from the following text. \n {text}',
    input_variable = ['text']
)

prompt2 = PromptTemplate(
    template = 'Generate 5 short Question and Answer from the following text \n {text}',
    input_variable = ['text']
)

prompt3 = PromptTemplate(
    template = 'Merge the provided notes and quiz into a single document \n -> {notes} ans {quiz}',
    input_variable = ['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """Deep Learning Tutorial
Last Updated : 16 Dec, 2024
Deep Learning tutorial covers the basics and more advanced topics, making it perfect for beginners and those with experience. Whether you're just starting or looking to expand your knowledge, this guide makes it easy to learn about the different technologies of Deep Learning.

Deep Learning is a branch of Artificial Intelligence (AI) that enables machines to learn from large amounts of data.
It uses neural networks with many layers to automatically find patterns and make predictions.
It is very useful for tasks like image recognition, language translation, and speech processing.
Deep learning models learn directly from data, without the need for manual feature extraction.
Popular applications of Deep Learning include self-driving cars, chatbots, medical image analysis, and recommendation systems.
Introduction to Neural Networks
Neural Networks are fundamentals of deep learning inspired by human brain. It consists of layers of interconnected nodes, or "neurons," each designed to perform specific calculations. These nodes receive input data, process it through various mathematical functions, and pass the output to subsequent layers.

Biological Neurons vs Artificial Neurons
Single Layer Perceptron
Multi-Layer Perceptron
Artificial Neural Networks (ANNs)
Basic Components of Neural Networks
The basic components of neural network are:

Neurons
Layers in Neural Networks
Weights and Biases
Forward Propagation
Activation Functions
Loss Functions
Backpropagation
Learning Rate
Optimization Algorithm in Deep Learning
Optimization algorithms in deep learning are used to minimize the loss function by adjusting the weights and biases of the model. The most common ones are:

Gradient Descent
Stochastic Gradient Descent (SGD)
Mini-batch Gradient Descent
RMSprop (Root Mean Square Propagation)
Adam (Adaptive Moment Estimation)
Convolutional Neural Networks (CNNs)
Convolutional Neural Networks (CNNs) are a class of deep neural networks that are designed for processing grid-like data, such as images. They use convolutional layers to automatically detect patterns like edges, textures, and shapes in the data.

Basics of Digital Image Processing
Need for CNN
Strides
Padding
Convolutional Layers
Pooling Layers
Fully Connected Layers
Batch Normalization
Backpropagation in CNNs
To learn about the implementation, you can explore the following articles:

CNN based Image Classification using PyTorch 
CNN based Images Classification using TensorFlow 
CNN Based Architectures
There are various architectures in CNNs that have been developed for specific kinds of problems, such as:

LeNet-5
AlexNet
VGG-16 Network
VGG-19 Network
GoogLeNet/Inception
ResNet (Residual Network)
MobileNet
Recurrent Neural Networks (RNNs)
Recurrent Neural Networks (RNNs) are a class of neural networks that are used for modeling sequence data such as time series or natural language.

Vanishing Gradient and Exploding Gradient Problem
How RNN Differs from Feedforward Neural Networks
Backpropagation Through Time (BPTT)
Types of Recurrent Neural Networks
Bidirectional RNNs
Long Short-Term Memory (LSTM)
Bidirectional Long Short-Term Memory (Bi-LSTM)
Gated Recurrent Units (GRU)
Generative Models in Deep Learning
Generative models generate new data that resembles the training data. The key types of generative models include:

Generative Adversarial Networks (GANs)
Autoencoders
Restricted Boltzmann Machines (RBMs)
Variants of Generative Adversarial Networks (GANs)
GANs consists of two neural networks - the generators and the discriminator that compete with each other in a game like framework. The variants of GANs include the following:

Deep Convolutional GAN (DCGAN)
Conditional GAN (cGAN)
Cycle-Consistent GAN (CycleGAN)
Super-Resolution GAN (SRGAN)
Wasserstein GAN (WGAN)
StyleGAN
Types of Autoencoders
Autoencoders are neural networks used for unsupervised learning that learns to compress and reconstruct data. There are different types of autoencoders that serve different purpose such as noise reduction, generative modelling and feature learning.

Sparse Autoencoder
Denoising Autoencoder
Undercomplete Autoencoder
Contractive Autoencoder
Convolutional Autoencoder
Variational Autoencoder
Deep Reinforcement Learning (DRL)
Deep Reinforcement Learning combines the representation learning power of deep learning with the decision-making ability of reinforcement learning. It enables agents to learn optimal behaviors in complex environments through trial and error, using high-dimensional sensory inputs.

Reinforcement Learning
Markov Decision Processes
Function Approximation
Key Algorithms in Deep Reinforcement Learning
Deep Q-Networks (DQN)
REINFORCE
Actor-Critic Methods
Proximal Policy Optimization (PPO)
Application of Deep Learning
Image Recognition: Identifying objects, faces, and scenes in photos and videos.
Natural Language Processing (NLP): Powering language translation, chatbots, and sentiment analysis.
Speech Recognition: Converting spoken language into text for virtual assistants like Siri and Alexa.
Medical Diagnostics: Detecting diseases from X-rays, MRIs, and other medical scans.
Recommendation Systems: Personalizing suggestions for movies, music, and shopping.
Autonomous Vehicles: Enabling self-driving cars to recognize objects and make driving decisions.
Fraud Detection: Identifying unusual patterns in financial transactions and preventing fraud.
Gaming: Enhancing AI in games and creating realistic environments in virtual reality.
Predictive Analytics: Forecasting customer behavior, stock prices, and weather trends.
Generative Models: Creating realistic images, deepfake videos, and AI-generated art.
Robotics: Automating industrial tasks and powering intelligent drones.
Customer Support: Enhancing chatbots for instant and intelligent customer interactions."""

result = chain.invoke({'text':text})

print(result)

# chain.get_graph().print_ascii()