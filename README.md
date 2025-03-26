# 🚀 Project Name

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
A brief overview of your project and its purpose. Mention which problem statement are your attempting to solve. Keep it concise and engaging.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
What inspired you to create this project? Describe the problem you're solving.

## ⚙️ What It Does
This solution extracts, interprets, and refines regulatory reporting instructions using LLMs, generates profiling rules, detects anomalies, and suggests remediation actions. It ensures compliance and risk management through automated validation and adaptive risk scoring.

## 🛠️ How We Built It
LLM Integration: Used NLP models to interpret regulatory reporting instructions and generate profiling rules.
Validation Rules: Implemented business constraints such as negative balance checks, future transaction dates, and jurisdictional validation.
Anomaly Detection: Utilized Isolation Forest for identifying unusual transactions.
Risk Scoring: Developed a dynamic scoring system that adjusts based on transaction patterns and historical violations.
Scalability: Designed an end-to-end pipeline that can handle large datasets efficiently.


## 🚧 Challenges We Faced
Data Complexity: Ensuring accurate profiling across diverse regulatory requirements.
Scalability: Handling large datasets while maintaining processing speed.
Anomaly Accuracy: Fine-tuning Isolation Forest to minimize false positives.
LLM Interpretability: Making AI-generated profiling rules explainable and reliable.


## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/gaidp-ai-forge.git
   ```
2. Install dependencies  
   ```sh
   pip install pandas numpy scikit-learn transformers
   ```
3. Run the project  
   ```sh
   python main.py
   ```

## 🏗️ Tech Stack
- Python 3.8+
- Required Python Libraries:
  - pandas
  - numpy
  - scikit-learn
  - transformers

## 👥 Team
- Pradeep Ramakrishna - [[GitHub](https://github.com/Pradeep0710)] 
