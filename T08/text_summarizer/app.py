from flask import Flask, render_template, request
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, BartTokenizer, BartForConditionalGeneration, PegasusTokenizer, PegasusForConditionalGeneration
import nltk
from nltk.tokenize import sent_tokenize
import networkx as nx
import numpy as np
import pandas as pd
import plotly.express as px

nltk.download('punkt_tab')  # Ensure the correct tokenizer is installed


# Initialize Flask App
app = Flask(__name__)

# Load Models
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load all models (T5, BART, Pegasus for Abstractive, TextRank for Extractive)
model_dict = {
    "T5-small": (T5ForConditionalGeneration.from_pretrained("t5-small").to(device),T5Tokenizer.from_pretrained("t5-small", legacy=False)),
    "facebook/bart-large-cnn": (BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn").to(device),BartTokenizer.from_pretrained("facebook/bart-large-cnn", legacy=False)),
    #"google/pegasus-xsum": (PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum").to(device),PegasusTokenizer.from_pretrained("google/pegasus-xsum", legacy=False)),

    #"facebook/bart-large-cnn": (BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn").to(device), BartTokenizer.from_pretrained("facebook/bart-large-cnn")),
    #"google/pegasus-xsum": (PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum").to(device), PegasusTokenizer.from_pretrained("google/pegasus-xsum")),
}

# Example Evaluation Scores (ROUGE, BLEU)
model_evaluations = {
    "T5": {"rouge1": 0.45, "rouge2": 0.25, "bleu": 0.1},
    "BART": {"rouge1": 0.5, "rouge2": 0.3, "bleu": 0.12},
    "Pegasus": {"rouge1": 0.35, "rouge2": 0.2, "bleu": 0.08}
}

# Abstractive Summarization Function (T5, BART, Pegasus)
def abstractive_summarization(text, model, tokenizer, max_input=512, max_output=150):
    inputs = tokenizer("summarize: " + text, return_tensors="pt", max_length=max_input, truncation=True)
    inputs = {key: val.to(device) for key, val in inputs.items()}
    summary_ids = model.generate(**inputs, max_length=max_output, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Extractive Summarization (TextRank)
def extractive_summarization(text, num_sentences=3):
    sentences = sent_tokenize(text)
    if len(sentences) <= num_sentences:
        return text

    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                similarity_matrix[i][j] = nltk.edit_distance(sentences[i], sentences[j])

    similarity_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(similarity_graph)
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    return " ".join([sent for _, sent in ranked_sentences[:num_sentences]])

from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu

# Function to calculate ROUGE and BLEU scores
def calculate_metrics(reference, generated):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2'], use_stemmer=True)
    rouge_scores = scorer.score(reference, generated)

    # Convert ROUGE scores into usable format
    rouge1 = rouge_scores['rouge1'].fmeasure
    rouge2 = rouge_scores['rouge2'].fmeasure

    # Compute BLEU score
    reference_tokens = [reference.split()]
    generated_tokens = generated.split()
    bleu = sentence_bleu(reference_tokens, generated_tokens)

    return {"rouge1": rouge1, "rouge2": rouge2, "bleu": bleu}


# Route for Summarization
@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    metrics = None  # Store dynamic metrics

    if request.method == "POST":
        text = request.form["input_text"]
        model_choice = request.form["model"]

        model, tokenizer = model_dict.get(model_choice, (None, None))

        # Determine summarization type
        summarization_type = "abstractive" if model_choice in model_dict else "extractive"

        if summarization_type == "abstractive" and model:
            summary = abstractive_summarization(text, model, tokenizer)
        elif summarization_type == "extractive":
            summary = extractive_summarization(text)

        # Compute dynamic metrics based on user input and generated summary
        if summary:
            metrics = calculate_metrics(text, summary)

    return render_template("index.html", summary=summary, metrics=metrics)

# Route for displaying dynamic metrics
@app.route("/metrics")
def metrics():
    # Create a DataFrame for visualizing evaluation scores
    data = {
        "Model": ["T5", "BART", "Pegasus"],
        "ROUGE-1": [model_evaluations["T5"]["rouge1"], model_evaluations["BART"]["rouge1"], model_evaluations["Pegasus"]["rouge1"]],
        "ROUGE-2": [model_evaluations["T5"]["rouge2"], model_evaluations["BART"]["rouge2"], model_evaluations["Pegasus"]["rouge2"]],
        "BLEU": [model_evaluations["T5"]["bleu"], model_evaluations["BART"]["bleu"], model_evaluations["Pegasus"]["bleu"]],
    }

    df = pd.DataFrame(data)

    # Generate a Plotly bar chart for ROUGE-1 scores and BLEU scores
    fig = px.bar(df, x="Model", y=["ROUGE-1", "ROUGE-2", "BLEU"], title="Model Evaluation Scores")

    # Convert the Plotly figure to HTML for embedding in the template
    graph_html = fig.to_html(full_html=False)

    return render_template("metrics.html", graph_html=graph_html)

# Run Flask App
if __name__ == "__main__":
    print("Flask server is starting...")
    app.run(debug=True, host='127.0.0.1', port=5000)
