# Neural Machine Translation

## Introduction

In this project, I’ve developed a web application for **Neural Machine Translation (NMT)** using Hugging Face's inbuilt models. This application translates text from English to French without requiring an API key. The project utilizes Gradio for the web interface and transformers for the translation process. Additionally, I have explored solving this project using deep learning techniques.

## What is Neural Machine Translation?

1. **Neural Machine Translation (NMT)** is the task of using artificial neural network models for translation from one language to another.
2. The NMT model generally consists of an encoder that encodes a source sentence into a fixed-length vector from which a decoder generates a translation.
3. This problem can be thought of as a prediction problem, where given a sequence of words in the source language as input, the task is to predict the output sequence of words in the target language.
4. The dataset comes from [ManyThings.org](http://www.manythings.org/anki/), where you may find tab-delimited bilingual sentence pairs in different files based on the source and target language of your choice.
5. For this project, you need to use French-English language pairs to evaluate the project uniformly for all students.

## Data Preparation

1. Download the data as a zip file and extract it to the corresponding text file. Read this text file and prepare the list of pairs of language phrases.
2. Now, we will need to clean these pairs. Some operations for cleaning include:
   - Remove non-printable characters, if any.
   - Remove punctuations and non-alphabetic characters.
   - Convert to lowercase.

## Data Splitting and Tokenization

1. After cleaning the data, split it into training and testing sets.
2. Create separate tokenizers for both the source language and the target language.
3. Encode and pad the input (source language) and output (target language) sequences with respect to their individual tokenizers and maximum sequence lengths.
4. Convert the output sequences into one-hot encoding for the target language.

## Model Definition

1. Define a sequential model consisting mainly of two parts: Encoder and Decoder.
2. In the Encoder, pass the input sequence through an Embedding layer (to train the word embeddings for the source language) and then through one or more RNN/LSTM layers.
3. Use a RepeatVector layer to connect the Encoder to the Decoder, as the output shape of the Encoder is not the same as the expected input shape of the Decoder.
4. Stack up the Decoder, adding one or more RNN/LSTM layers and finally a TimeDistributed Dense layer to get output separately by timesteps.
5. Train the model on the training data, experimenting with the number of epochs, optimizer, and batch size to achieve optimal results.

## Evaluation

Use the **BLEU score** for evaluating your model using the NLTK library.

Note: The deployed code utilizes Hugging Face's pre-trained models for translation, making it accessible and efficient for users.

## Techniques Used

- **Translation Model**: Hugging Face's pre-trained model for English to French translation.
- **Web Interface**: Developed using Gradio for user interaction.
- **Transformers**: Utilized for the translation process.

## Installation

Instructions for setting up the development environment and installing dependencies:

```bash
pip install -r requirements.txt


Usage
To use the web application for translating text:
bash


gradio app.py
Technical Details
Libraries Installed: Gradio, Hugging Face Transformers, NLTK
Error Handling and Configuration: The application includes robust error handling mechanisms to ensure smooth operation and user guidance.
License
This project is licensed under the MIT License.
Contact Information
For any questions or suggestions, please contact:
Email: karanmakwana@gmail.com
GitHub: https://github.com/CodeCraftsmanML
