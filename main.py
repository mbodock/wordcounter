from typing import Annotated, Union

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    form = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Word Counter</title>
    </head>
    <body>
        <form action="/submit" method="post">
            <label for="message">Enter you text:</label><br>
            <textarea id="message" name="message" rows="4" cols="50"></textarea><br>
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    """
    return form

@app.post("/submit")
def count(message: Annotated[str, Form()]):
    return {"message": message}
