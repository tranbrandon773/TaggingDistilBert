import requests
import pandas as pd
from openai import OpenAI

url = 'https://hcb.hackclub.com/api/v3/organizations'
headers = {
    'Accept': 'application/json'
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    org_ids = [org['id'] for org in data]
    print(org_ids)
else:
    print(f"Failed to retrieve data, status code: {response.status_code}")

organization_ids = org_ids
transactions_data = []
base_url = 'https://hcb.hackclub.com/api/v3/organizations'
headers = {'Accept': 'application/json'}
for org_id in organization_ids:
    url = f'{base_url}/{org_id}/transactions'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        transactions = response.json()
        
        for t in transactions:
            transactions_data.append({
                'Organization ID': org_id,
                'Transaction ID': t['id'],
                'Amount Cents': t['amount_cents'],
                'Memo': t['memo'],
                'Tags': ', '.join([tag['label'] for tag in t['tags']])
            })
            
df_transactions = pd.DataFrame(transactions_data)
df_transactions.to_csv('data.csv')
client = OpenAI(api_key='...')
file_path = 'data.csv'
data = pd.read_csv(file_path)

def get_tag_from_gpt4(client, memo):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Suggest a one-word tag for memos. Use 'Food' for restaurants or food items. Use 'Funding' for mentions of 'funding', 'donation', 'grant', or 'sponsorship'. Consider 'Equipment', 'Prize', 'Marketing', 'Events', 'Programming' for relevant contents. Default to 'Misc' if uncertain."},
                {"role": "user", "content": memo}
            ]
        )
        tag = response.choices[0].message
        return tag
    except Exception as e:
        print(f"Error processing memo: {memo}. Error: {e}")
        return "Misc"

for index, row in data.iterrows():
    if pd.isna(row['Tags']): 
        memo = row['Memo']
        suggested_tag = get_tag_from_gpt4(client, memo)
        data.at[index, 'Tags'] = suggested_tag

updated_file_path = 'NEWNEWNEWdata.csv'
data.to_csv(updated_file_path, index=False)

print("Updated dataset saved to:", updated_file_path)