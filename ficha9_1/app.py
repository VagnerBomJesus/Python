from flask import Flask, render_template

'''import win32com.client
import os
from PIL import ImageGrab

o = win32com.client.Dispatch('Excel.Application')
o.visible = False

wb = o.Workbooks.Open('C:/Users/shakaw/Documents/python/gestao.xlsx')
ws = wb.Worksheets['Corretiva']

ws.Range(ws.Cells(4,1),ws.Cells(26,16)).Copy()  
img = ImageGrab.grabclipboard()
imgFile = os.path.join('C:/Users/shakaw/Documents/python/','test.jpg')
img.save(imgFile)

ws.Range(ws.Cells(27,1),ws.Cells(56,18)).Copy()  
img = ImageGrab.grabclipboard()
imgFile = os.path.join('C:/Users/shakaw/Documents/python/','test2.jpg')
img.save(imgFile)
'''

app = Flask(__name__, template_folder='template')


@app.route("/index")
def home():
    return render_template('index.html')


@app.route('/')
def message():
    messages = "Welcome to FlaskBlog"
    return messages


if __name__ == "__main__":
    app.run(debug=True)
