import streamlit as st
import os
from dotenv import load_dotenv
from msal_streamlit_authentication import msal_authentication

# Load environment variables from .env file
load_dotenv()
client_id = os.getenv("CLIENT_ID")
tenant_id = os.getenv("TENANT_ID")
scope = os.getenv("SCOPE")
# add the port based on what you've configured in the azure portal
redirectUri = "http://localhost:4000"
value = msal_authentication(
    login_button_text="Click to Login",

    auth={
        "clientId": client_id,
        "authority": "https://login.microsoftonline.com/" + tenant_id,
        "redirectUri": redirectUri,
        "postLogoutRedirectUri": "/"
    },
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    },
    login_request={
        "scopes": [scope]
    },
    key=1)
if value:
    st.session_state['user_name'] = value['account']['name']
