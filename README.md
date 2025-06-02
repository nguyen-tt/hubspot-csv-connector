🔗 HubSpot → Google Sheets Sync (AWS Lambda)

Ce projet est un connecteur serverless qui synchronise automatiquement les contacts HubSpot dans un fichier Google Sheets, avec une mise à jour quotidienne grâce à AWS Lambda et EventBridge.

🚀 Fonctionnalités
	•	🔄 Récupération des contacts via l’API HubSpot
	•	📤 Export automatique vers un fichier Google Sheets (via GSpread + API Google)
	•	🗓️ Cronjob quotidien grâce à AWS Lambda + EventBridge
	•	📁 Export CSV local disponible (option)

🛠️ Stack utilisée
	•	Python 3.11
	•	hubspot-api-client
	•	gspread, oauth2client
	•	AWS Lambda
	•	EventBridge (pour le déclenchement planifié)
	•	Hébergement serverless