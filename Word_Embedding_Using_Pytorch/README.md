# Script Name
Word Embedding Using Pytorch

## Short description of script

Word Embedding is an approach to represent any word or document in a lower dimensional space. Actually, it is a vectorization method, which vectorizes the word(with multiple vector input) with same or similar meaning in similar representation in vector space. Sometimes, also meaning of the specific word can be approximated while representation. 
If a word vector has 'n' values, then at the time of representation, it will also have 'n' features.

**Goal of word embedding:**
- To reduce dimensionality, as the multidimensional perspective of a word can be removed after vectorization;
- To predict adjacent words of a specific word;
- To capture inter-word semantics

## Setup instructions

Import the necessary libraries:
- torch
- torch.nn
- torch.optim
- torch.nn.functional

Then run all the cells consequtively.

## Detailed explanation of script, if needed

- First context size and embedding dimension (which the domain in vector field) will be initialized.
- A sample text will be processed which will be considered as training data, using this text segment the vectorization scale can be understood.
- We will split the test in training and testing for better model evaluation and generalization purpose.
- (N gram language model) First four segment of the model will be printed in chronological order after the training process is complete.
- Necessary libraries will be imported to implement N gram language model.
- Using the nn module the N gram modeling class will be implemented.
There will be segment of the total class, one initializing the context and embedded(vectorized) dimension and other indicating the forward propagation through the network.
- The error generated through forward propagation will be calculated and using gradient decent the more optimized approach will be implemented.
- The total loss will be prined.
- To test the model and evaluate the generalization approach some vectorized form of letter of printed.
- (CBOW model) n this modelling method, multiple word input vectors will be trained in a single projection and it will be mapped to a specified vectorized output.
First the context dimension and main text(training) will be initialized.
- The text will be considered as array format and the array will be deduplicated. The length which will be used for training purpose will printed.
- Some specific text area will be extracted from the total text segment for training purpose and other will be for testing purpose to achieve better generalized approach.
- The first five extracted segment of the training text will be printed.
- The CBOW class will be implemented and the context vectorizer function will be initialized to vectorize the domain.
- As the text segment was taken as an array format, so some array index will printed to analyze the vectorized form for that index.
- For word processing and measurement purpose in vectorized format nltk and gensim will be used.
- First the libraries will be imported and dataset text file will be processed, then word2vec will be implemented in both the modelling format n gram and CBOW.
- 

## Output
![ss1](https://github.com/sujanrupu/Amazing-Python-Scripts/assets/103595490/de90e434-5f7a-400c-8f34-84ebc85cc261)
![ss2](https://github.com/sujanrupu/Amazing-Python-Scripts/assets/103595490/3e7391b3-7e14-445f-9d9b-d37ae2259191)
![ss3](https://github.com/sujanrupu/Amazing-Python-Scripts/assets/103595490/87965b8b-6eff-4fde-aa95-8a9fedcaeb0e)

## Author(s)

Sujan Ghosh

## Disclaimers, if any

Use this section to mention if any particular disclaimer is required
