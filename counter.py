from collections import Counter

def count_word_frequency_from_file(file_path):
    with open(file_path, 'r') as file:
        
        text = file.read()
        
        
        words = text.split()
        
    
        word_counts = Counter(words)
        
        return word_counts


file_path = "/wadah/fprag.txt"

word_frequency = count_word_frequency_from_file(file_path)


for word, count in word_frequency.items():
    print(f"{word}: {count}")
