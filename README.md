### Keylogger with Email Reporting**  

#### **Project Overview**  
This project is a **keystroke logging tool** designed for **authorized use** in **cybersecurity research, parental control, or personal activity tracking**. It captures and logs keyboard inputs and securely sends the logs via email for review.  

⚠ **Disclaimer:** This tool must only be used with proper authorization. Unauthorized use of keyloggers is illegal and unethical.  

#### **Features**  
- Captures keystrokes in real-time  
- Stores logs with timestamps  
- Sends logs via email automatically  
- Uses environment variables for secure credential handling  
- Stops logging when the **Esc** key is pressed  

#### **Technologies Used**  
- **Python**  
- **pynput** (for keyboard event listening)  
- **smtplib** (for email automation)  
- **dotenv** (for secure credential storage)  

#### **Installation & Setup**  
1. **Clone the repository:**  
   ```sh
   git clone https://github.com/Mado007/keylogger-project.git 
   cd keylogger-tool
   ```  
2. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt  
   ```  
3. **Create a `.env` file** and add your email credentials securely:  
   ```
   EMAIL_ADDRESS=your_email@gmail.com  
   EMAIL_PASSWORD=your_password  
   ```  
4. **Run the script:**  
   ```sh
   python keylogger.py  
   ```  

#### **Ethical Use Cases**  
- Cybersecurity professionals testing **data security**  
- Parents monitoring children's computer usage **with consent**  
- Individuals tracking their own keystrokes for **productivity analysis**  

