from twilio.rest import Client 
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
 
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN 
#aa419a169fcbc733eaef3c1fb00f007e
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG1ead865f31acdbb2644e878cecc259e9', 
                              body='SMS prueba2',      
                              to='+573006488489' 
                          ) 
 
print(message.sid)