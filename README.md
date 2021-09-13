# MeiMei
A web app interfacing an AI that can spot cats.

## Configuring the project
Activate the virtual environment and install dependencies:
```bash
~/meimei$ source `poetry env info --path`/bin/activate
~/meimei$ poetry install
```
With the virtual environment activated in the current shell, you can omit
`poetry run` before all of the following commands.

## Running tests
`pytest` is installed in the project virtual environment.
```bash
~/meimei$ poetry run pytest
```

## Running the server
You can run an instance of the app server locally:
```bash
~/meimei$ poetry run flask run
```
Open a browser on http://localhost:4000.

## Training the model
Train the default model using the utility script:
```bash
~/meimei/scripts$ poetry run python -m train_model
```
On my laptop (Intel i7 CPU @ 2.20GHz x 8; 16GB RAM), it takes about 35s to train
(209 examples) and test (50 examples) the model through the sample data set,
with training accuracy 98.6% and test accuracy 80.0% using the default
parameters.
