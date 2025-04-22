import spacy

nlp=spacy.load("en_core_web_sm")

text="Elon Musk founded SpaceX in 2002."
question="Who founded SpaceX? "

doc=nlp(text)

for ent in doc.ents:
    if question.lower().startswith("who")and ent.label_=="PERSON":
        print(ent.text)
        break
