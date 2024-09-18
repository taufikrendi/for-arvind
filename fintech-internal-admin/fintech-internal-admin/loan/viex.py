import aiohttp
import asyncio
import pandas as pd
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from sklearn.linear_model import LinearRegression
import time
from .forms import ApprovalForm

async def fetch_data(session, url, headers, params=None):
    async with session.get(url, headers=headers, params=params) as response:
        response.raise_for_status()  
        return await response.json()

async def fetch_all_data(tokens):
    api_urls = {
        'loan': "slik socring link here",
        'dukcapil': "verfiy government link here",
        'liveness': "verify liveness gesture link here"
    }

    headers = {
        "Authorization": f"Bearer {tokens['xxx']}",
        "Authorization-Dukcapil": f"Bearer {credentials['xxx']}",
        "Authorization-Liveness": f"Bearer {secret['xxx']}"
    }
    
    async with aiohttp.ClientSession() as session:
        all_data = {'loan': [], 'dukcapil': [], 'liveness': []}
        
        for key, url in api_urls.items():
            token_header_key = {
                'loan': 'Authorization',
                'dukcapil': 'Authorization-Dukcapil',
                'liveness': 'Authorization-Liveness'
            }[key]
            
            page = 1
            while True:
                params = {"page": page}
                data = await fetch_data(session, url, {token_header_key: headers[token_header_key]}, params)
                if not data.get('results'):
                    break
                all_data[key].extend(data.get('results'))
                page += 1
        
        return all_data


def load_or_train_model(loan_data, dukcapil_data, liveness_data):
    combined_data = []

    for i in range(len(loan_data)):
        combined_data.append({**loan_data[i], **dukcapil_data[i], **liveness_data[i]})

    df = pd.DataFrame(combined_data)

    df = df.fillna(0).astype(int)

    X = df[['loan_amount_total', 'loan_current_amount', 'loan_current_month', 'loan_not_payment',
            'dukcapil_score', 'birthdate', 'fullname', 'nik', 'liveness_detection']]
    y = df['loan_at_risk']

    model = LinearRegression()
    model.fit(X, y)
    return model


def process_and_predict(data, model):
    results = []

    loan_data = data['loan']
    dukcapil_data = data['dukcapil']
    liveness_data = data['liveness']
    
    for i in range(len(loan_data)):
        combined_data = {**loan_data[i], **dukcapil_data[i], **liveness_data[i]}
        
        df = pd.DataFrame([combined_data]).fillna(0).astype(int)
        X = df[['loan_amount_total', 'loan_current_amount', 'loan_current_month', 'loan_not_payment',
                'dukcapil_score', 'birthdate', 'fullname', 'nik', 'liveness_detection']]
        
        prediction = model.predict(X)[0]
        threshold = 0.5
        recommendation = "Loan at Risk - Recommended for further action" if prediction >= threshold else "Loan Not at Risk - No immediate action needed"
        
        results.append({
            'prediction': prediction,
            'recommendation': recommendation,
            'nik': combined_data.get('nik')  #
        })

    return results


@require_http_methods(["GET", "POST"])
async def predict_loan_risk(request):
    tokens = {
        'loan': request.GET.get('loan_token', 'default_loan_token'),
        'dukcapil': request.GET.get('dukcapil_token', 'default_dukcapil_token'),
        'liveness': request.GET.get('liveness_token', 'default_liveness_token')
    }

    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            approved = form.cleaned_data.get('approved', False)
            if approved:
                return redirect('loan:verify') 
            else:
                return render(request, 'prediction_results.html', {
                    'form': form,
                    'results': [],
                    'execution_time': '0.00 seconds',
                    'approval_message': 'The request was not approved.'
                })

    all_data = await fetch_all_data(tokens)

    model = load_or_train_model(all_data['loan'], al
