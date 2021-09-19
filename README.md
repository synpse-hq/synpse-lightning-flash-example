## Model deployment to Synpse

Build it:

```
docker build -t synpse-lighning-flash:latest -f Dockerfile .
```

Run it:

```
docker run -it -p 8000:8000 synpse-lighning-flash:latest
```

### Client side

Install some deps:

```
pip install -r requirements.txt
```

Run it:

```
python client.py
```