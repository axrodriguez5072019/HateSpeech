# FADOHS: Framework for Detection and Integration of Unstructured Data of Hate Speech on Facebook Using Sentiment and Emotion Analysis

# (Library 1.0 User Manual)


# ABSTRACT  

This is the official manual for the FADHOS’ Library 1.0. This library is fully supported   for nltk==3.5, numpy==1.19.1, matplotlib==3.3.1, pandas==1.1.0, gensim==3.8.3, networkx==2.4, scikit_learn==0.23.2, and python=3.0.

This manual explains how to trigger the identification of hate speech on Facebook of the FADHOS framework. Repository with code to replicate the experiments of the upcoming paper FADHOS. Framework for Detection and Integration of Unstructured Data of Hate Speech on Facebook Using Sentiment and Emotion Analysis.

**Note:** FADOHS’ Framework is only compatible with Python 3.1 and also uses Facebook’s  Graph API.  Since Facebook locked down the groups application programming interface (API) as part of a general crackdown after the Cambridge Analytica data-sharing scandal, hence it is quite difficult to replicate the experiment using our Framework right now.


# I. LIBRARY FILES

The FADHOS’ Library 1.0 contains all the files related to the Hate Speech Detection using Sentiment and Emotion Analysis.

## A. FADHOS’ LIBRARY - STANDALONE

The FADHOS library - standalone folder contains the session
subfolder and several additional files:

1. Program1.py
2. Program2.py
3. Program3.py
4. Program4.py
5. our-method.ipynb
6. our-method-extended.ipynb
7. Untitled-2.ipynb

All these files have their own documentation and explain in great detail how to use them and what do they do.

### Program1.py:  

Discovery Layer. From 9 seed pages discussing discriminatory topics, sensate topics discover other similar pages that promote hate speech. We used program1.py until the three-level of the social graph. Use Graph API to extract the pages the seeds like – create “LIKE” graph. Apply betweenness centrality analysis to get central pages Pick 50 most central.

### Program2.py:  

After obtaining a list of the 50 most influential pages from the crawled network, the latest 1,000 posts per page and the latest 1,000 comments are then collected from each page via the Facebook API. 


### Program3.py: 

Sensitive Social Data Collection. A dictionary-based filter was introduced to keep only the posts
containing potential hate speech. Two dictionaries were adopted for this purpose: the first one contains swearing and bad words or phrases from the Internet; the second one contains words or phrases that, though not bad per se, are related to sensitive topics that usually trigger hatred. Table II shows a small sample of words from these two dictionaries.

### Program4.py: 

Sentiment and Emotion Analysis. We use two tools to perform sentiment and emotion analysis on all the texts to sieve out the dataset of posts that may include the terms from the filter that were not sufficiently negative to be termed hate. The first tool we use is VADER, a sentiment analysis tool with a lexicon and rules that are especially tailored to sentiments posted on social media.

### Our-method.ipynb:

Try raw jammin scores 2) Try normalized jammin scores 3) Normalized jammin + vader scores 4) Balance dataset.

### Our-method-extended.ipynb: 

Create our-method-extended:
1. Try raw jammin scores
2. Try normalized jammin scores
3. Normalized jammin + vader scores
4. Balance dataset.

### Paper-2.ipynb: 

Implementation of the second best approach of Fortuna et al. A Survey on Automatic Detection of Hate Speech in Text SVM + BOG and Bigrams.

### Untitled-2.ipynb:

Implementation of the first approach of Fortuna et al. A survey on Automatic Detection of Hate Speech in Text.

## II. INSTALLATION

*Clone the repository with $ git clone https://github.com/axrodriguez5072019/HateSpeech
*(Optional) Create a virtual environment

Enter the grabmodels folder and install dependencies:
```
$ cd grabmodels
$ pip3 install -r requirements.txt
```

Install DeepWalk
```
$ git clone https://github.com/phanein/deepwalk.git
$ cd deepwalk
$ pip install -r requirements.txt (Note: DeepWalk uses Python 2)
$ python setup.py install
```

## III Usage

Note: The following instructions are for Ubuntu and may apply to other similar unix-based systems. For Windows, some steps may need to be modified.

1. If this is the first time to use the program, you may need to make sure that the NLTK's stopwords are available. In a new terminal do the following:

```
i.  $ python3
ii. >>> import nltk
iii.    >>> nltk.download('stopwords')
iv. >>> quit()
```

2. Within the folder grabmodels run $ python3 grabmodels.py -t <graph_type>
Replace <graph_type> with pathways, minusnet, or jammin to create a classifier end-to-end with one of the three different graph creation approaches.

## IV Hyperparameters

The code is configured to run the complete pipeline with the best reported hyperparameters for each method in the paper. At this moment, in order to try other parameter combinations, you will have to open the file grabmodels.py and within one of the functions run_pathways_example(), run_minusnet_example(), and run_pathways_example(), add the corresponding parameters to the function calls get_pathways_model(), get_minusnet_model(), or get_jammin_model().