from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()


def sending_sms(text, reciever):

    try:
        account_sid = os.getenv("SID")
        auth_token = os.getenv("AUTH_TOKEN")

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=text,
            from_=os.getenv("SENDER_PHONE"),
            to=reciever
        )
        return "The message was seccussfully sent!"

    except Exception as ex:
        return "Something went wrong...", ex


def main():
    text = input("Please enter sms text: ")
    print(sending_sms(text=text, reciever=os.getenv("RECIEVER_PHONE")))


if __name__ == "__main__":
    main()
