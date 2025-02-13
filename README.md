# Arash
These lines of codes are regarding using openai's API for free. and it has also been modified to let you know about the real time prices of all cryptocurrencies
import requests
import json
from flask import Flask,redirect,render_template,request,url_for,send_file,Response
app=Flask(__name__)
response = requests.get("https://api.coincap.io/v2/assets/")
@app.route("/y")
def y():
    return render_template("y.html")
import openai
# Set up your OpenAI API key
openai.api_key = os.getenv(OPENAI_SECRET_API)
if not openai_api_key:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")
import googletrans
from googletrans import Translator
@app.route("/chatgpt",methods=["POST","GET"])
def chat_with_gpt( model="gpt-4o-mini", temperature=0.7, max_tokens=900):
    max_retries = 5
    base_wait_time = 2
    if request.method == "POST":
     # email=request.form.get("email")
     # if email not in signed_in_users:
     #     return redirect(url_for("sign_in"))
     # else:
     while True:
        user = request.form.get("user")
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user},
            ],
            timeout=30,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        # Extract and return the assistant's reply
        response2 = requests.get("https://api.coincap.io/v2/assets/")
        l = []
        # for y in range(100):
        #     l.append(response2.json()["data"][y]["id"])
        print(googletrans.LANGUAGES)
        # translator = Translator()
        # try:
        #     print(translator.detect(text1))
        # except:
        #     pass
        while True:
             language = request.form.get("language of response")
             user = request.form.get("user")
             translator = Translator()
             pr = f"{translator.detect(user)}"
             pri = f"{pr}".split('=')[1][0:2]
             if language in googletrans.LANGUAGES.values():
                 for i in range(100):
                    for u in response2.json()["data"]:
                      for r in u:
                          if response2.json()["data"][i]["id"] in user and "price" in user:
                              return f"{render_template("y.html")},{response2.json()["data"][i]["priceUsd"]}"
                          if response2.json()["data"][i]["id"] in user and r in user:
                              response23 = response2.json()["data"][i][r]
                              print(response23)
                              return f"{render_template("y.html")},{response23}"
                          if  "founder".lower() in user or "founder".upper() in user:
                                return "Arash Khajavi was the one who created and modified me in order to stand out"
                                       # f"{translator.detect(text1)}"

                      # return f"{translator.detect(text1)}"
                 # import googletrans
                 # from googletrans import Translator
                 # p=response['choices'][0]['message']['content'].strip()
                 p = []
                 o = []
                 for t, y in googletrans.LANGUAGES.items():
                     if language == y:
                         p.append(t)
                         re=f"{render_template("y.html")},{translator.translate(response['choices'][0]['message']['content'].strip(), src=str(pri), dest=str(t))}"
                         # pr1 = f"{translator.translate("what's the meaning of the word 'dick' in persian? ", src=str(pri), dest=str(t))}"
                         # return f"{re}"
                         pr = re.replace("Translated", "")
                         return pr
                         # return pr.split("=")[3].replace("pronunciation", "")
                         # prin = r.replace(",", "")
                         # pro = prin.split()
                         # return " ".join(pro)
             # pr=f"{translator.detect(language)}"
             # pri = f"{pr}".split('=')[1][0:2]
             # for t,y in googletrans.LANGUAGES.items():
             #   if language == y:

                    # break
                        # print(response2.json()["data"][i][g])
            # except openai.error.RateLimitError:
            #     wait_time = base_wait_time * (2 ** attempt)  # Exponential backoff
            #     print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
            #     time.sleep(wait_time)

    return render_template("y.html")
if __name__ == "__main__":
    app.run(debug=True)
