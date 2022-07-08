import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('Chases Dinner')

streamlit.header('Chases Favorites')

streamlit.text("Moms Special Pancakes.")
streamlit.text("No place Like Home Burger.")
streamlit.text("Chase Loves his Moma Deluxe Smoothie.")

streamlit.header('Build Your Own Fruit Smoothie')

streamlit.text("Moms Special Pancakes.")

streamlit.dataFrame(my_fruit_list)
