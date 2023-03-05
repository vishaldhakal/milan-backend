from sitesettings.models import SMTPSetting
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import  EmailMultiAlternatives

class Util:

    @staticmethod
    def send_mail_register(data):
        # smtpsetting = SMTPSetting.objects.last()
        backend = EmailBackend(port=587,
                               host='smtp.gmail.com',
                               username=settings.EMAIL_HOST_USERNAME,
                               password=settings.EMAIL_HOST_PASSWORD,
                               fail_silently=False
                               )
        
        email = EmailMessage(subject= data['email_subject'], body=data['email_body'], from_email= settings.EMAIL_HOST_USERNAME,to=[data['email_receiver']], connection=backend)
        email.send()

    @staticmethod
    def send_mail_admin(data):
        backend = EmailBackend(port=587,
                               host='smtp.gmail.com',
                               username=settings.EMAIL_HOST_USERNAME,
                               password=settings.EMAIL_HOST_PASSWORD,
                               fail_silently=False
                               )

        text_content = """
       <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap"
      rel="stylesheet"
    />
    <title></title>
  </head>
  <body>
    <div
      style="
        font-family: 'Poppins', sans-serif;
        font-size: 14px;
        background-color: white;
        border: 4px solid #b1d7b4;
        border-radius: 8px;
        padding: 15px;
        max-width: 700px;
        width: 100%;
        margin: 0 auto;
      "
    >
      <div style="display: flex; align-items: center; padding-left: 1.5px">
        <span> Hi </span>
        <span
          style="
            color: rgba(0, 112, 117, 0.65);
            word-break: break-all;
            margin-left: 4px;
          "
        >
          Milan
        </span>
      </div>
      <div
        style="
          font-size: 18px;
          font-weight: 500;
          margin-bottom: 16px;
          padding-left: 1.5px;
        "
      >
        Some one contacted you from Contact US form
      </div>
      <ul style="list-style-type: none; margin: 0; padding: 0">
        <li
          style="
            display:block;
            color: #6b7280;
            border: 2px solid #6b7280;
            border-radius: 3px;
            padding: 5px 10px 5px 15px;
            margin: 6px 0;
            font-weight: 500;
          "
        >
          <div
            style="color: #374151; font-size: 16px; text-transform: capitalize"
          >
            Name
          </div>
          <div>{}</div>
        </li>
        <li
          style="
            display:block;
            color: #6b7280;
            border: 2px solid #6b7280;
            border-radius: 3px;
            padding: 5px 10px 5px 15px;
            margin: 6px 0;
            font-weight: 500;
          "
        >
          <div
            style="color: #374151; font-size: 16px; text-transform: capitalize"
          >
            Email
          </div>
          <div>{}</div>
        </li>
        <li
          style="
            display:block;
            color: #6b7280;
            border: 2px solid #6b7280;
            border-radius: 3px;
            padding: 5px 10px 5px 15px;
            margin: 6px 0;
            font-weight: 500;
          "
        >
          <div
            style="color: #374151; font-size: 16px; text-transform: capitalize"
          >
            Phone
          </div>
          <div>{}</div>
        </li>
        <li
          style="
            display:block;
            color: #6b7280;
            border: 2px solid #6b7280;
            border-radius: 3px;
            padding: 5px 10px 5px 15px;
            margin: 6px 0;
            font-weight: 500;
          "
        >
          <div
            style="color: #374151; font-size: 16px; text-transform: capitalize"
          >
            Subject
          </div>
          <div>{}</div>
        </li>
        <li
          style="
            display:block;
            color: #6b7280;
            border: 2px solid #6b7280;
            border-radius: 3px;
            padding: 5px 10px 5px 15px;
            margin: 6px 0;
            font-weight: 500;
          "
        >
          <div
            style="color: #374151; font-size: 16px; text-transform: capitalize"
          >
            Message
          </div>
          <div>
            {}
          </div>
        </li>
      </ul>
    </div>
  </body>
</html>
        """.format(data['name'],data['user_email'], data['user_phone'], data['subject'], data['user_message'])
        msg = EmailMultiAlternatives(subject =data['email_subject'],body =text_content,from_email =settings.EMAIL_HOST_USERNAME,to = [data['email_receiver']],connection=backend)
        msg.attach_alternative(text_content, "text/html")
        msg.send()


    @staticmethod
    def send_mail_admin_for_answer(data):
        backend = EmailBackend(port=587,
                               host='smtp.gmail.com',
                               username=settings.EMAIL_HOST_USERNAME,
                               password=settings.EMAIL_HOST_PASSWORD,
                               fail_silently=False
                               )
        text_content = """
        <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap"
      rel="stylesheet"
    />
    <title>QA</title>
  </head>
  <body>
    <div
      style="
        font-family: 'Poppins', sans-serif;
        font-size: 14px;
        background-color: white;
        border: 4px solid #b1d7b4;
        border-radius: 12px;
        padding: 18px;
        max-width: 700px;
        width: 100%;
        margin: 0 auto;
      "
    >
      <div style="display: flex; align-items: center; padding-left: 1.5px">
        <span>Hi</span>
        <span
          style="
            color: rgba(0, 112, 117, 0.65);
            word-break: break-all;
            margin-left: 4px;
          "
        >
          Milan
        </span>
      </div>
      <div
        style="
          font-size: 18px;
          font-weight: 500;
          margin-bottom: 16px;
          padding-left: 1.5px;
        "
      >
        Someone has answered a question from Giveaway Form
      </div>
      <div>
        <div
          style="
            color: #6b7280;
            position: relative;
            border: 2px solid #6b7280;
            border-radius: 6px;
            padding: 5px 10px;
            margin: 0;
            font-weight: 500;
            margin-bottom: 10px;
          "
        >
          <div
            style="color: #374151; font-size: 16px; text-transform: capitalize"
          >
            Full Name
          </div>
          <div>{} {}</div>
        </div>
 
        <div
          style="
            color: #6b7280;
            position: relative;
            border: 2px solid #6b7280;
            border-radius: 6px;
            padding: 5px 10px;
            font-weight: 500;
            display: block;
            margin: 0;
            margin-bottom: 10px;
          "
        >
          <div
            style="color: #374151; font-size: 16px; text-transform: capitalize"
          >
            Email
          </div>
          <div style="color: #6b7280; text-decoration: none">
            {}
          </div>
        </div>
 
        <div
          style="
            color: #6b7280;
            position: relative;
            border: 2px solid #6b7280;
            border-radius: 6px;
            padding: 5px 10px;
            font-weight: 500;
            display: block;
            margin: 0;
            margin-bottom: 10px;
          "
        >
          <div
            style="color: #374151; font-size: 16px; text-transform: capitalize"
          >
            Phone Number
          </div>
          <div>{}</div>
        </div>
        <div
          style="
            color: #6b7280;
            position: relative;
            border: 2px solid #6b7280;
            border-radius: 6px;
            font-weight: 500;
            overflow: hidden;
            display: block;
            margin: 0;
            margin-bottom: 10px;
          "
        >
          <div
            style="
              color: #4b5563;
              background-color: #f1f5f9;
              text-align: center;
              padding: 5px 10px;
              margin-bottom: 2px;
            "
          >
            QA
          </div>
          <div style="padding: 5px 10px">
            <div
              style="
                color: #374151;
                font-size: 16px;
                text-transform: capitalize;
              "
            >
              {}
            </div>
            <div>
              {}
            </div>
          </div>
        </div>
      </div>
 
    
    </div>
  </body>
</html>
        """.format(data['first_name'],data['last_name'],data['user_email'],data['user_phone_number'],data['user_question'],data['user_answer'])
        msg = EmailMultiAlternatives(subject =data['email_subject'],body =text_content,from_email =settings.EMAIL_HOST_USERNAME,to = [data['email_receiver']],connection=backend)
        msg.attach_alternative(text_content, "text/html")
        msg.send()
