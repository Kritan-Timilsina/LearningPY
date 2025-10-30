#User function Template for python3
s = input()

# Your code here
words=s.split()
capitalized_words=[word.capitalize() for word in words]
capitalized_line=' '.join(capitalized_words)
word_count=len(words)
print(capitalized_line)
print(word_count)