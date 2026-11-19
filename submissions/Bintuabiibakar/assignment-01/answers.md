# Assignment 1 – NLP Foundations

**Student Name:** Bintuabiibakar  
**Course:** Natural Language Processing (NLP)  
**Assignment:** 1 – NLP Foundations

---

## 1. Define Natural Language Processing (NLP). What is its relationship to Artificial Intelligence and Machine Learning?

Natural Language Processing (NLP) is a branch of Artificial Intelligence (AI) that enables computers to understand, interpret, analyze, and generate human language. Human language includes written text and spoken words. NLP allows computers to work with languages such as English, Somali, Arabic, and many others.

NLP is closely related to Artificial Intelligence and Machine Learning:

- **Artificial Intelligence (AI):** A broad field of computer science that focuses on creating machines capable of performing tasks that normally require human intelligence.
- **Machine Learning (ML):** A subfield of AI that enables computers to learn patterns from data and improve their performance without being explicitly programmed for every situation.
- **Natural Language Processing (NLP):** A field that applies computational and AI techniques to process and understand human language. Machine Learning is commonly used to build modern NLP systems.

### Real-Life Example: Email Spam Detection

An email spam detection system demonstrates how AI, ML, and NLP work together.

1. **NLP:** The system examines the words and sentences in an email.
2. **Machine Learning:** The model learns from previously labeled emails, which are classified as spam or not spam.
3. **Artificial Intelligence:** The overall intelligent application uses the model's prediction to help automatically identify unwanted messages.

For example, if an email contains suspicious language and links, the system may classify it as spam.

Therefore, AI provides the broader intelligent system, ML helps the system learn from examples, and NLP enables it to work with human language.

---

## 2. Explain the Terms Corpus, Document, Token, Vocabulary, Feature, and Label.

These terms are important in NLP because they describe how text data is collected, organized, and prepared for Machine Learning.

### Definitions

| Term | Explanation |
|---|---|
| Corpus | A collection of text documents used for language analysis or NLP research. |
| Document | One individual piece of text, such as an email, article, or message. |
| Token | A unit of text produced when a document is divided into smaller parts, usually words or punctuation marks. |
| Vocabulary | The collection of unique tokens found in a corpus. |
| Feature | A measurable or numerical property extracted from text and used as input to a Machine Learning model. |
| Label | The correct category or target assigned to a document or other data sample. |

### Example Dataset: Email Classification

Consider a small dataset containing three emails:

- Document 1: "Win money now"
- Document 2: "Meeting tomorrow"
- Document 3: "Claim your free prize"

Their labels are:

- Document 1: Spam
- Document 2: Not Spam
- Document 3: Spam

The terms apply as follows:

**1. Corpus:** All three emails together form one corpus.

**2. Document:** Each email is an individual document. For example, "Meeting tomorrow" is one document.

**3. Token:** Document 1 can be divided into three tokens: "Win", "money", and "now".

**4. Vocabulary:** The unique words from all three documents form the vocabulary:

`{Win, money, now, Meeting, tomorrow, Claim, your, free, prize}`

**5. Feature:** The frequency of each word can be used as a numerical feature. For example, the word "money" appears once in Document 1 and zero times in the other documents.

**6. Label:** Spam and Not Spam are the labels that indicate the correct category of each email.

This example shows how raw text can be organized into information that a Machine Learning model can process.

---

## 3. Describe Four Common NLP Tasks.

NLP includes different tasks that allow computers to perform useful operations on human language.

### 3.1 Text Classification

Text classification is the process of assigning a category to a complete text document based on its content.

**Input:** A text document, sentence, or message.

**Output:** A predicted category or class.

**Example:** An email classification system receives an email and predicts whether it is Spam or Not Spam.

### 3.2 Sequence Labeling

Sequence labeling assigns a label to each token in a sentence. Instead of classifying the whole document with one category, the system identifies the role of individual words.

**Input:** A sentence containing several tokens.

**Output:** A sequence of labels corresponding to the tokens.

**Example:**

Sentence: "Ahmed lives in Mogadishu."

| Word | Label |
|---|---|
| Ahmed | PERSON |
| lives | OTHER |
| in | OTHER |
| Mogadishu | LOCATION |

This is useful in Named Entity Recognition (NER), which identifies people, places, organizations, and other important names.

### 3.3 Search and Similarity

Search and similarity involve finding documents that are relevant or similar to a user's search query.

**Input:** A search query and a collection of documents.

**Output:** A list of relevant or similar documents, usually ranked by relevance.

**Example:** A user searches for "Machine Learning tutorials." A search system retrieves documents containing relevant information about Machine Learning.

### 3.4 Text Generation

Text generation is the process of producing new human-readable text automatically based on an input or instruction.

**Input:** A prompt, question, or starting text.

**Output:** Newly generated text.

**Example:** A user enters "Explain Artificial Intelligence." An AI system generates a paragraph explaining the topic.

### Summary of NLP Tasks

| NLP Task | Input | Output |
|---|---|---|
| Text Classification | Complete text | Category |
| Sequence Labeling | Sentence or token sequence | Label for each token |
| Search and Similarity | Query and documents | Ranked relevant documents |
| Text Generation | Prompt or starting text | Generated text |

---

## 4. Compare Supervised and Unsupervised Learning in NLP.

Machine Learning approaches in NLP can be divided into supervised and unsupervised learning.

### Supervised Learning

Supervised learning is a Machine Learning approach in which a model learns from training data that already contains correct answers, known as labels.

The model examines the relationship between the input data and its labels. It then uses what it has learned to predict labels for new data.

**Example: Spam Email Classification**

A dataset contains emails labeled as Spam or Not Spam.

- Input: Email text.
- Target label: Spam or Not Spam.
- Output: The predicted email category.

The model needs target labels because it must learn which patterns are associated with each category.

### Unsupervised Learning

Unsupervised learning is a Machine Learning approach in which a model learns patterns and structures from data without receiving predefined target labels.

It attempts to discover similarities, groups, or hidden relationships within the data.

**Example: Customer Review Clustering**

A system receives thousands of customer reviews without categories. It groups similar reviews based on their content.

For example:
- Group 1: Reviews about product quality.
- Group 2: Reviews about delivery.
- Group 3: Reviews about customer service.

The system does not need target labels because its purpose is to discover groups from the data rather than predict previously provided categories.

### Comparison Table

| Supervised Learning | Unsupervised Learning |
|---|---|
| Uses labeled data. | Uses unlabeled data. |
| Has known target outputs during training. | Does not have predefined target outputs. |
| Learns to predict categories or values. | Discovers patterns and groups. |
| Example: Spam detection. | Example: Review clustering. |

**Why do they differ in labels?**

Supervised learning needs labels to guide the model toward the correct answers. Unsupervised learning does not require labels because it searches for patterns and relationships independently.

---

## 5. Why Must Text Be Converted into Numerical Representations Before Most Machine Learning Models Can Use It?

Human language is made up of words, characters, and sentences. However, most traditional Machine Learning algorithms cannot directly process raw text as they process numerical data.

Computers and Machine Learning models generally require numerical representations, such as vectors or matrices, to perform mathematical calculations and identify patterns.

Converting text into numbers allows a Machine Learning model to analyze words, compare documents, and make predictions.

### One Simple Representation Method: Bag of Words (BoW)

Bag of Words is a basic text representation technique that converts text into numerical values by counting how many times each word appears in a document.

It works through three main steps:

1. **Tokenization:** Divide text into individual words.
2. **Vocabulary Creation:** Collect all unique words from the documents.
3. **Counting:** Count the number of times each vocabulary word appears in each document.

### Example

Consider two documents:

- Document 1: "I love NLP"
- Document 2: "I love AI"

The vocabulary is:

`[I, love, NLP, AI]`

The Bag of Words representation becomes:

| Document | I | love | NLP | AI |
|---|---:|---:|---:|---:|
| Document 1 | 1 | 1 | 1 | 0 |
| Document 2 | 1 | 1 | 0 | 1 |

Each row represents a document, and each column represents a word.

The numbers show how many times each word occurs.

### Main Limitation of Bag of Words

The main limitation is that Bag of Words ignores word order and grammatical relationships.

For example:

- "The dog bites the man."
- "The man bites the dog."

These sentences contain the same words, but their meanings are different. Bag of Words may represent them using the same word counts.

Therefore, although Bag of Words is simple and useful, it does not fully understand the meaning or context of sentences.

---

## 6. Research the Challenges of NLP for Low-Resource Languages Such as Somali.

Low-resource languages are languages that have limited digital text, annotated datasets, linguistic tools, and other resources available for developing NLP applications.

Somali is an example of a language that faces several challenges in computational language research.

### Challenge 1: Limited Datasets and Digital Resources

One major challenge is the lack of large, high-quality, publicly available Somali text datasets.

Many NLP systems depend on large amounts of text to learn language patterns. When there is not enough Somali training data, it becomes difficult to train accurate models.

**Effect on NLP systems:**

- Models may not learn enough Somali vocabulary.
- Predictions may become less accurate.
- Systems may perform poorly on new Somali text.
- Developing applications such as translation, sentiment analysis, and information retrieval becomes more difficult.

For example, a Somali chatbot trained on a small dataset may fail to understand many questions that are written in everyday Somali.

Research on Somali information retrieval has also identified the lack of dedicated language resources as an important barrier (Badel et al., 2023).

### Challenge 2: Morphological Complexity and Word Forms

Somali has rich morphology. Words can change their forms through the addition of grammatical and derivational elements.

This means that related words may appear in different forms while sharing a common root or meaning.

**Effect on NLP systems:**

- A model may treat related word forms as completely different words.
- The vocabulary can become unnecessarily large.
- Search systems may fail to retrieve documents containing related forms.
- Text classification models may struggle to recognize similar meanings.

Lemmatization can help by identifying the base form of a word. However, developing accurate Somali lemmatization tools requires knowledge of Somali grammar and sufficient linguistic resources.

Mohamed and Mohamed (2023) developed a Somali lexicon and rule-based lemmatization approach to address this problem.

### Challenge 3: Spelling Variation and Mixed-Language Text

Somali text written on social media and other informal platforms may contain inconsistent spelling, shortened words, and mixtures of Somali and English.

For example, a person may write a Somali sentence and insert English words into it.

**Effect on NLP systems:**

- The same word may appear in several written forms.
- Models may fail to recognize unfamiliar spellings.
- Mixed-language sentences can make language identification difficult.
- Classification and search results may become less reliable.

### Possible Solutions

Some approaches that can help improve Somali NLP include:

1. Collecting more high-quality Somali text datasets.
2. Working with Somali language experts to annotate data.
3. Developing better tokenizers, stemmers, and lemmatizers.
4. Creating language models trained on Somali text.
5. Including informal and mixed-language text in training datasets.

These improvements can help make NLP systems more useful for Somali speakers.

---

## 7. Case Study: Somali Information Retrieval Corpus

### Research Paper

**Title:** Somali Information Retrieval Corpus: Bridging the Gap between Query Translation and Dedicated Language Resources.

**Authors:** Abdisalam Badel, Ting Zhong, Wenxin Tai, and Fan Zhou.

**Publication:** Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023).

**Source:** https://aclanthology.org/2023.emnlp-main.462/

### 7.1 Research Problem

The research focuses on the limited availability of resources for Somali information retrieval.

Information retrieval is the process of finding relevant information or documents based on a user's search query.

The researchers identified that Somali information retrieval research was limited and often depended on translating queries instead of searching using dedicated Somali language resources.

### 7.2 Task

The main task was to develop a Somali information retrieval system that could retrieve relevant documents based on search queries.

For example, a user enters a Somali search query, and the system attempts to find relevant Somali documents.

### 7.3 Data

The researchers created an annotated Somali information retrieval corpus containing **2,335 documents**.

The documents were collected from different sources, including:

- Hiiraan Online.
- Dhacdo.net.
- Somali poetry books.

The researchers worked with language experts and NLP researchers to develop the corpus.

### 7.4 Method

The researchers developed a Somali information retrieval system using a technique called **Pseudo-Relevance Feedback (PRF)**.

Pseudo-Relevance Feedback is a query expansion technique. It uses the initially retrieved documents to identify additional useful terms that can improve the original search query.

The system uses these additional terms to improve the retrieval of relevant documents.

### 7.5 Findings

The study demonstrated the importance of creating dedicated Somali language resources for information retrieval.

The researchers showed that a purpose-built Somali corpus can support the development of search systems and provide a foundation for future Somali NLP applications.

The work also highlighted how collecting and annotating Somali text can help address the shortage of language-specific datasets.

### 7.6 Which NLP Task Does This Case Study Cover?

This research mainly covers **Search and Similarity (Information Retrieval)**.

The input is a user's search query, and the output is a collection of relevant documents retrieved from the Somali corpus.

### Case Study Summary

| Component | Description |
|---|---|
| Problem | Limited Somali information retrieval resources. |
| Task | Somali information retrieval. |
| Data | 2,335 annotated documents. |
| Sources | Hiiraan Online, Dhacdo.net, and Somali poetry books. |
| Method | Pseudo-Relevance Feedback (PRF). |
| Main Contribution | A dedicated Somali corpus and an information retrieval system. |
| NLP Task | Search and Similarity. |

This case study demonstrates how research and language-specific datasets can help improve NLP technologies for low-resource languages such as Somali.

---

## Conclusion

Natural Language Processing is an important area of Artificial Intelligence that allows computers to work with human language.

This assignment explored the relationship between NLP, AI, and Machine Learning, explained important text data concepts, and discussed four common NLP tasks.

It also examined supervised and unsupervised learning and explained why text must be converted into numerical representations before most Machine Learning algorithms can process it.

Finally, the assignment discussed the challenges of developing NLP systems for Somali and examined a research case study on Somali information retrieval.

Overall, developing better datasets, language tools, and research resources is essential for improving NLP applications in Somali and other low-resource languages.

---

## References

1. Jurafsky, D., & Martin, J. H. (2026). *Speech and Language Processing*. Stanford University. https://web.stanford.edu/~jurafsky/slp3/

2. Scikit-learn Developers. (n.d.). *Working with Text Data*. Scikit-learn Documentation. https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html

3. Scikit-learn Developers. (n.d.). *Feature Extraction: Text Feature Extraction and Bag of Words*. https://scikit-learn.org/stable/modules/feature_extraction.html

4. Badel, A., Zhong, T., Tai, W., & Zhou, F. (2023). *Somali Information Retrieval Corpus: Bridging the Gap between Query Translation and Dedicated Language Resources*. Proceedings of EMNLP 2023. https://aclanthology.org/2023.emnlp-main.462/

5. Mohamed, S. A., & Mohamed, M. A. (2023). *Lexicon and Rule-based Word Lemmatization Approach for the Somali Language*. https://arxiv.org/abs/2308.01785

6. Bahar, K., & Ramaha, N. T. A. (2023). *Exploring Somali Sentiment Analysis: A Resource-Light Approach for Small-scale Text Classification*. International Conference on Applied Engineering and Natural Sciences. https://doi.org/10.59287/icaens.1069

7. Nekoto, W., et al. (2020). *Participatory Research for Low-resourced Machine Translation: A Case Study in African Languages*. https://buknlp.github.io/researchgroup/publication/nekoto-2020-aa/
