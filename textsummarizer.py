import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from spacy import displacy
# Build a List of Stopwords
stopwords = list(STOP_WORDS)
def getsummary(text):
    
    nlp = spacy.load('en_core_web_sm')
    # Build an NLP Object
    docx = nlp(text)
    # Build Word Frequency
    # word.text is tokenization in spacy
    word_frequencies = {}
    for word in docx:
        if word.text not in stopwords:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    # Maximum Word Frequency
    maximum_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():  
            word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
    # Sentence Tokens
    sentence_list = [ sentence for sentence in docx.sents ]
    # Sentence Score via comparrng each word with sentence
    sentence_scores = {}  
    for sent in sentence_list:  
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if len(sent.text.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word.text.lower()]
                        else:
                            sentence_scores[sent] += word_frequencies[word.text.lower()]
    # Import Heapq 
    from heapq import nlargest
    summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    # List Comprehension of Sentences Converted From Spacy.span to strings
    final_sentences = [ w.text for w in summarized_sentences ]
    summary = ' '.join(final_sentences)
    
    # Length of Summary
    len(summary)
    # Length of Original Text
    len(text)
    from gensim.summarization import summarize
    rettext=summarize(text, word_count=150)
    import json
    data = {}
    data['summarizedtext'] = rettext
    docx = nlp(rettext)
    i =1
    for ent in docx.ents:
        data['tag'+ str(i)] = ent.text
        #print(ent.text, ent.label_)
        i=i+1
    json_data = json.dumps(data)
    #displacy.render(docx, style="dep")
    return json_data