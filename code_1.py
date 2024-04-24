import nltk
from nltk.corpus import stopwords
import string


nltk.download('punkt')
nltk.download('stopwords')

def remove_stopwords(text): 
    #
    words = nltk.word_tokenize(text)
    
    stop_words = set(stopwords.words('english'))
    stop_words.update(string.punctuation)
    
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    filtered_text = ' '.join(filtered_words)
    return filtered_text

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        
        text = file.read()
    
    
    filtered_text = remove_stopwords(text)
    
    with open(output_file, 'w') as file:
        
        file.write(filtered_text)


input_file = 'C:\\Users\\rxuun\OneDrive\\Desktop\\assg cloud\\paragraphs.txt'
output_file = 'C:\\Users\\rxuun\\OneDrive\\Desktop\\assg cloud\\fprag.txt'
process_file(input_file, output_file)
