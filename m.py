import smtplib
import os
from email.message import EmailMessage
import googletrans
from googletrans import Translator
import openai
from flask import Flask,redirect,render_template,request,url_for,send_file,Response
try:
 import cgi
except:
    pass
import os
app2=Flask(__name__)
@app2.route("/y")
def y():
    return render_template("y.html")
# import openai
# Set up your OpenAI API key
openai.api_key = os.getenv("NEW12")
# import googletrans
# from googletrans import Translator
@app2.route("/chatgpt",methods=["POST","GET"])
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
                              return f"{render_template('y.html')},{response2.json()['data'][i]['priceUsd']}"
                          if response2.json()["data"][i]["id"] in user and r in user:
                              response23 = response2.json()["data"][i][r]
                              print(response23)
                              return f"{render_template('y.html')},{response23}"
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
                         re=f"{render_template('y.html')},{translator.translate(response['choices'][0]['message']['content'].strip(), src=str(pri), dest=str(t))}"
                         # pr1 = f"{translator.translate("what's the meaning of the word 'dick' in persian? ", src=str(pri), dest=str(t))}"
                         # return f"{re}"
                         pr = re.replace("Translated", "")
                         return pr
                         #  index=pr.index("text")
                         # o.append(" ".join(pr))
                         # for y1 in o:
                         #     if f"{translator.detect(y1)}".split('=')[1][0:2] != str(t):
                         #         o.remove(y1)
                         #         print(" ".join(o))
                         #         return " ".join(o)
                         # return pr.split("=")[3].replace("pronunciation", "")
                         # prin = b.replace(",", "")
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
                # if input1 not in l and g  not in input1:
            # response1 = chat_with_gpt(user)
    # return ("<form action=/chatgpt method=POST>"
    #         "<input type=text id=user name=user required>"
    #         "<label for=user>user</label>"
    #         "<input type=submit value=Submit>"
    #         "</form>")
if __name__ == "__main__":
  port = int(os.environ.get("PORT", 8080))  # Use the PORT from Render, default to 8080
  app2.run(host="0.0.0.0", port=port)

  
