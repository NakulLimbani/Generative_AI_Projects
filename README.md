# Generative AI Projects

---

# Generative AI Projects

Welcome to the **Generative AI Projects** repository! This collection is focused on exploring and showcasing a variety of generative models, including Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs). The tutorials and projects here cover a range of datasets and applications, from classic benchmarks like MNIST to more complex ones like CIFAR-10 and FashionMNIST.

Whether you're looking to learn about generative AI or build on existing knowledge, this repository offers hands-on projects and easy-to-follow code to help you dive into the exciting world of AI-generated content.

---

## Table of Contents

- [Tutorial 1: Generative Adversarial Networks (GANs) on MNIST](#tutorial-1-generative-adversarial-networks-gans-on-MNIST)
- [Tutorial 2: Generative Adversarial Networks (GANs) on CIFAR-10](#tutorial-2-generative-adversarial-networks-gans-on-CIFAR-10)
- [Tutorial 3: Variational Autoencoder (VAE) on Fashion MNIST](#tutorial-3-variational-autoencoder-vae-on-fashion-mnist)
- [Tutorial 4: VAE on Fashion MNIST Dataset](#tutorial-4-vae-on-fashion-mnist-dataset)
- [Tutorial 5: Apply Regularization Techniques to Improve VAE](#tutorial-5-apply-regularization-techniques-to-improve-vae)
- [Tutorial 6: Fine-Tuning a Transformer Model on Wikipedia Text Corpus](#tutorial-6-fine-tuning-a-transformer-model-on-wikipedia-text-corpus)
- [Tutorial 8: AI based Text Summarization Application](#tutorial-8-ai-based-text-summarization-application)
- [Tutorial 09: Generative Model for Marketing Emails Using LSTM](#tutorial-9-generative-model-for-marketing-emails-using-lstm)

---

## Tutorials Overview

### Tutorial 1: **Generative Adversarial Networks (GANs) on MNIST**

**Objective:** Train a GAN to generate realistic images from the MNIST dataset.

**Key Features:**
- Implementation of Generator and Discriminator networks.
- Training using adversarial loss.
- Visualizing generated images at different epochs.

---

### Tutorial 2: **Generative Adversarial Networks (GANs) on CIFAR-10**

**Objective:** Train a GAN to generate realistic images from the the CIFAR-10 dataset.

**Key Features:**
- Generator and Discriminator network implementations.
- Adversarial training over 100 epochs.
- Visualizations of generated images and loss trends.
- Evaluation using FID and Inception Score.

---

### Tutorial 3: **Variational Autoencoder (VAE) on Fashion MNIST**

**Objective:** This tutorial demonstrates the implementation and training of a Variational Autoencoder (VAE) using the Fashion MNIST dataset. The VAE is trained to learn meaningful latent representations for image reconstruction and generation.

**Key Features:**
- Implementation of Encoder, Decoder, and Variational Sampling.
- Training using the Fashion MNIST dataset.
- Visualization of training loss and reconstructed images.
- Analysis of latent space using t-SNE and PCA.
- Comparison with standard Autoencoders.

---

### Tutorial 4: **VAE on Fashion MNIST Dataset**

**Objective:** Train a VAE on grayscale images from the Fashion MNIST dataset.

**Key Features:**
- Application of regularization techniques (dropout, batch normalization).
- Visualization of generated images from latent space.
- Analysis of reconstruction quality over training epochs.

---

### Tutorial 5: **Apply Regularization Techniques to Improve VAE**

**Objective:** Enhance the performance of VAE using various regularization techniques and compare performance with and without regularization.

**Key Features:**
- Implementation of L1/L2 regularization, dropout, batch normalization, and Beta-VAE.
- Data augmentation for better generalization.
- Comprehensive evaluation: reconstruction loss, training loss curves, and image quality.
- Comparison of AE, VAE (with and without regularization), and Beta-VAE.

---

### Tutorial 6: **Fine-Tuning a Transformer Model on Wikipedia Text Corpus**

**Objective:** This project demonstrates the implementation and fine-tuning of a pre-trained Transformer model (GPT-2) on the Wikipedia text corpus. The goal is to improve text generation quality by leveraging transfer learning and analyzing the model’s performance through various evaluation metrics.

**Key Features:**
- Loading and fine-tuning GPT-2 on Wikipedia dataset
- Efficient tokenization and preprocessing for text corpus
- Adversarial training using AdamW optimizer, learning rate scheduling, and gradient clipping
- Training loss and evaluation loss visualizations
- Comparison of text generation before and after fine-tuning
- Perplexity calculation to evaluate language model performance

---

### Tutorial 8: **AI based Text Summarization Application**

**Objective:** Develop a text summarization tool using pre-trained transformer models (T5, BART, Pegasus) and extractive techniques (TextRank) to generate concise summaries from news articles or business reports.

**Key Features:**
- Implementation of Abstractive (T5, BART, Pegasus) and Extractive (TextRank) summarization.
- Flask-based web application for interactive summarization.
- Evaluation using ROUGE & BLEU scores for performance analysis.

---

### Tutorial 09: **Generative Model for Marketing Emails Using LSTM**

**Objective:** Develop a Generative Model using LSTM to generate personalized marketing emails from the Enron Email Dataset. The aim is to create realistic email content for marketing purposes.

**Key Features:**
- LSTM-based Text Generation: Utilize Bidirectional LSTM layers for generating coherent emails.
- Preprocessing: Clean and tokenize the Enron dataset for training.
- Temperature Sampling: Control creativity in generated text with temperature values.
- Evaluation: Measure model performance using Test Loss and Perplexity metrics.

---

## Why This Repository?

This repository serves as a hub for experiments, tutorials, and real-world applications of generative models. It's designed for developers, data scientists, and AI enthusiasts who are interested in:
- Understanding the principles behind generative models.
- Building AI-driven systems for image generation, transformation, and manipulation.
- Experimenting with state-of-the-art architectures in machine learning.

You’ll find clean, well-documented code that enables you to explore, customize, and extend the projects. Each tutorial is carefully crafted to provide meaningful insights and practical applications of AI.

## Features

- **Generative Models:** GANs (Generative Adversarial Networks) and VAEs (Variational Autoencoders) implemented from scratch.
- **Diverse Datasets:** Projects using popular datasets like MNIST, FashionMNIST, and CIFAR-10.
- **Modular and Extensible Code:** Easily understandable code structure that can be adapted for various use cases.
- **Visualization:** Code for generating and visualizing AI outputs (e.g., images) as well as training progress.

## Getting Started

To get started with any of the projects, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/NakulLimbani/Generative_AI_Projects.git 
