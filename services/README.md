# services app

It was kind of hard to cobble together the information on how to make a really basic, Hello World style microservice app for AppEngine! This does just that... Performs simple string concatenation with the help of a simple microservice, which is deployed as a separate Google AppEngine service (but part of the same app).

The microservice sends back a reponse with a json formatted data in the body. The `main.py` script receives this data and loads it into a dictionary for convenience.

Deployed with:
```shell
gcloud app deploy app.yaml service1/app.yaml --project <project name>
```

The app is live at: https://ea-ut-apt-servicepractice.appspot.com/.
