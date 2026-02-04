import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile and STEM data", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Education", "Research Interests", "Publications", "Contact"],
)

# Dummy STEM data
phd_data = pd.DataFrame({
    "Degree": ["PhD in Bioinformatics"],
    "Institution": ["Rhodes University"],
    "Years": ["2019 - 2023"],
    "Thesis": ["Computational studies in human African trypanosomiasis"],
    "Focus": ["Structural bioinformatics, protein-protein interactions, computational drug discovery"]   
})

msc_data = pd.DataFramep({
    "Degree": ["MSc in Bioinformatics"],
    "Institution": ["Rhodes University"],
    "Years": ["2018 - 2019"],
    "Thesis": ["Cyclooxygenase-1 as an anti-stroke target: Potential inhibitor identification and non-synonymous single nucleotide polymorphism analysis"],    
    "Focus": ["Structural bioinformatics, mutation analysis, computational drug discovery"]
})

bsc_data = pd.DataFramep({
    "Degree": ["MSc in Biochemistry"],
    "Institution": ["University of Zimbabwe"],
    "Years": ["2012 - 2016"],
    "Thesis": ["dsRNA analysis of sweet potato to index for unknown viruses"],    
    "Focus": ["Lab techniques, Tissue culture, Molecular biology and Chemistry"]

# weather_data = pd.DataFrame({
#     "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
#     "Temperature (°C)": [25, 10, -3, 15, 30],
#     "Humidity (%)": [65, 70, 55, 80, 50],
#     "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
# })

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Dr. Tendai Muronzi"
    field = "Bioinformatics"
    institution = "Rhodes University, South Africa"
    summary = "Highly motivated computational biologist and biochemist with a Ph.D in Bioinformatics" 

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    st.write(f"**Summary:** {summary}")
    
    st.image(
    "https://raw.githubusercontent.com/muronzit/css_streamlit_2026/main/pexels-myburgh-4816921.jpg",
    caption="Photo by Myburgh (Pexels)",
    use_column_width=True
)

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")
    st.write("Skip if no publications yet") 

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "Education":
    st.title("Education")
    st.sidebar.header("Degree Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a degree", 
        ["PhD in Bioinformatics", "MSc in Bioinformatics", "BSc in Biochemistry"]
    )

    if data_option == "PhD in Bioinformatics":
        st.write("### Physics Experiment Data")
        st.dataframe(physics_data)
        # Add widget to filter by Energy levels
        energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
        filtered_physics = physics_data[
            physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
        ]
        st.write(f"Filtered Results for Energy Range {energy_filter}:")
        st.dataframe(filtered_physics)

    elif data_option == "MSc in Bioinformatics":
        st.write("### Astronomy Observation Data")
        st.dataframe(astronomy_data)
        # Add widget to filter by Brightness
        brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
        filtered_astronomy = astronomy_data[
            astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
        ]
        st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
        st.dataframe(filtered_astronomy)

    elif data_option == "BSc in Biochemistry":
        st.write("### Molecular Dynamics Simulation Data")
        rmsd_range = st.slider(
        "Filter by RMSD (Å)",
        float(md_data["RMSD (Å)"].min()),
        float(md_data["RMSD (Å)"].max()),
        (float(md_data["RMSD (Å)"].min()), float(md_data["RMSD (Å)"].max()))
        )
        filtered_md = md_data[
        md_data["RMSD (Å)"].between(rmsd_range[0], rmsd_range[1])
        ]
        st.write(f"Frames with RMSD in range {rmsd_range}:")
        st.dataframe(filtered_md)

    # elif data_option == "Weather Data":
    #     st.write("### Weather Data")
    #     st.dataframe(weather_data)
    #     # Add widgets to filter by temperature and humidity
    #     temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    #     humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
    #     filtered_weather = weather_data[
    #         weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
    #         weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
    #     ]
    #     st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
    #     st.dataframe(filtered_weather)
        
        

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "tendai.muronzi@ru.ac.za"

    st.write(f"You can reach me at {email}.")















