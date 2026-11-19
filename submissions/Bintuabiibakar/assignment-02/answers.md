# Assignment 2 – Preprocessing

**Student Name:** Bintuabiibakar  
**Course:** Natural Language Processing (NLP)  
**Assignment:** 2 – Preprocessing

# Part A – Research

## 1. Text Preprocessing

Text preprocessing is the set of operations used to prepare raw text before it is supplied to an NLP or machine-learning system. Raw text often contains inconsistent capitalization, repeated spaces, punctuation, spelling variation, markup, and other forms that can make analysis harder. Typical operations include normalization, tokenization, filtering, stemming, and lemmatization.

Preprocessing can make text more consistent, reduce irrelevant variation, and help a model focus on patterns related to its task. However, cleaning is not automatically beneficial: deleting information can remove useful signals. For example, a spam detector may use capital letters and repeated exclamation marks in “URGENT!!!” as evidence of promotional or suspicious language. If all capitalization and punctuation are removed, that signal disappears. Similarly, removing “not” from “not happy” reverses or weakens the sentiment. The correct preprocessing strategy therefore depends on the task, data, and model.

## 2. Text Normalization

Text normalization converts different surface forms into a more consistent representation.

- **Lowercasing:** changes uppercase letters to lowercase, for example, `DELIVERY` becomes `delivery`.
- **Whitespace normalization:** replaces repeated spaces, tabs, or line breaks with a consistent separator and may trim spaces at the beginning and end.
- **Unicode normalization:** converts text into a consistent Unicode representation. For example, visually identical accented characters can sometimes be represented as a single precomposed character or as a base character followed by a combining mark. Unicode normalization forms such as NFC and NFKC handle these cases in different ways.

Normalization helps when the same word appears with inconsistent capitalization or spacing. For example, `Great`, `GREAT`, and `great` can be treated as the same token in a case-insensitive product-review classifier.

Normalization can also remove useful information. In a spam detector, converting `URGENT!!!` to `urgent!` removes the repeated punctuation that may be a useful spam signal. Lowercasing can also remove the distinction between a proper name and an ordinary word, such as `Apple` (the company) and `apple` (the fruit). NFKC may additionally fold some compatibility characters, so it should be chosen with awareness of the writing system and task.

## 3. Word-Level, Subword, and Character-Level Tokenization

Tokenization divides text into units that a model can process.

| Tokenization type | How it works | Example for “unhappiness” | Typical vocabulary size |
|---|---|---|---|
| Word-level | Treats whole words as tokens | `unhappiness` | Often large; every distinct word form may need an entry |
| Subword | Divides uncommon words into frequent pieces | e.g. `un`, `happi`, `ness` (exact pieces depend on tokenizer) | Medium; usually a controlled inventory |
| Character-level | Treats individual characters as tokens | `u`, `n`, `h`, `a`, `p`, `p`, `i`, `n`, `e`, `s`, `s` | Small; usually based on characters plus special symbols |

**Vocabulary size** is the number of distinct token types that a tokenizer or model recognizes in its vocabulary. Word-level tokenization can create a very large vocabulary because inflections, spelling variants, and rare names become separate entries. Subword tokenization reduces this problem by representing rare words as combinations of familiar pieces. Character-level tokenization has a small vocabulary and can handle unseen spellings, but it creates longer sequences and may make learning word-level meaning more difficult.

No method is best for every task. Word tokens are intuitive for many traditional text tasks; subwords are widely useful for neural language models; character tokens can be helpful with spelling variation, morphology, or noisy text.

## 4. Stopwords

Stopwords are frequent words that some NLP tasks treat as less informative, such as articles and common prepositions. In English, examples can include `the`, `is`, and `at`. Stopword lists are resources, not universal rules: a word that is unhelpful for one task may be essential for another.

Removing stopwords can reduce the number of features and help a topic-search or document-classification system focus on content words. However, removal can damage meaning. In sentiment analysis, removing `not` from “not happy” changes the polarity. In search, removing a word that is important to a phrase or query can reduce relevance. Stopword lists must therefore be selected for the language, domain, and objective. Lists designed for English should not be applied blindly to Somali or another language.

## 5. Stemming and Lemmatization

**Stemming** reduces a word by applying rules that remove or alter affixes. The result is a stem, which may not be a valid dictionary word. Stemming is usually fast and useful when approximate matching is sufficient.

**Lemmatization** maps an inflected word to a dictionary base form (lemma), using linguistic information such as vocabulary and part of speech. It is generally more linguistically informed, but may require more resources and processing.

### Porter stemming algorithm

The Porter stemmer, introduced by Martin Porter (1980), is a rule-based English suffix-stripping algorithm. It applies ordered rules to reduce related forms, such as `connected` and `connecting`, toward a common stem. It is relatively lightweight and is often useful in information retrieval, where matching related word forms matters more than producing a dictionary word.

### WordNet lemmatization approach

NLTK's `WordNetLemmatizer` uses the WordNet lexical database. It can use a part-of-speech hint to choose an appropriate lemma. For example, the noun form `wolves` can be lemmatized to `wolf`; the verb `ran` can be lemmatized to `run` when the verb hint is supplied. With the default noun setting, a verb may remain unchanged. This illustrates why POS information matters.

Stemming may be preferred for fast retrieval or a simple baseline. Lemmatization may be preferred when readable base forms and grammatical distinctions matter, provided that the language has suitable lexical resources. Neither should be applied automatically: for tasks where exact word forms matter, both may remove useful distinctions.

## 6. Regular Expressions in Text Cleaning

A regular expression (regex) describes a pattern that can be searched for, matched, or replaced in text. Regex is useful for identifying repeated whitespace, phone numbers, URLs, punctuation sequences, and other predictable patterns.

**Example 1 – repeated whitespace**

Pattern: `\s+`

This matches one or more whitespace characters (spaces, tabs, or line breaks). Replacing each match with one ordinary space can normalize spacing.

**Example 2 – a 10-digit phone number**

Pattern: `\b\d{10}\b`

This matches a standalone sequence of exactly ten digits. In the assignment example, it can identify `0712345678` so it can be replaced with a placeholder such as `PHONE_NUMBER`.

An overly broad pattern can damage text. For example, deleting every non-letter character may remove currency symbols, amounts, phone numbers, emoji, apostrophes, and punctuation that express urgency or sentiment. It may also remove information needed for a task. Replacing sensitive patterns with informative placeholders is often safer than deleting them.

## 7. Case Study: Preprocessing Choices for Twitter Sentiment Analysis

Symeonidis, Effrosynidis, and Arampatzis (2018) studied how different preprocessing choices affect Twitter sentiment analysis. The task was sentiment classification: given a tweet, predict its sentiment category. The study compared sixteen preprocessing techniques using two Twitter datasets and four machine-learning algorithms: Linear SVC, Bernoulli Naive Bayes, Logistic Regression, and Convolutional Neural Networks. The researchers evaluated the effects on classification accuracy and also investigated how preprocessing methods interact when combined.

The paper reported that the impact depended on the technique and its combination with other steps. Lemmatization, number removal, and replacing contractions improved accuracy in their experiments, while punctuation removal did not provide the same benefit. Their combination and ablation experiments also showed that the order and interaction of preprocessing steps matter. This case study supports the principle that preprocessing should be tested against the actual task and dataset rather than applied as a fixed cleaning recipe.

**NLP task:** Text classification (sentiment analysis).

## Conclusion

Preprocessing makes text more consistent and can improve NLP performance, but every transformation has a cost. Lowercasing, whitespace normalization, tokenization, stopword filtering, stemming, lemmatization, and regex cleaning should be selected according to the information needed by the task. Negation, punctuation, capitalization, numbers, and emoji can all carry meaning, so they should not be removed without a reason.

## References

1. Porter, M. F. (1980). An algorithm for suffix stripping. *Program, 14*(3), 130–137. https://doi.org/10.1108/eb046814
2. Bird, S., Klein, E., & Loper, E. (2009). *Natural Language Processing with Python*. O'Reilly Media. https://www.nltk.org/book/
3. NLTK Project. (n.d.). *NLTK documentation: Stemmers, WordNetLemmatizer, tokenization, tagging and corpora*. https://www.nltk.org/
4. Symeonidis, S., Effrosynidis, D., & Arampatzis, A. (2018). A comparative evaluation of pre-processing techniques and their interactions for Twitter sentiment analysis. *Expert Systems with Applications, 110*, 298–310. https://doi.org/10.1016/j.eswa.2018.06.022
5. Unicode Consortium. (n.d.). *Unicode Standard Annex #15: Unicode Normalization Forms*. https://unicode.org/reports/tr15/
6. Camacho-Collados, J., & Pilehvar, M. T. (2018). On the role of text preprocessing in neural network architectures: An evaluation study on text categorization and sentiment analysis. *Proceedings of the Workshop on Representation Learning for NLP*. https://aclanthology.org/W18-5406/

# Part B – Practical

## Reproducibility and execution

The practical results must be generated by running `preprocessing_practice.py`; they must not be typed into this report by hand. From the root of the course repository, install the course requirements and run:

```bash
python code/download-nltk-data.py
```

Then open a terminal in this `assignment-02` folder and run:

```bash
python preprocessing_practice.py > output.txt
```

The script prints the before-and-after stages, token counts, stemming comparison, lemmatization comparison, sentence splitting, POS tags, NER output, and both full pipelines.

> **Important:** After running the script, use the actual contents of `output.txt` to complete the tables and short answers below. NLTK tagger and named-entity results can vary by NLTK model version; do not invent or copy expected entities as if they were your program's output.

## Practical results to insert from `output.txt`

### Task 1 – Lowercasing

The script prints T1 before and after lowercasing. Lowercasing makes the text more uniform, but it removes the uppercase emphasis in `URGENT` and `WON`. A spam detector may lose capitalization as a signal of urgency or promotional emphasis, even though the words themselves remain.

### Task 2 – Whitespace

The script uses `re.sub(r"\s+", " ", T4).strip()` and prints both values with `repr()`. This makes leading, trailing, and repeated spaces visible and shows that whitespace normalization changes formatting without intentionally changing the words.

### Task 3 – Regex cleaning

The required pattern `[^a-z\s]` keeps only lowercase English letters and whitespace. It therefore deletes uppercase letters if the text has not first been lowercased, as well as digits, punctuation, the pound sign, and the emoji. The script also demonstrates a safer replacement approach that converts the phone number to `PHONE_NUMBER`, the amount to `MONEY`, and repeated exclamation marks to one exclamation mark.

### Task 4 – Tokenization

The script compares Python's `split()` with NLTK's `word_tokenize()` on T2. `split()` separates on whitespace, while `word_tokenize()` also handles punctuation and contractions as separate tokens. It then reports the token count and the number of unique tokens (vocabulary size) for T4.

### Task 5 – Stopwords and negation

The default NLTK English stopword list includes negation forms that are important to the meaning of T2. Removing them can leave positive-looking content words while losing the customer's negative meaning. The custom list subtracts `not`, `n't`, `no`, and `never` from the removal list, preserving negation in the remaining tokens.

### Task 6 – Stemming comparison

Paste the stemming comparison printed under **TASK 6** in `output.txt` here.

| Original word | Porter | Lancaster | Snowball |
|---|---|---|---|
| connection | From output.txt | From output.txt | From output.txt |
| connected | From output.txt | From output.txt | From output.txt |
| connecting | From output.txt | From output.txt | From output.txt |
| organization | From output.txt | From output.txt | From output.txt |
| organized | From output.txt | From output.txt | From output.txt |
| university | From output.txt | From output.txt | From output.txt |
| universal | From output.txt | From output.txt | From output.txt |
| flies | From output.txt | From output.txt | From output.txt |
| wolves | From output.txt | From output.txt | From output.txt |
| better | From output.txt | From output.txt | From output.txt |
| ran | From output.txt | From output.txt | From output.txt |

Use the collision lines printed by the script to identify at least one pair of different words that a stemmer maps to the same stem. A stem such as `fli` or `org` is a stem fragment, not necessarily a dictionary word. State the exact example shown by your run.

### Task 7 – Lemmatization

Paste or summarize the default and POS-hinted lemma columns from **TASK 7** in `output.txt`. The default `WordNetLemmatizer` behavior uses noun POS unless another part of speech is supplied. Verb hints can therefore change forms such as `ran`, while adjective hints can affect adjective forms such as `better`. Identify the words that changed by comparing the two columns in your actual output.

### Task 8 – Sentence splitting

The script uses NLTK's `sent_tokenize` on T3 and prints each sentence and the total count. Check the printed result to determine whether `Mr.` and `a.m.` were handled as abbreviations or caused incorrect sentence boundaries. Sentence tokenizers use learned or rule-based boundary clues, so their output should be checked rather than assumed.

### Task 9 – POS tagging and named entity recognition

Paste the actual entity list from **TASK 9** in `output.txt` into this table. The labels below are the expected semantic categories for evaluating the text, not a claim that NLTK recognized them correctly.

| Text span | Expected label | Recognized by NLTK? | Correct? |
|---|---|---|---|
| Smith | PERSON | Check output.txt | Check output.txt |
| London | GPE/LOCATION | Check output.txt | Check output.txt |
| Friday | DATE/TIME | Check output.txt | Check output.txt |
| Apple | ORGANIZATION | Check output.txt | Check output.txt |

Also inspect the NLTK tree and report any missed or incorrectly labeled names. In particular, `Apple` refers to a company in this sentence, although a general-purpose NER model may not identify that context correctly. The day `Friday` is a date/time expression and may not be recognized by the NLTK named-entity chunker.

### Task 10 – Full preprocessing pipeline

The script runs the T2 pipeline twice and prints every stage: lowercase, regex, tokenization, stopword removal, and lemmatization. Compare the two final lines. The pipeline that preserves negation should retain the complaint more clearly because it keeps `not` and `n't`; the default stopword pipeline may remove those words and weaken or distort the negative meaning.

## Preprocessing choices for a spam detector

For a spam detector, I would normalize repeated whitespace and use carefully designed regex rules to replace phone numbers and money amounts with placeholders instead of deleting them. Lowercasing may be useful for reducing vocabulary variation, but I would preserve or separately record capitalization and repeated punctuation because `URGENT!!!` can signal spam. I would avoid blindly removing all punctuation, digits, currency symbols, or emoji, and I would test stopword removal rather than assume it helps. The T1 demonstration shows why replacing a phone number and money amount is safer than deleting all non-letter characters, while the T2 demonstration shows why negation should be retained when meaning or sentiment matters.
