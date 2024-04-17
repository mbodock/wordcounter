# Python Word Counter

Counts all words in an English text. Great for checking if you've met the essay requirement.

### Running the Project

The easiest way is through your container engine, such as Docker. You can either build it locally or use the public image.

To build, run the following command from within the application's root directory:
```bash
docker build -t wordcounter . 
```

Then start the application with:
```bash
docker run -p 8000:8000 wordcounter
```

Finally, access http://localhost:8000/

> Please note the -p flag to allow us to access the container directly from our browser.


### Running Tests And Contributing

First, install the required libraries in you environment:
```bash
# Create virtualenv
virtualenv env
. env/bin/activate

# Install python requirements
pip install -r requirements.txt

# Install required Corpora/Models
python -m nltk.downloader punkt
python -m nltk.downloader averaged_perceptron_tagger
```

To check if everything is working as it should, run:
```bash
python -m unittest
```

Now we can start a test server with the following command:
```bash
python -m uvicorn main:app --reload
```
