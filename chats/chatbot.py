import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


def load_qa_pairs(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    qa_pairs = {item['question']: item['answer'] for item in data}
    return qa_pairs

path = "F:\\Islamic-Assistance-ChatBot\\quran_data.json"
qa_pairs = load_qa_pairs(path)


def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    return words

questions = list(qa_pairs.keys())
processed_questions = [' '.join(preprocess_text(q)) for q in questions]
vectorizer = TfidfVectorizer()
vectorizer.fit(processed_questions)
question_vectors = vectorizer.transform(processed_questions)

def get_response(user_query):
    processed_query = ' '.join(preprocess_text(user_query))
    query_vector = vectorizer.transform([processed_query])
    similarities = cosine_similarity(query_vector, question_vectors)
    best_match_index = similarities.argmax()
    best_similarity_score = similarities[0][best_match_index]
    
    threshold = 0.3            # threshold for understanding
    
    if best_similarity_score < threshold:
        return "I didn't understand that."
    
    best_match_question = questions[best_match_index]
    response = qa_pairs[best_match_question]
    return response
