import spacy

nlp=spacy.load("en_core_web_sm")

text=""
question""

doc=nlp(text)

for ent in doc.ents:
    if question.lower().startswith("who").and ent.label=="PERSON":
        print(ent.text)
        break
