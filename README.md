# Lab4_s25098

# Uruchomienie Lokalnie
1. Klonowanie Repozytorium:
   git clone https://github.com/s25098/Lab4_s25098.git
   cd Lab4_s25098
2. Instalacja Zależności i Uruchomienie Aplikacji
   pip install -r requirements.txt
   python main.py
3. Wysłanie zapytania POST
   curl -X POST -H "Content-Type: application/json" -d 'Data' http://localhost:5000/predict

# Uruchomienie z Dockera
1. Pull Obrazu Dockera
   docker pull s25098/score-predictor-api:latest
2. Uruchomienie Kontenera
   docker run -p 5000:5000 s25098/score-predictor-api:latest
3. Wysłanie zapytania POST
   curl -X POST -H "Content-Type: application/json" -d 'Data' http://localhost:5000/predict
