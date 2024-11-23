# Stock & News Alert App
Get real-time stock fluctuations from Alpha Vantage, fetch relevant news headlines from News API, and receive updates via SMS using Twilio.

### Prerequisites

* **Install the package:** `pip3 install twilio python-dotenv`
* **Sign up for Twilio:** [Twilio Login](https://www.twilio.com/login)
* **Twilio SMS Quickstart (Python):** [Documentation](https://www.twilio.com/docs/messaging/quickstart)
* **Alpha Vantage Stock API:** [Website](https://www.alphavantage.co/documentation/)
* **News API for articles:** [Website](https://newsapi.org/)
* **Online JSON Viewer (for response formatting):** [Tool](https://jsonviewer.stack.hu/)

### Setup

* Create a `.env` file in the root directory to securely store your private variables:

```env
ALPHADVANTAGE_API_KEY=your_alpha_vantage_key
NEWS_API_KEY=your_news_api_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
MY_PHONE=your_verified_phone_number
SENDER_PHONE=your_twilio_sender_number
```
