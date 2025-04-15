from flask import Blueprint, render_template, request, jsonify
from openai import OpenAI

with open("api_key.txt", "r") as file:
    api_key = file.read().strip()
client = OpenAI(api_key = api_key)

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/generate', methods=['POST'])
def generate():
    name = request.form.get('name')
    mail = request.form.get('mail')
    title = request.form.get('title')
    num = request.form.get('num')
    cname = request.form.get('cname')
    desc = request.form.get('desc')
    amount = request.form.get('amount')

    prompt = f"""
            Write a professional and concise cover letter in English for a job application.

            Here are the details of the applicant (remember to include them, like in a letter):

            - Full name: {name}
            - Email: {mail}
            - Phone number: {num}
            - Current job title: {title}

            Company being applied to:
            - Name: {cname}
            - Job description: {desc}

            The cover letter should be tailored to the job description above, sound enthusiastic but professional, and be no longer than {amount} words.

            Start with a brief introduction, mention relevant experience, and end with a polite and confident closing.

            Do not repeat the input information directly. Focus on tone, clarity, and alignment with the job.

            Generate only the content of the letter. Do not include metadata or explanations.
            """

    response = client.responses.create(
    model="gpt-4.1",
    input=prompt
    )
    
    return jsonify({'cover_letter': response.output_text})