from flask import Flask, render_template, send_file
import matplotlib as mpl
mpl.use('Agg')  # Use 'Agg' backend for non-interactive plotting
import matplotlib.pyplot as plt
import pandas as pd
from utils import to_percentages
from keys import FILE_PATH
import io

app = Flask(__name__)

@app.route('/')
def index():
    file = pd.read_csv(FILE_PATH)
    column = file['category']
    percentage_dict = to_percentages(column.tolist())
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.pie(percentage_dict.values(), labels=percentage_dict.keys(), autopct='%1.1f%%')
    ax1.set_title('Categorias de gastos')

    ax2.bar(x=percentage_dict.keys(), height=percentage_dict.values())
    ax2.set_title('Gastos por semana')

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)