# Islamic Knowledge Assistance Chatbot

This project is an Islamic Knowledge Assistance Chatbot developed using Django, HTML, and CSS. The bot is designed to answer questions related to Islam by utilizing a retrieval-based approach with cosine similarity to match user queries with the most relevant answers.

Demo Video - https://youtu.be/V1IRyMDqTm8

## Features

- **Django Framework**: The backend is built using Django, ensuring a scalable and maintainable codebase.
- **Retrieval-Based Approach**: The bot uses TF-IDF vectorization and cosine similarity to retrieve the best matching answers from a predefined dataset.
- **Natural Language Processing**: Preprocessing steps include tokenization, stopword removal, and vectorization to ensure accurate understanding of user queries.
- **Custom Dataset**: A JSON file containing Islamic questions and answers is used to train the chatbot.

## How It Works

1. **Data Preprocessing**: 
   - Stopwords are removed from the user input.
   - The input is tokenized to break down sentences into words.
   - TF-IDF vectorization is applied to transform the words into numerical vectors.

2. **Similarity Matching**:
   - The cosine similarity between the user's question and the predefined dataset is calculated.
   - The bot retrieves the answer corresponding to the most similar question.

3. **User Interface**:
   - The chatbot interface is created using HTML and CSS.
   - Users can interact with the bot, which provides responses based on the similarity of the question to the dataset.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- NLTK
- Scikit-learn

## Usage

- **Home Page**: The homepage welcomes the user and provides a "Start Chat" button to begin interacting with the bot.
- **Chat Interface**: Users can type their questions into the input field. Pressing "Enter" or clicking the "Send" button will trigger the chatbot's response.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.
