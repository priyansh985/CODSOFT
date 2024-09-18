import streamlit as st
import nltk
import pickle
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
nltk.download('punkt_tab')
nltk.download('stopwords')
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in (text):
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(ps.stem(i))    
            
    return  ' '.join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model_final.pkl', 'rb'))

st.title('SMS Spam Detection Classifier!')

input_text = st.text_input('Enter the text to be classified as spam or not spam')

if st.button('Predict'):
# 1. preprocess the input text
    transform_sms = transform_text(input_text)


# 2. vectorize the input text
    transform_sms = tfidf.transform([transform_sms])

# 3. predict the input text

    result = model.predict(transform_sms)

    if result[0] == 0:
        st.write('This is Not a SPAM')
    else:
        st.write('This is a SPAM')