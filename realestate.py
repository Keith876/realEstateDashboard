import pandas as pd
import streamlit as st

#page configuration
st.set_page_config(page_title="Real Estate data",
                   page_icon=":bar_chart:",
                   layout="wide")

df = pd.read_csv('Real_Estate.csv')


#SIDEBAR
st.sidebar.header("Please Filter Here:")
property_type = st.sidebar.multiselect(
    "Select the property:",
    options=df["property_type"].unique(),
    default=df["property_type"].unique()
    )

bedrooms = st.sidebar.multiselect(
    "Select the bedrooms:",
    options=df["bedrooms"].unique(),
    default=df["bedrooms"].unique()
    )

bathrooms = st.sidebar.multiselect(
    "Select the bathrooms:",
    options=df["bathrooms"].unique(),
    default=df["bathrooms"].unique()
    )

df_selection = df.query(
    "property_type == @property_type & bedrooms == @bedrooms & bathrooms == @bathrooms"
)

#Mainpage
st.title(":bar_chart: Properties")
st.markdown("##")

#Top KPI'S
average_sale_price = int(df_selection[" sale_price "].mean())
average_rating = round(df_selection["neighborhood_rating"].mean(),1)
star_rating = ":star:" * int(round(average_rating, 0))

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Average Sale Price:")
    st.subheader(f"US $ {average_sale_price:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating}")
with right_column:
    st.subheader("star rating:")
    st.subheader(f"{star_rating}")

    st.markdown("___")

st.dataframe(df_selection)












