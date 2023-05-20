import requests
import streamlit as st
import json
from pprint import pprint

# Set page title and description using Markdown
st.title("International Space Station Tracker")
st.markdown("This app displays the current number of people in space and their names, along with the location of the ISS.")


# Total number of people in space as well as the names of the people

astros = requests.get("http://api.open-notify.org/astros.json")
astros.text
astros_data = json.loads(astros.text)

ppl_in_space = []
for i in range(0,len(astros_data["people"])):
    name = astros_data["people"][i]["name"]
    ppl_in_space.append(name)

print(f"People that are right now in space:")
print(ppl_in_space)

number_of_astronauts = len(ppl_in_space) 

 # Display the total number of people in space
st.subheader("Total Number of People in Space:")
st.write(number_of_astronauts)

# Display the names of the people in space
st.subheader("Names of People in Space:")
for name in ppl_in_space:
    st.write(name)


# Get the current location of the ISS
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
data = response.json()
latitude = float(data["iss_position"]["latitude"])
longitude = float(data["iss_position"]["longitude"])

# Display a map with the ISS location
st.subheader("Current Location of the International Space Station (ISS):")
st.map(data={"latitude": latitude, "longitude": longitude}, zoom=2)

# Display a description for the map
st.markdown("The map above shows the current location of the International Space Station (ISS).")

if __name__ == "__main__":
    main()



