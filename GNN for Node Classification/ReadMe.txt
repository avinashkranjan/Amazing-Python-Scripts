Description:
a Graph Neural Network (GNN) for node classification on graph-structured data.
 The example uses the PyTorch Geometric library to build and train a GNN on the Cora dataset.
 
Graph Neural Networks (GNNs) are designed to operate on graph-structured data, where nodes represent entities and edges represent relationships between entities. This project showcases a simplified GNN architecture for node classification, helping you understand the fundamentals of GNNs and their application in real-world scenarios.

Dataset: The code uses the Cora dataset, which is a well-known citation network dataset. It consists of scientific publications as nodes in a graph, where edges represent citation relationships between publications. Each node (publication) has a bag-of-words feature representation and a class label indicating its research field.

GNN Architecture:
Node Features -> GCN Layer -> ReLU Activation -> GCN Layer -> Final Node Classifications
 


Input Layer (GCNConv1):

The input layer uses the GCNConv operation to perform the first graph convolution.
The input to this layer is the node features (data.x) and the edge indices (data.edge_index).
The layer applies a graph convolution operation to aggregate information from neighboring nodes.
The activation function used after this layer is the Rectified Linear Unit (ReLU), applied using F.relu.

Hidden Layer (GCNConv2):

The output of the first layer serves as the input to the second layer.
The second layer (GCNConv2) is another graph convolutional layer.
It further aggregates information from neighboring nodes and aims to capture more complex relationships.
Again, the ReLU activation is applied after this layer.

Output Layer:

The output of the hidden layer is passed through a log-softmax activation function to obtain the final node classification probabilities.
The output dimension of this layer is determined by the number of classes (out_channels).


Requirements:

pip install torch torch_geometric matplotlib

