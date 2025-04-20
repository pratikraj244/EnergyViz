import streamlit as st
import pandas as pd
def main():
    st.markdown("""
    <style>
    /* Sidebar background and text */
    [data-testid="stSidebar"] {
        background-color: #013e7d;
    }
    
    /* Make ALL sidebar text white */
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Headings color */
    h1, h2, h3, h4 {
        color: #007BFF !important;
    }
    
    </style>
    """, unsafe_allow_html=True)
    st.header("The data")
    st.write("For analysis and prediction of the data, one should have an idea of the dataset.Therefore, in this page,the description of the dataset will give an idea about the contents in it. ")
    data = pd.read_csv(r"monthly_electric_data.csv")
    st.dataframe(data,hide_index=True)
    st.subheader("Overview")
    st.write("This dataset provides detailed monthly data related to the power sector across various states and union territories of India. It captures information spanning electricity capacity, generation, and related metrics, structured in a long-format layout ideal for time-series and comparative analysis.")
    st.subheader("Geographical and Temporal Coverage")
    st.write("Each row in the dataset is associated with a specific Indian state or union territory, identified by both full name and code. The data is recorded monthly, with each entry corresponding to a specific date (in a month-year format), allowing for longitudinal analysis over time and comparison across regions.")
    st.subheader("Data Categories and Variables")
    st.write("The dataset is divided into major categories such as emissions and possibly others (like Generation, depending on other entries). Within each category, subcategory like “Fuel” break the data down by type of energy source — for example, Fossil, Clean, Renewables, or specific groupings like Gas and Other Fossil. The variable column identifies what specific aspect is being measured (e.g., renewable energy capacity).")
    st.subheader("Measurements and Units")
    st.write(f"Values in the dataset are measured using units like % for power sector emissions and electricity generation, for energy generated. These numerical values represent the actual performance of the power sector in each region and time period.")
    st.subheader("Purpose and Usefulness")
    st.write("This dataset is highly valuable for researchers, policymakers, and energy analysts aiming to understand the progress and distribution of electricity infrastructure in India. It supports insights into regional disparities, growth in renewable energy, shifts in fossil fuel dependence, and the effectiveness of energy policies over time.")
if __name__ == "__main__":
    main()
