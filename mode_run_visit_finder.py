from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with the actual path to your browser driver
driver_path = '/path/to/chromedriver' 

# Initialize the web driver (Chrome in this example)
driver = webdriver.Chrome(executable_path=driver_path)

# Navigate to the URL
url = 'https://app.mode.com/cloverhealth/reports/23e529f4ae96'
driver.get(url)

# Wait for the element to be loaded (adjust timeout as needed)
wait = WebDriverWait(driver, 10)  

# The ID of the input field
element_id = "report_run_params_search_term" 

try:
    # Wait for the input field to be visible and clickable
    input_field = wait.until(EC.element_to_be_clickable((By.ID, element_id)))  
    
    # Input the text
    input_text = "your_text_here"  # Replace with your desired text
    input_field.send_keys(input_text)

except Exception as e:
    print(f"Error: {e}")

# Optionally, keep the browser open to see the result
# input("Press Enter to close the browser...")

# Close the browser
driver.quit()