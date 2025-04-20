import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import datetime as dt
import pydeck as pdk
import geopandas as gpd
from shapely import wkt
from sklearn.preprocessing import MinMaxScaler
import json
from prophet import Prophet
def main():
    st.markdown("""
    <style>
    /* Sidebar styling - always blue with white text */
    [data-testid="stSidebar"] {
        background-color: #013e7d !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Headings color */
    h1, h2, h3, h4 {
        color: #007BFF !important;
    }
    
    /* ===== BASE DROPDOWN STYLES ===== */
    /* These will be overridden by the JavaScript theme detection */
    div[data-baseweb="select"] > div {
        border-radius: 25px !important;
        border: 2px solid #007BFF !important;
    }
    
    /* ===== JAVASCRIPT THEME DETECTION ===== */
    <script>
    function applyThemeStyles() {
        // Check if dark theme is active
        const isDark = document.body.classList.contains('st-emotion-cache-fg4pbf');
        
        // Select all dropdown containers
        const dropdowns = document.querySelectorAll('div[data-baseweb="select"] > div');
        
        dropdowns.forEach(dropdown => {
            if (isDark) {
                // Dark theme styles
                dropdown.style.backgroundColor = 'black';
                dropdown.style.color = 'white';
                
                // Find the selected value div and style it
                const selectedValue = dropdown.querySelector('div');
                if (selectedValue) {
                    selectedValue.style.color = 'white';
                }
            } else {
                // Light theme styles
                dropdown.style.backgroundColor = 'white';
                dropdown.style.color = 'black';
                
                // Find the selected value div and style it
                const selectedValue = dropdown.querySelector('div');
                if (selectedValue) {
                    selectedValue.style.color = 'black';
                }
            }
        });
        
        // Style dropdown menus
        const menus = document.querySelectorAll('div[data-baseweb="menu"]');
        menus.forEach(menu => {
            if (isDark) {
                menu.style.backgroundColor = 'black';
            } else {
                menu.style.backgroundColor = 'white';
            }
        });
        
        // Style menu items
        const menuItems = document.querySelectorAll('div[data-baseweb="menu"] > div > div');
        menuItems.forEach(item => {
            if (isDark) {
                item.style.backgroundColor = 'black';
                item.style.color = 'white';
            } else {
                item.style.backgroundColor = 'white';
                item.style.color = 'black';
            }
        });
    }
    
    // Run initially
    applyThemeStyles();
    
    // Run whenever the theme might change
    new MutationObserver(applyThemeStyles).observe(document.body, {
        attributes: true,
        attributeFilter: ['class']
    });
    </script>
    
    /* ===== COMMON STYLES ===== */
    
    </style>
    """, unsafe_allow_html=True)
    st.header("Forecasting and Prediction")
    st.write("Forecasting and prediction of the data in this page, will provide suitable analysis, that explores the historical and forecasted patterns of energy sources usage (in percentage) across different states and years using time series modeling. The primary objective is to evaluate trends and provide insight into regional and temporal changes in energy sources reliance.")
    st.subheader("Filters")
    st.write(f"Categories: In categories filter, Electricity Generation means the amount of electricity produced in % by selected energy resources. Power sector emission means the amount of CO2 released from the energy resource in %. ")
    st.write("source: This filter is to select different energy sources such as Coal,natural gas, solar, wind, bioenergy, etc.")
    st.write("region: In this filter you can select regions of India such as North, Eastern, Central, Southern, Western and North-Eastern regions. On selecting any region, state filter will contain that states that are present in that selected region, eg: On selecting West region, state filter will contain states of Western region of India and so on.")
    col1,col2,col3 = st.columns(3)
    with col1:
       drop3 = st.selectbox("select category",["Power sector emissions","Electricity generation"])
    with col2:
       drop4 = st.selectbox("select source",["Bioenergy","Coal","Gas","Hydro","Nuclear","Other Fossil", "Other Renewables","Solar","Wind"])
    with col3:
       drop5 = st.selectbox("select region:",["North","East","West","South","Central","North-East"])
    data = pd.read_csv(r"india_monthly_full_release_long_format.csv")
    data1 = data[data["Subcategory"] == "Fuel"]
    data2 = data1[data["Unit"] == "%"]
    xyz = data2['Variable'].unique() 
    for value in xyz:
       data2[value] = np.nan  # or pd.NA if you prefer pandas nullable type

    # Fill the new columns with values based on the 'Variable' column
    for index, row in data2.iterrows():
       if row['Variable'] in xyz:  # To avoid KeyError if a value is missing in variable_values
          data2.loc[index, row['Variable']] = row['Value']
    data3 = data2[data2["Category"] == drop3]
    data3 = data3[data3["Unit"] == "%"]
    data3["Value"] = data3.groupby(["State", "Date"])["Value"].transform(lambda x: 100 * x / x.sum())
    data4 = data3[data3["Variable"] == drop4]
    st.subheader("State wise forecasting")
    st.write("On selecting the state, after the region, along with categories and energy resources, various plots of actual and predicted data are provided, to gain meaningful insight.")
    if drop5 == "North":
       place = st.selectbox("state/UT", ["Punjab", "Delhi","Jammu and Kashmir","Himachal Pradesh","Haryana","Uttarakhand","Uttar Pradesh","Chandigarh","Ladakh"])
    if drop5 == "West":
       place = st.selectbox("state/UT", ["Goa", "Maharashtra","Rajasthan","Gujarat","Lakshadweep","Dadra and Nagar Haveli and Daman and Diu"])
    if drop5 == "East":
       place = st.selectbox("state/UT", ["Bihar", "Jharkhand","Odisha","West Bengal","Andaman and Nicobar"])
    if drop5 == "South":
       place = st.selectbox("state/UT", ["Andhra Pradesh", "Karnataka","Kerala","Tamil Nadu","Puducherry"])
    if drop5 == "Central":
       place = st.selectbox("state/UT", ["Madhya Pradesh", "Chhattisgarh"])
    if drop5 == "North-East":
       place = st.selectbox("state/UT", ["Arunachal Pradesh", "Assam","Manipur","Meghalaya","Mizoram","Nagaland","Sikkim","Tripura"])
    if place:
       data5 = data4[data4["State"] == place]
       data5 = data5[["Date",f"Value"]]
       data5.fillna(0)
       #data5
       model = Prophet(interval_width=0.95)
       data5["Date"] = pd.to_datetime(data5["Date"], format='%d-%m-%Y')
       model.fit(data5.reset_index().rename(columns={'Date': 'ds', 'Value': 'y'}))
       future_dates = model.make_future_dataframe(periods=40, freq='MS') # Changed my_model to model
       forecast = model.predict(future_dates) # Changed my_model to model
       forecast = forecast[forecast["ds"] > "2024-11-01"]
       forecast['yhat'] = forecast['yhat'].clip(lower=0)
       dx1 = pd.DataFrame({"Date":forecast["ds"],"pred_mean_%":forecast["yhat"]})
       dx1["Date"] = pd.to_datetime(dx1["Date"], format='%d-%m-%Y')
       dx2 = pd.concat([data5,dx1],axis=0)
       f = go.Figure()
       st.subheader("Monthly analysis")
       st.write(f"In this plot, month wise data of {drop3} of mean % of {drop4}, of place {place}, is displayed to gain meaningful insight. Along with actual data, predicted data is also displayed. This plot can also be traced, to gain vital information. You also need to note that data of certain month in some state is not recorded. Therefore, graph will not plot those data.")
       f.add_trace(go.Scatter(x=dx2["Date"],y=dx2["Value"],name="actual"))
       f.add_trace(go.Scatter(x=dx2["Date"],y=dx2["pred_mean_%"],name="forecast"))
       f.update_layout(yaxis=dict(title=dict(text=f"values of mean % of {drop4}")))
       f.update_layout(xaxis=dict(title=dict(text="Date")))
       st.plotly_chart(f,use_container_width=True,height=200)
       st.subheader("Yearly analysis")
       st.write(f"In yearly analysis, actual and predicted yearly data will be displayed. This data contains yearly mean % of {drop3} of {drop4} in {place}. It will be suitable to identify and observe amount of production as well as environmental consumptions in usage of {drop4}, for each state.")

       start_date = '2019-01-01'
       end_date = '2024-11-01'
       data5["Date"] = pd.to_datetime(data5["Date"],format='%d-%m-%Y').dt.normalize()
       data6 = data5[(data5["Date"] >= start_date) & (data5["Date"] <= end_date)]
       data7 = data6.groupby(data6["Date"].dt.year)["Value"].mean().reset_index()
# Rename columns for clarity
       data7.columns = ["Year", f"Average Value"]
       data7.fillna(0)

       start_date = dx1["Date"].min()
       end_date = dx1["Date"].max()
       dx1["Date"] = pd.to_datetime(dx1["Date"],format='%d-%m-%Y').dt.normalize()
       dx11 = dx1[(dx1["Date"] >= start_date) & (dx1["Date"] <= end_date)]
       dx21 = dx11.groupby(dx11["Date"].dt.year)["pred_mean_%"].mean().reset_index()
# Rename columns for clarity
       dx21.columns = ["Year", f"predicted Value"]
       dx21.fillna(0)
       final = pd.concat([data7,dx21],axis=0)
       
       f = go.Figure()
       f.add_trace(go.Bar(x=final["Year"],y=final["Average Value"],name="actual"))
       f.add_trace(go.Bar(x=final["Year"],y=final["predicted Value"],name="forecast"))
       f.update_layout(yaxis=dict(title=dict(text=f"yearly mean % of {drop4}")))
       f.update_layout(xaxis=dict(title=dict(text="Date")))
       st.plotly_chart(f,use_container_width=True,height=200)

    st.header("Region-Wise forecasting")
    st.write(f"On selecting the region according to the user, predicted mean % of {drop4}, of the states present in that region will be represented in graphical form.These analysis, presents the yearly mean percentage of {drop4} predicted by algorithm, across selected northern Indian states and union territories. The dataset highlights considerable usage and drawbacks of {drop4} in future.")
    latitudes = []
    longitudes = []
    if drop5 == "West":
       state_arr = ["Rajasthan","Gujarat","Maharashtra","Goa","Lakshadweep","Dadra and Nagar Haveli and Daman and Diu"]
       latitudes = [27.0238, 22.2587, 19.7515, 15.2993, 10.5667, 20.4283]
       longitudes = [74.2179, 71.1924, 75.7139, 74.1240, 72.6369, 72.8397]
    if drop5 == "North":
       state_arr = ["Punjab", "Delhi","Jammu and Kashmir","Himachal Pradesh","Haryana","Uttarakhand","Uttar Pradesh","Chandigarh","Ladakh"]
       latitudes = [31.1471, 28.6139, 33.7782, 31.1048, 29.0588, 30.0668, 26.8467, 30.7333, 34.1526]
       longitudes = [75.3412, 77.2090, 76.5762, 77.1734, 76.0856, 79.0193, 80.9462, 76.7794, 77.5770]
    if drop5 == "East":
       state_arr = ["Bihar", "Jharkhand","Odisha","West Bengal","Andaman and Nicobar"]
       latitudes = [25.0961, 23.6102, 20.9517, 22.9868, 11.7401]
       longitudes = [85.3131, 85.2799, 85.0985, 87.8550, 92.6586]
    if drop5 == "South":
       state_arr = ["Andhra Pradesh", "Karnataka","Kerala","Tamil Nadu","Puducherry"]
       latitudes = [15.9129, 15.3173, 10.8505, 11.1271, 11.9139]
       longitudes = [79.7400, 75.7139, 76.2711, 78.6569, 79.8145]
    if drop5 == "Central":
       state_arr = ["Madhya Pradesh", "Chhattisgarh"]
       latitudes = [22.9734, 21.2787]
       longitudes = [78.6569, 81.8661]
    if drop5 == "North-East":
       state_arr = ["Arunachal Pradesh", "Assam","Manipur","Meghalaya","Mizoram","Nagaland","Sikkim","Tripura"]
       latitudes = [28.2180, 26.2006, 24.6637, 25.4670, 23.1645, 26.1584, 27.5330, 23.9408]
       longitudes = [94.7278, 92.9376, 93.9063, 91.3662, 92.9376, 94.5624, 88.5122, 91.9882]
    state_arr1 = state_arr
    rr=[]
    rs=[]
    arr_fr1 = []
    for i in state_arr1:
      d5 = data4[data4["State"] == i]
      d5 = d5.groupby("Date")["Value"].mean()
      d5.index = pd.to_datetime(d5.index, format='%d-%m-%Y')
      d5 = d5.dropna()
      h2 = d5.groupby(d5.index.year).mean()
      rs.append(i)
      rr.append(h2.mean().item())
      if len(d5) > 0:
           my_model = Prophet(interval_width=0.95)
           my_model.fit(d5.reset_index().rename(columns={'Date': 'ds', 'Value': 'y'}))
           future_dates = my_model.make_future_dataframe(periods=40, freq='MS')
           forecast = my_model.predict(future_dates)
           forecast['yhat'] = forecast['yhat'].clip(lower=0)
           forecast["yhat"].mean()
           arr_fr1.append(forecast["yhat"].mean().item())
    data8 = pd.DataFrame({"states":rs,"actual value":rr})
    #data8
    data9 = pd.DataFrame({"states":rs,"predicted value":arr_fr1})
    data10 = pd.concat([data8,data9],axis=0)
    #data10
    f = go.Figure()
    f.add_trace(go.Bar(x=data8["states"],y=data8["actual value"],name="actual"))
    f.add_trace(go.Bar(x=data9["states"],y=data9["predicted value"],name="forecast"))
    f.update_layout(yaxis=dict(title=dict(text=f"yearly mean % of {drop4}")))
    f.update_layout(xaxis=dict(title=dict(text="Date")))
    st.plotly_chart(f,use_container_width=True,height=200)
    st.write("An interactive 3D map visualization is also used along with bar plots. In this visualization, each state's predicted value is represented with colour intensity and heights. Larger the values, greater is the height, and colour changes from green to red.")
    st.write("     ")
    state_data = pd.DataFrame(
       {
          "state":state_arr1,
          "value":arr_fr1,
          "latitudes":latitudes,
          "longitudes":longitudes
       }
    )
    val_min,val_max = state_data["value"].min(),state_data["value"].max()
    state_data["color_r"] = ((state_data["value"]) / (val_max) * 255).astype(int)
    state_data["color_g"] = (255 - state_data["color_r"]).astype(int)  # Green intensity
    state_data["color_b"] = 100  # Keep blue constant
    state_data["color_a"] = 180
    layer = pdk.Layer(
    "ColumnLayer",
    data=state_data,
    get_position=['longitudes','latitudes'],
    get_elevation = "value*20",
    elevation_scale=800,
    radius=62000,
    get_fill_color=["color_r", "color_g", "color_b", "color_a"],
    #elevation_range="AQI",
    pickable=True,
    extruded=True,
    auto_highlight=True
    )
    vi = pdk.ViewState(latitude=state_data["latitudes"].mean(),longitude= state_data["longitudes"].mean(),zoom=4,pitch=45)
    xyz = pdk.Deck(layers=[layer],initial_view_state=vi,tooltip={"text": "{state}\nValue: {value}"})
    st.pydeck_chart(xyz)
       
if __name__ == "__main__":
    main()
