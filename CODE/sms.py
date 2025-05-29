from twilio.rest import Client


def send_sms(self, phone_number, message):
    # twilio account
    account_sid = 'ACa7eea26461ffacc419a7b392a381f193'
    auth_token = 'b7b818ab935964217c37c5ee4f62f50d'
    twilio_number = '+13155441260'
    
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_=twilio_number,
        to=phone_number
    )