import csv
import re
from collections import Counter
import matplotlib.pyplot as plt

def main():
    filename = input("\nEnter the filename to analyze (.txt or .csv): ")

    while not (filename.lower().endswith('.txt') or filename.lower().endswith('.csv')):
        print("Invalid file type. Please enter a .txt or .csv file.")
        filename = input("\nEnter the filename to analyze (.txt or .csv): ")

    text = read_file(filename)
    words = process_text(text)
    word_counts = count_words(words)

    x = int(input("Input the amount of top words you would like to see: "))
    
    top_words = get_top_words(word_counts, x)
    display_words(top_words)
    plot_top_words(top_words)

def read_file(file_name):
    try:

        if file_name.lower().endswith('.txt'):
            with open(file_name, 'rt') as txt_file:
                return txt_file.read()
            
        elif file_name.lower().endswith('.csv'):
            content = []

            with open(file_name, 'rt') as csv_file:
                reader = csv.reader(csv_file)

                for row in reader:
                    for cell in row:
                        content.append(cell)

            return ' '.join(content)
        
        else:
            print("Unsupported file type. Please provide a .txt or .csv file.")
            return ""
        
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.\n")
        return ""
    
def process_text(text):
    text = text.lower()
    return re.findall(r"\b[\w']+\b", text)
    
def count_words(word_list):
    return Counter(word_list)

def get_top_words(word_counts, top_n):
    return word_counts.most_common(top_n)

def display_words(word_list):
    print("\nTop Word Frequencies:")

    for word, count in word_list:
        print(f"{word.capitalize()}: {count}")

def plot_top_words(word_list):
    words = [word for word, _ in word_list]
    counts = [count for _, count in word_list]

    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top Word Frequencies')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    main()