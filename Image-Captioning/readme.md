# Image Captioning Model

* Uses pretrained ResNet50 model and Glove embeddings to caption any image

 <pre>
 Model ARCHITECTURE
 img feature -------->  MODEL --> Next word in sequence  ----
 partial sequence --->                                       |
   | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |
 Partial caption ----> RNN 
                           \
                            \ Feed forward network ----> predicted word,next
                            / ending with softmax        in the sequence of
                           /                               partial caption
               Image vector
</pre>

## <a href="https://towardsdatascience.com/image-captioning-with-keras-teaching-computers-to-describe-pictures-c88a46a311b8">Link</a> for this model

## Installation 
    pip install tensorflow
    pip install keras