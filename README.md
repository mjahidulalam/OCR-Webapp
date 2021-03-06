# Character Recognition Webapp

[Click here to checkout the webapp](https://ocr-webapp.herokuapp.com/)

Trained a Convolutional Neural Network using Keras to identify handwritten characters (A-Z) from the MNIST Character dataset.
Used Streamlit to create a webapp that allows users to draw characters and the trained CNN model is used to predict the letter drawn.
I purpose of building this app is to learn how to export a trained model and use it in a production setting with less emphasis on accuracy of the model itself.
Although the model achieved a 99% accuracy on the test set, the dataset has a sampling bias and therefore the model is trained on fewer smaples of certain characters. As a result does not perform as well in the real world.

The CNN model is trained on 297,960 images with a size of 28x28 pixels.

![data](https://raw.githubusercontent.com/mjahidulalam/OCR-Webapp/main/model/sample_data.png "Sample Character Data")

 A summary of the model used is shown below:

_________________________________________________________________
Model: "sequential"

| Layer (type)                                  | Output Shape              | Param #  |   
| --------------------------------------------- | :-----------------------: | -------: |
| conv2d (Conv2D)                               | (None, 26, 26, 32)        | 320      |
| conv2d_1 (Conv2D)                             | (None, 24, 24, 64)        | 18496    | 
| max_pooling2d (MaxPooling2D)                  | (None, 12, 12, 64)        | 0        |                                                                
| batch_normalization (BatchNormalization)      | (None, 12, 12, 64)        | 256      | 
| conv2d_2 (Conv2D)                             | (None, 10, 10, 128)       | 73856    | 
| conv2d_3 (Conv2D)                             | (None, 8, 8, 128)         | 147584   | 
| max_pooling2d_1 (MaxPooling2D)                | (None, 4, 4, 128)         | 0        | 
| batch_normalization_1 (BatchNormalization)    | (None, 4, 4, 128)         | 512      | 
| conv2d_4 (Conv2D)                             | (None, 2, 2, 256)         | 295168   |
| max_pooling2d_2 (MaxPooling2D)                | (None, 1, 1, 256)         | 0        | 
| flatten (Flatten)                             | (None, 256)               | 0        | 
| batch_normalization_2 (BatchNormalization)    | (None, 256)               | 1024     |
| dense (Dense)                                 | (None, 512)               | 131584   | 
| dense_1 (Dense)                               | (None, 26)                | 13338    | 


Total params: 682,138 \
Trainable params: 681,242 \
Non-trainable params: 896
_________________________________________________________________


