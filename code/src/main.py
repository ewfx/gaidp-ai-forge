import pandas as pd
from sklearn.ensemble import IsolationForest
from transformers import pipeline
import os

# Ensure required folders exist
os.makedirs("output", exist_ok=True)

# Load OpenAI Transformer Pipeline
llm = pipeline("text-generation", model="gpt-3.5-turbo")

# Step 1: Load Data
def load_data(file_path):
    return pd.read_csv(file_path)

# Step 2: AI-Powered Profiling Rules
def generate_profiling_rules_ai(data):
    prompt = f"Analyze the dataset structure and suggest profiling rules: {data.head(5).to_dict()}"
    response = llm(prompt, max_length=300)
    return response[0]['generated_text']

# Step 3: Validate Transactions
def validate_transaction(data):
    errors = []
    if data['account_balance'] < 0:
        errors.append("Account balance should never be negative.")
    if pd.to_datetime(data['transaction_date']) > pd.Timestamp.now():
        errors.append("Transaction date should not be in the future.")
    accepted_jurisdictions = ['US', 'UK', 'EU', 'CA']
    if data['country'] not in accepted_jurisdictions:
        errors.append("Country is not an accepted jurisdiction based on bank regulations.")
    if data['transaction_amount'] != data['reported_amount']:
        errors.append("Transaction amount should always match reported amount.")
    return errors

# Step 4: AI-Powered Anomaly Explanations
def explain_anomalies(anomalies):
    prompt = f"Explain why the following transactions are anomalous: {anomalies.head(5).to_dict()}"
    response = llm(prompt, max_length=300)
    return response[0]['generated_text']

# Step 5: Dynamic Risk Scoring with AI Adjustments
def risk_scoring_ai(data):
    base_score = 50  
    if data['account_balance'] < 0:
        base_score += 20
    if pd.to_datetime(data['transaction_date']) > pd.Timestamp.now():
        base_score += 30
    if data['transaction_amount'] != data['reported_amount']:
        base_score += 40
    if data.get('previous_violations', 0) > 0:
        base_score += data['previous_violations'] * 10

    # AI-Powered Score Refinement
    prompt = f"Adjust risk score based on transaction patterns and violations: {data.to_dict()}"
    response = llm(prompt, max_length=50)
    
    return min(100, base_score + int(response[0]['generated_text'].strip()))

# Step 6: AI-Powered Remediation Suggestions
def suggest_remediation_ai(anomalies):
    prompt = f"Suggest tailored remediation actions for flagged transactions: {anomalies.head(5).to_dict()}"
    response = llm(prompt, max_length=300)
    return response[0]['generated_text']

# Step 7: Execute the Full Pipeline
if __name__ == "__main__":
    input_file = "data/transactions.csv"
    output_file = "output/processed_transactions.csv"

    # Load dataset
    data = load_data(input_file)

    # AI-Generated Profiling Rules
    profiling_rules = generate_profiling_rules_ai(data)

    # Detect anomalies
    features = ['account_balance', 'transaction_amount', 'reported_amount', 'risk_score']
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(data[features])
    data['anomaly'] = model.predict(data[features])
    anomalies = data[data['anomaly'] == -1]

    # AI-Powered Explanations & Remediation
    anomaly_explanations = explain_anomalies(anomalies)
    remediation_actions = suggest_remediation_ai(anomalies)

    # AI-Enhanced Risk Scoring
    data['risk_score'] = data.apply(risk_scoring_ai, axis=1)

    # Save results
    data.to_csv(output_file, index=False)
    
    # Print outputs
    print(f"Profiling Rules:\n{profiling_rules}")
    print(f"Anomalies:\n{anomaly_explanations}")
    print(f"Remediation:\n{remediation_actions}")
    print(f"Processed data saved to {output_file}")
