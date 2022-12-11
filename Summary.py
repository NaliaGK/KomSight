from transformers import pipeline
import re

hub_model_id = "Farras/mt5-small-kompas"
summarizer = pipeline("summarization", model=hub_model_id)

def print_summary(teks):
    news = teks
    summary = summarizer(news)
    summary =  re.sub(r'\[\{\'summary_text\'\: \'<extra_id_0>', '', str(summary))
    summary =  re.sub('\'}]', '', summary)
    return(summary)