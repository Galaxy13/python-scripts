from fastapi import FastAPI, Request, Form
from numpy import sqrt, linspace
from fastapi.templating import Jinja2Templates
import matplotlib.pyplot as plt
import io
import base64

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/')
async def root(request: Request, message='Temp'):
    return templates.TemplateResponse("equation.html", {'request': request,
                                                     'message': message})

@app.get('/solve')
def solve_quadrative(a: int, b: int, c: int):
    d = int(b ** 2 - 4 * a * c)
    if d > 0:
        return {'roots': [(-b + sqrt(d)) / (2 * a), ((-b - sqrt(d)) / (2 * a))]}
    elif d == 0:
        return {'roots': [-b / (2 * a)]}
    else:
        return {'roots': []}

@app.post('/solve')
def solve_quadratic(request: Request, a: int = Form(...) , b: int = Form(...), c: int = Form(...)):
    d = int(b ** 2 - 4 * a * c)
    if d > 0:
        return templates.TemplateResponse('solution.html', {"request": request, 'roots': [(-b + sqrt(d)) / (2 * a), ((-b - sqrt(d)) / (2 * a))], 'a': a if a != 1 else '', 'b': b if b != 1 else '', 'c': c if c != 1 else ''})
    elif d == 0:
        return templates.TemplateResponse('solution.html', {"request": request, 'roots': [-b / (2 * a)], 'a': a if a != 1 else '', 'b': b if b != 1 else '', 'c': c if c != 1 else ''})
    else:
        return templates.TemplateResponse('solution.html', {"request": request, 'roots': "No real solution", 'a': a if a != 1 else '', 'b': b if b != 1 else '', 'c': c if c != 1 else ''})

@app.post('/plot')
def plot(request: Request, a: int = Form(...), b: int = Form(...), c: int = Form(...)):
    d = int(b ** 2 - 4 * a * c)
    if d >= 0:
        x = linspace(-10, 10, 100)
        y = a * x ** 2 + b * x + c
        fig = plt.figure()
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Quadratic-equation parabola')
        plt.grid(True)

        pngImage = io.BytesIO()
        fig.savefig(pngImage)
        pngImageB64str = base64.b64encode(pngImage.getvalue()).decode('ascii')
        return templates.TemplateResponse("graph.html", {'request': request,
                                                         'plot': pngImageB64str,
                                                         'a': a if a != 1 else '',
                                                         'b': b if b != 1 else '',
                                                         'c': c if c != 1 else ''})
    else:
        return 'No real solutions'
