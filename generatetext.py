#this is a sample notes. can be replaced to actual content or changed to input parameter as per requirement
meeting_notes = """
Meeting Notes

Date: September 20, 2024
Time: 2:00 PM - 3:00 PM
Location: Conference Room B

Attendees:

Alex Johnson - IT Development Manager
Jamie Smith - Manager
Taylor Brown - Senior Developer
Morgan Lee - Business Analyst
Jordan Davis - Inventory Manager
Casey Miller - ERP Specialist
Agenda:

Introduction and Objectives
Current Inventory Management Challenges
Business Requirements for Inventory Levels
Oracle ERP Solutions and Capabilities
Next Steps and Action Items
Discussion Points:

Introduction and Objectives:

Alex opened the meeting by stating the objective: to discuss the business requirements for managing inventory levels using Oracle ERP.
Current Inventory Management Challenges:

Jordan highlighted the current challenges faced in inventory management, including:
Inaccurate inventory levels leading to stockouts or overstock situations.
Lack of real-time visibility into inventory across multiple locations.
Inefficient manual processes for tracking and updating inventory.
Business Requirements for Inventory Levels:

The team discussed the key business requirements for managing inventory levels:
Real-time Inventory Tracking: Ability to track inventory levels in real-time across all locations.
Automated Replenishment: System to automatically trigger replenishment orders when inventory levels fall below a certain threshold.
Inventory Forecasting: Tools to forecast inventory needs based on historical data and trends.
Integration with Other Modules: Seamless integration with other Oracle ERP modules such as Procurement and Sales.
Reporting and Analytics: Comprehensive reporting and analytics capabilities to monitor inventory performance and make data-driven decisions.
Oracle ERP Solutions and Capabilities:

Casey provided an overview of Oracle ERP's capabilities in managing inventory levels:
Real-time inventory tracking through IoT and barcode scanning.
Automated replenishment workflows and alerts.
Advanced forecasting algorithms for accurate inventory predictions.
Integration with Procurement, Sales, and other modules for end-to-end visibility.
Robust reporting and analytics tools for inventory management.
Next Steps and Action Items:

The team agreed on the following action items:
Alex to coordinate with the IT team to set up a demo of Oracle ERP's inventory management module.
Taylor to gather detailed requirements from the Inventory and Procurement teams.
Morgan to prepare a draft of the business requirements document.
Jordan to provide historical inventory data for analysis and forecasting.
Meeting Adjourned at: 3:00 PM
"""
import requests
import json

ollama_url = 'http://localhost:11434/api/generate'
model_name = 'llama3.1:latest'  # Replace with the actual model name
prompt = f"Based on the following meeting notes and business requirement discussions, write detailed functional specifications and user stories: {meeting_notes}"
response = requests.post(ollama_url, json={'model': model_name, 'prompt': prompt}, stream=True)

if response.status_code == 200:
    functional_specifications = ""
    for line in response.iter_lines():
        if line:
            try:
                line_json = json.loads(line.decode('utf-8'))
                token = line_json.get('response', '')
                functional_specifications += token
                print(token, end='', flush=True)
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")
else:
    print(f"Failed to connect to Ollama. Status code: {response.status_code}")
    print(response.content)
