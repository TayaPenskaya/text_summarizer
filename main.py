from typing import Optional

from fastapi import FastAPI

from summarizer import Summarizer
from transformers import BertTokenizer, BertModel

app = FastAPI()

tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-uncased')
model = BertModel.from_pretrained('bert-base-multilingual-uncased', output_hidden_states=True)
sum_model = Summarizer(custom_model=model, custom_tokenizer=tokenizer)


@app.get("/get_summary")
def sum_text(t: Optional[str] = None):
    return sum_model(t)
