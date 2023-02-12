# PhonePe-Pulse-Data-Visualization-and-Exploration

PhonePe is a transactioning application which consists of millions of users with thousands of transactions everyday. To kepp track of the transactions PhonePe has developed a github repository where all the data is stored from which the Pulse Data Visualization and Exploration website imports the data and creates a Geo visualization of India.
This is my project of extracting data from Github and creating my own dashboard to practice different Python libraries.
The approach involved in developing this project is as follows.

1.Data extraction: Clone the Github using scripting to fetch the data from the Phonepe pulse Github repository and store it in a suitable format such as CSV
or JSON.

2. Data transformation: Use a scripting language such as Python, along with libraries such as Pandas, to manipulate and pre-process the data. This may include cleaning the data, handling missing values, and transforming the data into a format suitable for analysis and visualization.

3. Database insertion: Use the "mysql-connector-python" library in Python to connect to a MySQL database and insert the transformed data using SQL commands.

4.Dashboard creation: Use the Streamlit and Plotly libraries in Python to create an interactive and visually appealing dashboard. Plotly's built-in geo map functions can be used to display the data on a map and Streamlit can be used o create a user-friendly interface with multiple dropdown options for users to select different facts and figures to display.

5. Data retrieval: Use the "mysql-connector-python" library to connect to the MySQL database and fetch the data into a Pandas dataframe. Use the data in the dataframe to update the dashboard dynamically.

6. Deployment: Ensure the solution is secure, efficient, and user-friendly. Test the solution thoroughly and deploy the dashboard publicly, making it
accessible to users.

This approach leverages the power of Python and its numerous libraries to extract, transform, and analyze data, and to create a user-friendly dashboard for visualizing
the insights obtained from the data.
