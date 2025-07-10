from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__, static_folder='static', template_folder='templates')
model = joblib.load('cricket_win_predictor.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        team = request.form['team']
        opponent = request.form['opponent']
        score = int(request.form['score'])
        toss = request.form['toss']
        ground = request.form['ground']

        input_df = pd.DataFrame([{
            'team': team,
            'opponent': opponent,
            'team_score_innings1': score,
            'toss': toss,
            'ground': ground
        }])

        result = model.predict(input_df)[0]
        prediction = "Win" if result == 1 else "Loss"

    return render_template('index.html', prediction=prediction)
    
if __name__ == '__main__':
    app.run(debug=True)
