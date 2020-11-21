import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Avg_Session_Length':2, 'Time_on_App':9, 'Time_on_Website':6, 'Length_of_Membership':2})

print(r.json())