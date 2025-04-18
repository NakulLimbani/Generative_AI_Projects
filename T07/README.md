# **T07: Building a Chatbot Using a Pre-Trained LLM**

---

## **Objective**
Build a conversational AI chatbot using the GPT-2 model, fine-tuned on the Cornell Movie-Dialogs Corpus. The goal is to create a model capable of generating meaningful dialogue responses by leveraging transfer learning.

---

## **Key Features**
- Fine-tuning GPT-2 (or DistilGPT-2) on a conversational dataset.
- Tokenization and formatting of movie dialogues into structured input-response pairs.
- Use of gradient accumulation, mixed precision (FP16), and memory optimization techniques for training.
- Evaluation of model performance using Perplexity (PPL) and BLEU score.
- Interactive chatbot testing to compare pre- and post-fine-tuning performance.

---

## **Usage**
- Run the provided notebook to fine-tune the GPT-2 model using the Cornell Movie-Dialogs Corpus.
- Monitor the fine-tuning process with loss curves and evaluation metrics.
- Test the chatbot's conversational abilities by providing real-time inputs and generating responses.
- Evaluate the performance using quantitative metrics like Perplexity and BLEU score.
