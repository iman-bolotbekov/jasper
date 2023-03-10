import requests
import json

# Define the JasperReports Server URL
jasper_url = "http://127.0.0.1/reportserver/"

# Authenticate to JasperReports Server and get the authentication token
auth_url = jasper_url + "/login"
auth_payload = {"j_username": "jasperadmin", "j_password": "jasperadmin"}
auth_response = requests.post(auth_url, auth_payload)
auth_token = auth_response.cookies["JSESSIONID"]

# Define the data source details
data_source = {
    "label": "Test Data Source",
    "description": "Test Data Source",
    "dataSourceType": "jdbc",
    "jdbcDataSource": {
        "connectionUrl": "jdbc:postgresql://localhost:5432/mydatabase",
        "username": "postgres",
        "password": "postgres",
        "driverClassName": "org.postgresql.Driver"
    }
}

# Create the data source
create_data_source_url = jasper_url + "/resources"
create_data_source_headers = {
    "Content-Type": "application/repository.datasource+json",
    "Accept": "application/json"
}
create_data_source_response = requests.post(
    create_data_source_url,
    headers=create_data_source_headers,
    data=json.dumps(data_source),
    cookies={"JSESSIONID": auth_token}
)

# Check the response
if create_data_source_response.status_code == 201:
    print("Data source created successfully")
else:
    print("Error creating data source: " + create_data_source_response.text)
