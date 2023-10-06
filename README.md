# Digital Resume with Python/Streamlit

for Edward | 27 September 2023



## Intro

This is a very simple edition of Digital Resume with Python/Streamlit. The main code is the `app.py` and the main modules are: `streamlit` and `Pillow`, which can be hooked up by running the code below:

```
pip install -r requirements.txt
```



## Run the app in VS Code locally

Open terminal in VS Code and type in:

```
streamlit run app.py
```

then open browser and point to https://localhost:8501



## Run the app in Docker Container locally

1. Start your Docker Desktop (Windows or macOS), then build the image

   ```
   docker build -t marcuszou/digitalresume:0.1 .
   ```

2. Docker run:

   ```
   docker run -dp 127.0.0.1:8501:8501 --name DigiResume marcuszou/digitalresume:0.1
   ```

3. Open a browser and point to:

   ```
   https://127.0.0.1:8501
   ```



## Deploy the webapp to Netlify.com

1. Push the webapp to GitHub

   ```
   git init
   git add .
   git commit -m "DigiCV-1st-commit"
   git branch -M main
   git remote add origin https://github.com/marcuszou/DigitalResume.git
   git push -u origin main
   ```

2. Deploy the webapp to Render.com as a `Web Service`:

   - connecting to the very GitHub repo,
   - Specify the parameters for the website:
     - `Name`="DigiCV666", 
     - `Branch`="main",
     - `Root Directory`="",
     - `Runtime`= "Python 3",
     - `Build Command` = "pip install -r requirements.txt",
     - `Start Command`= "streamlit run app.py".

   

3. Open a browser ad point to the website you just deployed

   ```
   https://digicv66.onrender.com/
   ```

   

## License

* GPL