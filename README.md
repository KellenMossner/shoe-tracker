# shoe-tracker
A simple web scraping script to monitor the prices of shoes and notify me when a monitored pair of shores drops in price.
<nl>
Designed to run on the Google Cloud as a Cloud Run function each day to notify me if any of the selected shoes have dropped in price.

## Email Example
![image](https://github.com/user-attachments/assets/f7ffe773-a273-4adc-a4ac-d074eb4a8122)

## Usage
This script scrapes the prices of specific shoes from a website and sends an email notification to me if any of the shoes are on sale.

### Prerequisites
- Python 3.x
- An internet connection
- A Gmail account with "Less secure app access" enabled or an app-specific password
### Installation
1. Clone the repository or download the script.
2. Navigate to the directory containing the script.
3. Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate
```
4. Install the required packages:
```bash
pip install -r requirements.txt
```
### Configuration
Update the sender_email and sender_password variables in the notify function with your Gmail email and password.
Update the receiver_email variable with the email address where you want to receive notifications.

### Running the Script
Run the script using the following command:
```bash
python3 main.py
```

#### Example
```bash
# Clone the repository
git clone https://github.com/yourusername/shoe-tracker.git
cd shoe-tracker

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the script
python3 main.py
```
