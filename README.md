
# Email Validation Using Regular Expressions (Regex)<br><br>

# Overview<br>
This Python script allows users to validate an email address using regular expressions (regex). The script checks the input email format to ensure it follows a common pattern and is valid based on standard email formatting rules.<br><br>

# Features<br>
- Validates the email address format.<br>
- Allows for the use of alphanumeric characters, dots (.), and underscores (_) in the local part of the email.<br>
- Validates the domain part, ensuring it has a valid top-level domain (TLD).<br>
- Supports multiple levels of domain (e.g., gmail.com, gmail.co.in).<br><br>

# Requirements<br>
- re (Regular Expression) module (Standard Python library)<br><br>

# Example Inputs:<br>
- Valid:<br>
  - sahil.123@gmail.com<br>
  - john_doe123@mail.co.in<br>
  - alice123@domain.com<br><br>
  
- Invalid:<br>
  - .sahil123@gmail.com (starts with a dot)<br>
  - sahil..123@gmail.com (consecutive dots not allowed)<br>
  - sahil123@.com (domain part starts with a dot)<br>
