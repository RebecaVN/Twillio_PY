from twilio.rest import Client

#Nossa conta
account_sid = 'AC87579b6c6ca924d6fb2ba4068bf9eafe'

#nosso Token
auth_token = '0602f99eda6b8b5d30b4263874d6e7c3'

client = Client (account_sid, auth_token)

client.messages.create(from_="+1 218 277 7602", body="Agora vou te encher o saco por aq tb pq eu te amo :) <3", to="+5511952266735")