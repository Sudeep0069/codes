from flask import Flask,render_template,request
from chat import talk
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('Home.html')


@app.route("/chat")
def call_gemini():
    pr = request.args.get("prompt")
    answer = talk(pr) if pr else ""
    
    # Pass the prompt and the AI's answer back into your HTML template
    return render_template('response.html', prompt=pr, response=answer)



if __name__=='__main__':
    app.run(debug=True)