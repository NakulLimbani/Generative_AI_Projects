---

# Tutorial 09: Generative Model for Marketing Emails Using LSTM

---

## Objective:
This tutorial demonstrates the implementation of a **Generative Model** using **LSTM** to generate personalized marketing emails from the **Enron Email Dataset**. The goal is to create realistic and coherent email content that can be used in marketing campaigns.

---

## Key Features:

- **LSTM-based Text Generation**: Bidirectional LSTM layers to capture context and generate coherent email content.
- **Data Preprocessing**: Tokenization and cleaning of the Enron Email dataset for training.
- **Temperature-based Sampling**: Control the randomness and creativity of generated emails.
- **Training**: Optimized using the Adam optimizer, with loss and perplexity metrics monitored during training.
- **Text Postprocessing**: Handling sentence fragments and incomplete phrases to improve text coherence.
- **Evaluation**: Measurement of **Test Loss** and **Perplexity** to assess model performance.

---

## Usage:

1. Run the notebook to train the **Generative Model** on the **Enron Email Dataset**.
2. Monitor training progress with **loss curves** and **perplexity**.
3. Generate email content by providing a seed text and adjusting the **temperature** for varied outputs.
