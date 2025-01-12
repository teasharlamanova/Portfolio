from flask import Flask, render_template, request
import smtplib

MY_MAIL = 'teasharlamanova@gmail.com'
MY_PASS = 'kkqodkwfexhvashw'

app = Flask(__name__)

def send_mail(name,email,phone,subject,message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL,password=MY_PASS)

        try:
            connection.sendmail(from_addr=MY_MAIL,to_addrs=["teasharlamanova@icloud.com"],
                                msg=f"""Subject: {subject}\n\n
                                Name: {name}
                                Email: {email}
                                Phone: {phone}
                                Message: {message}""")
            print('Your message has been sent successfully!', 'success')
        except Exception as e:
            print(f'Failed to send email: {str(e)}', 'danger')


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == "POST":
        # Handle form submission
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        subject = request.form.get("subject")
        message = request.form.get("message")

        send_mail(name=name, email=email, phone=phone,subject=subject, message=message)
        return render_template('index.html')
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)
