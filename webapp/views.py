from flask import Blueprint, render_template, request


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        mail = request.form.get('mail')
        num = request.form.get('num')
        title = request.form.get('title')
        cname = request.form.get('cname')
        desc = request.form.get('desc')
        amount = request.form.get('amount')

        #prompt for later
        prompt = f"""Write a cover letter based on this information:
        Full name: {name},
        E-mail: {mail},
        Phone number: {num},
        Job title of the person: {title},
        Name of the company which the person chose: {cname},
        Description of the job the person applies for: {desc},
        Maximum cover letter length (in words): {amount}
        """

        
        cover_letter = "RANDOM RESPONSE"

        return render_template('index.html', cover_letter=cover_letter)

    return render_template('index.html')
