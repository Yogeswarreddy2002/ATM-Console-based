### **ATM Management System - Project Description**

This project is a **Python-based ATM Management System** that simulates basic banking operations, designed to enhance Python programming skills and demonstrate effective handling of user data and transactions. The project is menu-driven and ensures user interaction is intuitive and efficient.

---

## **Key Features**
1. **User Authentication**
   - Users are required to enter their **Account Number** and **PIN** for security.
   - Ensures only authorized users can access account details.

2. **Withdrawal Functionality**
   - Allows users to withdraw money from their accounts.
   - Checks if the account has sufficient balance before proceeding.

3. **Deposit Functionality**
   - Enables users to deposit money into their accounts.
   - Automatically updates the account balance.

4. **PIN Generation**
   - Users can generate or reset their PIN securely.
   - Ensures PIN confirmation before updating.

5. **Mini Statement**
   - Displays the following account details:
     - **Name**
     - **Account Number**
     - **Date of Birth**
     - **Current Account Balance**
   - Ensures the PIN is verified before displaying account details.

6. **Fund Transfer**
   - Facilitates the transfer of funds between accounts.
   - Ensures proper validation of account details and sufficient balance.

7. **Exit Option**
   - Users can exit the system cleanly.

---

## **Account Data Structure**
The project stores account details in a dictionary:

```python
Accounts = {
    2000: ["user1", "1-1-2025", 10000, 2002],
    2001: ["user2", "1-2-2025", 20000, 2002],
    2002: ["user3", "1-2-2025", 30000, None],
}
```

Each entry contains:
- **Account Number** (e.g., `2000`)
- **User Name** (e.g., `"user1"`)
- **Date of Birth** (e.g., `"1-1-2025"`)
- **Account Balance** (e.g., `10000`)
- **PIN** (e.g., `2002`)

---

## **Technology Stack**
- **Language:** Python
- **Data Structure:** Dictionary for efficient storage and access
- **Control Flow:** `if-elif-else` conditions for menu navigation
- **Error Handling:** Input validation for improved user experience

---

## **How to Run the Project**
1. **Clone the Repository**
   ```
   git clone <repository_link>
   cd ATM-Management-System
   ```

2. **Run the Python Script**
   ```
   python ATM.py
   ```

3. **Follow the On-Screen Menu:**
   - Choose desired operations like Withdrawal, Deposit, Mini Statement, etc.

---

## **Future Improvements**
- Add a transaction history feature.
- Implement improved security features like OTP-based verification.
- Introduce GUI using Tkinter or PyQt for enhanced user experience.

---

## **Conclusion**
This project effectively demonstrates core programming concepts like condition handling, data structures, and user input validation. It's an ideal project for Python learners and aspiring developers looking to build real-world applications. 🚀
