import os
import pandas as pd
import pyodbc
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pickle
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

load_dotenv()

def get_database_connection():
    return pyodbc.connect(
        f"DRIVER={os.getenv('DB_DRIVER')};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        f"Authentication={os.getenv('DB_AUTHENTICATION')};"
    )

def load_training_data():
    conn = get_database_connection()
    query = "SELECT Heart_Rate_BPM, Sleep_Duration_Hours, Physical_Activity_Steps, Mood_Rating, Mental_Health_Condition FROM TrainingData"
    data = pd.read_sql(query, conn)
    conn.close()
    return data

def train_model():
    print("Training model...")
    data = load_training_data()
    
    X = data[['Heart_Rate_BPM', 'Sleep_Duration_Hours', 'Physical_Activity_Steps', 'Mood_Rating']]
    y = data['Mental_Health_Condition']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    with open('models/trained_model.pkl', 'wb') as file:
        pickle.dump(model, file)

    print("Model trained and saved successfully!")

def start_scheduler():
    scheduler = BackgroundScheduler()
    # Schedule the `train_model` function to run every 7 days
    scheduler.add_job(train_model, 'interval', days=7, id='weekly_model_training')
    scheduler.start()
    print("Scheduler started. The model will be retrained every 7 days.")

if __name__ == "__main__":
    train_model()

    start_scheduler()

    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        print("Stopping scheduler...")

