# Pulled Directly from Twilio


from twilio.rest import Client

account_sid = 'account_sid'
auth_token = 'auth_token'
client = Client(account_sid, auth_token)

# If using Trial account Number needs to be verified, and can only send messages to Verified numbers.
message = client.messages.create(
    from_='+#TwilioNumber#',
    body='#Message#',
    to='+#ClientPhone#' 
)
