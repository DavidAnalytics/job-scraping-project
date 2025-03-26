import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd

# Step 1: Connect to the webpage
base_url = "https://realpython.github.io/fake-jobs/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

# Send a request to the website
response = requests.get(base_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Connected Successfully ✅")
else:
    print("Connection Failed ❌")
    exit()  # Stop execution if the connection fails

# Step 2: Parse the webpage content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all job postings (each job is inside a div with class "card-content")
job_elements = soup.find_all("div", class_="card-content")

# Create an empty list to store extracted job data
job_data = []

# Step 3: Loop through each job element and extract details
for job in job_elements:
    try:
        # Extract the Job Title
        job_title = job.find("h2", class_="title").text.strip()

        # Extract the Company Name
        company_name = job.find("h3", class_="company").text.strip()

        # Extract Location (City & State)
        location_element = job.find("p", class_="location")
        if location_element:
            location_text = location_element.text.strip()

            # Split location into City and State
            location_parts = location_text.split(",")
            city = location_parts[0].strip() if len(location_parts) > 0 else "Unknown"
            state = location_parts[1].strip() if len(location_parts) > 1 else "Unknown"
        else:
            city, state = "Unknown", "Unknown"  # Fallback if location is missing

        # Extract and format the Date Posted
        date_element = job.find("time")  # The date is inside a <time> tag
        if date_element:
            date_posted_str = date_element["datetime"]  # Get date in "YYYY-MM-DD" format
            date_posted = datetime.datetime.strptime(date_posted_str, "%Y-%m-%d")  # Convert to datetime object

            # Format date: "Thursday, 08 April"
            formatted_date = date_posted.strftime("%A, %d %B")
            year = date_posted.year  # Extract year separately
        else:
            formatted_date = "Unknown"
            year = "Unknown"

        # Store the extracted data in a dictionary and add it to the list
        job_data.append({
            "Job Title": job_title,
            "Company Name": company_name,
            "Location (City)": city,
            "Location (State)": state,
            "Date Posted (Day, Month, Day of Week)": formatted_date,
            "Date Posted (Year)": year
        })

    except Exception as e:
        print(f"Error extracting job data for {job_title}: {e}")
        continue  # Skip this job and move to the next

# Step 4: Convert the extracted job data into a Pandas DataFrame
df = pd.DataFrame(job_data)

# Step 5: Print the DataFrame (optional)
print(df)

# Step 6: Save the extracted data into a CSV file
df.to_csv("job_listings.csv", index=False)
print("✅ Job listings saved to job_listings.csv")
