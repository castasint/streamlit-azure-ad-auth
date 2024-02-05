
# Streamlit Azure AD Authentication Demo

This demo showcases the seamless integration of a Streamlit component developed with TypeScript and React, enabling authentication via Microsoft Authentication Library (MSAL) with Azure Active Directory (Azure AD).

## Configuration

Before getting started, ensure your application is configured correctly by following the guidelines provided in the [Microsoft Identity Platform Quickstart](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app). 

     Please note that the app code employs port 4000 by default, which can be modified in the `config.toml`. 
     Ensure consistency between the configured port and your app settings in the Azure portal. 
     
Ensure you opt for single-page registration and make a note of the following essential values:

-   **Tenant ID**: Identifies the Azure AD tenant where your application is registered.
-   **Client ID**: Uniquely identifies your application in Azure AD.
-   **Scope**: (If applicable) Specifies the permissions required by your application.
  

Once you've collected these details, create a `.env` file in your project's root directory and populate it with these values accordingly.

## Installation

Follow these steps to set up the application:

1.  **Clone the repository**:

 Run the following command in your terminal: 
 `git clone https://github.com/castasint/streamlit-azure-ad-auth.git` 
2.  **Install Python dependencies**:

Navigate to the project directory and install the required Python packages using pip:

``cd streamlit-azure-ad-auth``

``pip install -r requirements.txt`` 

## Usage

After completing the installation process, follow these instructions to use the application:

1.  **Run the Streamlit app**:

Execute the following command in your terminal to start the Streamlit server:


`streamlit run index.py` 

2.  **Authenticate**:

Once the server is up and running ([http://localhost:4000](http://localhost:4000/)), access the provided interface to authenticate yourself using your Azure AD credentials.

3.  **Access the Welcome Route**:

Navigate to the welcome route by visiting [localhost:4000/welcome](http://localhost:4000/welcome) in your web browser.

4.  **Verification**:

Upon successful authentication, you should see your name displayed on the welcome page.

## Note

It's worth mentioning that Streamlit cannot operate on port 3000 due to constraints within the Streamlit codebase. This limitation arises from a hardcoded check for the development port in the Streamlit source code. For further insights, refer to the relevant portion of the code [here](https://github.com/streamlit/streamlit/blob/fb60c2756593f830cd3bb1aeab61b7c40a9354c1/frontend/src/lib/baseconsts.ts#L33).
