
# Cricket Win Predictor

Predicts T20 cricket match outcomes after the 1st innings using a Logistic Regression model.

## Files

* `cricket_win_predictor.pkl` — trained model
* `app.py` — Flask server
* `templates/index.html` — frontend form with Tailwind CSS
* `static/teams.json` & `static/grounds.json` — teams and grounds lists

## How to run

1. Install requirements: `pip install flask pandas scikit-learn joblib`
2. Start server: `python app.py`
3. Visit `http://127.0.0.1:5000` and input match data to get prediction.


