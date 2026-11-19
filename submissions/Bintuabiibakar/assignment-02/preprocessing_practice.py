"""
Assignment 2 – Preprocessing
Run from the course repository after installing requirements and downloading NLTK data:
    python code/download-nltk-data.py
    python preprocessing_practice.py > output.txt
"""
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk

T1 = "URGENT!!! You have WON a £1,000 gift card. Call 0712345678 NOW!"
T2 = "I don't think this jacket is worth the price. Not happy at all 😞"
T3 = "Mr. Smith arrived in London on Friday. He met the Apple team at 9 a.m."
T4 = "   The   delivery   was   fast,   and the  packaging   was   great."
WORDS = ["connection", "connected", "connecting", "organization", "organized",
         "university", "universal", "flies", "wolves", "better", "ran"]

def heading(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)

def require_nltk_data():
    # Fail clearly rather than silently inventing or substituting NLTK results.
    resources = {
        "punkt_tab": "tokenizers/punkt_tab",
        "stopwords": "corpora/stopwords",
        "wordnet": "corpora/wordnet",
        "averaged_perceptron_tagger_eng": "taggers/averaged_perceptron_tagger_eng",
        "maxent_ne_chunker_tab": "chunkers/maxent_ne_chunker_tab",
    }
    missing = []
    for package, path in resources.items():
        try:
            nltk.data.find(path)
        except LookupError:
            missing.append(package)
    if missing:
        raise RuntimeError(
            "Required NLTK data is missing: " + ", ".join(missing) +
            ". Run: python code/download-nltk-data.py (from the course repository), "
            "then run this script again."
        )

def main():
    require_nltk_data()

    heading("TASK 1 – LOWERCASE T1")
    print("BEFORE:", T1)
    t1_lower = T1.lower()
    print("AFTER: ", t1_lower)
    print("NOTE: Lowercasing removes the distinction between urgent emphasis and ordinary text.")

    heading("TASK 2 – WHITESPACE NORMALIZATION IN T4")
    print("BEFORE:", repr(T4))
    t4_clean = re.sub(r"\s+", " ", T4).strip()
    print("AFTER: ", repr(t4_clean))

    heading("TASK 3A – REQUIRED REGEX [^a-z\\s] ON LOWERCASED T1")
    print("PATTERN:", r"[^a-z\s]")
    print("BEFORE:", t1_lower)
    regex_deleted = re.sub(r"[^a-z\s]", "", t1_lower)
    print("AFTER: ", regex_deleted)
    deleted = re.findall(r"[^a-z\s]", t1_lower)
    print("DELETED CHARACTERS (in order):", repr(deleted))
    print("UNIQUE DELETED CHARACTERS:", repr(sorted(set(deleted))))

    heading("TASK 3B – REPLACE INSTEAD OF DELETE")
    t1_replaced = re.sub(r"\b\d{10}\b", "PHONE_NUMBER", T1)
    t1_replaced = re.sub(r"£[\d,]+(?:\.\d{2})?", "MONEY", t1_replaced)
    t1_replaced = re.sub(r"!{2,}", "!", t1_replaced)
    print("BEFORE:", T1)
    print("AFTER: ", t1_replaced)

    heading("TASK 4 – TOKENIZATION")
    print("T2:", T2)
    t2_split = T2.split()
    t2_word = word_tokenize(T2)
    print("split() tokens:", t2_split)
    print("split() count:", len(t2_split))
    print("word_tokenize() tokens:", t2_word)
    print("word_tokenize() count:", len(t2_word))
    print("T4 normalized:", t4_clean)
    t4_tokens = word_tokenize(t4_clean)
    print("T4 tokens:", t4_tokens)
    print("T4 token count:", len(t4_tokens))
    print("T4 vocabulary size (unique tokens):", len(set(t4_tokens)))

    heading("TASK 5 – STOPWORDS AND NEGATION")
    english_stop = set(stopwords.words("english"))
    default_remaining = [tok for tok in t2_word if tok.lower() not in english_stop]
    print("ORIGINAL TOKENS:", t2_word)
    print("NLTK DEFAULT STOPWORDS REMOVED:", default_remaining)
    negations = {"not", "n't", "no", "never"}
    custom_stop = english_stop - negations
    custom_remaining = [tok for tok in t2_word if tok.lower() not in custom_stop]
    print("NEGATION-PRESERVING STOPWORDS REMOVED:", custom_remaining)

    heading("TASK 6 – STEMMING COMPARISON")
    stemmers = {
        "Porter": PorterStemmer(),
        "Lancaster": LancasterStemmer(),
        "Snowball": SnowballStemmer("english"),
    }
    print(f"{'WORD':<16}{'PORTER':<16}{'LANCASTER':<16}{'SNOWBALL':<16}")
    results = {}
    for word in WORDS:
        stems = {name: stemmer.stem(word) for name, stemmer in stemmers.items()}
        results[word] = stems
        print(f"{word:<16}{stems['Porter']:<16}{stems['Lancaster']:<16}{stems['Snowball']:<16}")
    print("\nSTEM COLLISIONS (different words mapped to the same stem):")
    for name in stemmers:
        groups = {}
        for word in WORDS:
            groups.setdefault(results[word][name], []).append(word)
        collisions = [f"{stem}: {members}" for stem, members in groups.items() if len(members) > 1]
        print(name + ":", "; ".join(collisions) if collisions else "No collision in this word list")
    print("NOTE: A stem can be a fragment rather than a dictionary word.")

    heading("TASK 7 – WORDNET LEMMATIZATION")
    lemmatizer = WordNetLemmatizer()
    pos_hints = {
        "connection": "n", "connected": "v", "connecting": "v",
        "organization": "n", "organized": "v", "university": "n",
        "universal": "a", "flies": "v", "wolves": "n",
        "better": "a", "ran": "v",
    }
    print(f"{'WORD':<16}{'DEFAULT':<20}{'WITH POS HINT':<20}{'POS':<8}")
    for word in WORDS:
        default = lemmatizer.lemmatize(word)
        hinted = lemmatizer.lemmatize(word, pos=pos_hints[word])
        print(f"{word:<16}{default:<20}{hinted:<20}{pos_hints[word]:<8}")
    print("POS hint key: n=noun, v=verb, a=adjective.")

    heading("TASK 8 – SENTENCE SPLITTING")
    print("BEFORE:", T3)
    sentences = sent_tokenize(T3)
    for i, sentence in enumerate(sentences, 1):
        print(f"Sentence {i}: {sentence}")
    print("SENTENCE COUNT:", len(sentences))

    heading("TASK 9 – POS TAGGING AND NAMED ENTITY RECOGNITION")
    tokens_t3 = word_tokenize(T3)
    tagged = pos_tag(tokens_t3)
    print("TOKENS:", tokens_t3)
    print("POS TAGS:", tagged)
    tree = ne_chunk(tagged)
    print("NE CHUNK TREE:")
    print(tree)
    print("ENTITIES (recognized by NLTK):")
    found = []
    for subtree in tree:
        if hasattr(subtree, "label"):
            entity = " ".join(word for word, tag in subtree.leaves())
            found.append((entity, subtree.label()))
            print(f"- {entity}: {subtree.label()}")
    if not found:
        print("- No named entities recognized.")

    heading("TASK 10 – FULL PIPELINE ON T2")
    def pipeline(label, stop_set):
        print("\n" + label)
        print("0 ORIGINAL:", T2)
        stage1 = T2.lower()
        print("1 LOWERCASE:", stage1)
        # Keep letters, whitespace, apostrophes and emoji; remove punctuation except apostrophes.
        stage2 = re.sub(r"[^\w\s']", " ", stage1, flags=re.UNICODE)
        stage2 = re.sub(r"\s+", " ", stage2).strip()
        print("2 REGEX:", stage2)
        stage3 = word_tokenize(stage2)
        print("3 TOKENIZE:", stage3)
        stage4 = [tok for tok in stage3 if tok.lower() not in stop_set]
        print("4 STOPWORDS:", stage4)
        stage5 = [lemmatizer.lemmatize(tok, pos="v") for tok in stage4]
        print("5 LEMMATIZE (verb hint):", stage5)
        print("FINAL TEXT:", " ".join(stage5))
    pipeline("PIPELINE A – NLTK DEFAULT STOPWORDS", english_stop)
    pipeline("PIPELINE B – KEEP NEGATION WORDS", custom_stop)

if __name__ == "__main__":
    try:
        main()
    except LookupError as exc:
        print("NLTK RESOURCE ERROR:", exc)
        print("Run the course NLTK download script, then retry.")
        raise
    except RuntimeError as exc:
        print("SETUP ERROR:", exc)
        raise
