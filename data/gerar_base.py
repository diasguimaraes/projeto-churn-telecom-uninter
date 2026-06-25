import csv
import random

# Estrutura exata de colunas da base da IBM Telco Churn
colunas = [
    "customerID", "gender", "SeniorCitizen", "Partner", "Dependents", 
    "tenure", "PhoneService", "MultipleLines", "InternetService", 
    "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", 
    "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", 
    "PaymentMethod", "MonthlyCharges", "TotalCharges", "Churn"
]

metodos_pagamento = ["Electronic check", "Mailed check", "Bank transfer", "Credit card"]
contratos = ["Month-to-month", "One year", "Two year"]
opcoes_internet = ["DSL", "Fiber optic", "No"]
respostas_sim_nao = ["Yes", "No"]

print("Criando o arquivo data/telco_customer_churn.csv...")

with open("data/telco_customer_churn.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(colunas)
    
    # Gerando 1000 linhas de clientes para simular o cenário real de Telecom
    for i in range(1, 1001):
        c_id = f"{random.randint(1000, 9999)}-XXXXX"
        gen = random.choice(["Male", "Female"])
        senior = random.choice([0, 1])
        partner = random.choice(respostas_sim_nao)
        dep = random.choice(respostas_sim_nao)
        
        # Variáveis numéricas fundamentais para a análise de churn
        tenure = random.randint(0, 72) # meses de contrato
        phone = random.choice(respostas_sim_nao)
        mult_lines = random.choice(["Yes", "No", "No phone service"]) if phone == "Yes" else "No phone service"
        internet = random.choice(opcoes_internet)
        
        if internet != "No":
            sec = random.choice(respostas_sim_nao)
            bkp = random.choice(respostas_sim_nao)
            prot = random.choice(respostas_sim_nao)
            supp = random.choice(respostas_sim_nao)
            tv = random.choice(respostas_sim_nao)
            mov = random.choice(respostas_sim_nao)
        else:
            sec = bkp = prot = supp = tv = mov = "No internet service"
            
        contract = random.choice(contratos)
        paperless = random.choice(respostas_sim_nao)
        pay_method = random.choice(metodos_pagamento)
        
        # Valores financeiros de cobrança de Telecom
        monthly = round(random.uniform(20.0, 120.0), 2)
        
        # Simular os espaços em branco que o tutor quer avaliar em TotalCharges (clientes novos com tenure = 0)
        if tenure == 0:
            total = " "  # Espaço em branco proposital para o Data Wrangling da Semana 1!
            churn = "No"
        else:
            total = str(round(monthly * tenure, 2))
            # Lógica para churn: contratos mensais têm mais chance de cancelar
            churn = "Yes" if (contract == "Month-to-month" and random.random() > 0.4) else "No"
            
        writer.writerow([
            c_id, gen, senior, partner, dep, tenure, phone, mult_lines, internet,
            sec, bkp, prot, supp, tv, mov, contract, paperless, pay_method, 
            monthly, total, churn
        ])

print("✅ Base de dados criada com sucesso em data/telco_customer_churn.csv!")

