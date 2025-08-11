import sqlite3
import os

log_dir = "src/logs"
os.makedirs(log_dir, exist_ok=True)

def log_prediction(input_data, prediction):
    conn = sqlite3.connect(os.path.join(log_dir, "predictions.db"))
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs 
                 (input TEXT, prediction TEXT)''')
    c.execute("INSERT INTO logs (input, prediction) VALUES (?, ?)", 
              (str(input_data), str(prediction)))
    conn.commit()
    conn.close()
