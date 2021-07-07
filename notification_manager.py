# This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import smtplib
from data_manager import DataManager

class NotificationManager:

    def __init__(self):
        self.twilio_account_sid = "AC8c617f74e1d7802c219754a3c90c64c2"
        self.twilio_auth_token = "fe5b23906089d607281cc32a675e6b9c"
        self.from_number = "+16672132844"
        self.to_number = "+17039668858"
        self.user_email = "pythontest12320@gmail.com"
        self.user_password = "Boombox1"
        self.email_type = "smtp.gmail.com"

    def send_message(self, data):
        client = Client(self.twilio_account_sid, self.twilio_auth_token)

        message = client.messages.create(
            body=f"""
Low price alert! Only ${data["price"]} to fly from
{data["cityFrom"]}-{data["flyFrom"]} to {data["cityTo"]}-{data["flyTo"]}, from
{data["route"][0]["local_departure"].split("T")[0]} to {data["route"][1]["local_departure"].split("T")[0]} 
""",
            from_=self.from_number,
            to=self.to_number,
        )

    def send_email(self, data):
        # user_manager = DataManager()
        # user_data = user_manager.get_users()
        user_data = [{'firstName': 'Lorne', 'lastName': 'Malvo', 'email': 'pythontest12320@gmail.com', 'id': 2}, {'firstName': 'Lester', 'lastName': 'Nygard', 'email': 'pythontest12320@yahoo.com', 'id': 3}]
        for user in user_data:
            with smtplib.SMTP(self.email_type) as connection:
                connection.starttls()
                connection.login(user=self.user_email, password=self.user_password)
                connection.sendmail(
                    from_addr=self.user_email,
                    to_addrs=user["email"],
                    msg=f"""Subject: New Low Price Flight! \n\n Low price alert! Only ${data['price']} to fly from
{data["cityFrom"]}-{data["flyFrom"]} to {data["cityTo"]}-{data["flyTo"]}, from
{data["route"][0]["local_departure"].split("T")[0]} to {data["route"][1]["local_departure"].split("T")[0]} \n
https://www.google.co.uk/flights?hl=en#flt={data["flyFrom"]}.{data["flyTo"]}.{data["route"][0]["local_departure"].split("T")[0]}*{data["flyTo"]}.{data["flyFrom"]}.{data["route"][1]["local_departure"].split("T")[0]}
"""
                )

