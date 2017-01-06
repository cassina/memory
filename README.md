Welcome to memory, an starter kit for a Flask application running on Google App Engine.

[Install Google App Engine SDK for python.](https://cloud.google.com/appengine/downloads)

Create a virtual env and install requirements:
```
virtualenv venv --python python2.7
source venv/bin/activate
pip install -r requirements.txt
```

Install dependencies for GAE:
```
pip install requierements.txt -t lib
```

Run this to start smoke tests:
```
nosetests application/
```

You should see something like this:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.388s
```

Run this to start the dev server:
```
dev_appserver.py .
```

Go to ```/_t/smoke``` and you should see something like this:
```
{
  "foo": "bar"
}
```



