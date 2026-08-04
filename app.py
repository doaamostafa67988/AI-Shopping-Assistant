import streamlit as st
from crew.crew_setup import run_crew

st.title("AI Shopping Assistant")
product = st.text_input("Enter the product name")
sites= st.multiselect("Select websites to search", ["Amazon", "eBay", "Walmart", "Noon", "Jumia"])

if st.button("Recommend Products"):

    if product :

        with st.spinner("Finding the best products for you..."):
            result = run_crew(product, sites)

        st.subheader("Best Products Found:")
        if hasattr(result, "raw"):
            output = result.raw
        elif hasattr(result, "task_output"):
            output = result.task_output[-1].raw
        else:
            output = str(result)

        st.markdown(output)
        