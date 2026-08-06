import streamlit as st
from crew.crew_setup import run_crew

st.title("AI Shopping Assistant")
product = st.text_input("Enter the product name")
sites= st.multiselect("Select websites to search", ["Amazon", "eBay", "Walmart", "Noon", "Jumia"])

if st.button("Recommend Products"):

    if product.strip():

        with st.spinner("Finding the best products for you..."):
            try:
                result = run_crew(product.strip(), sites)
            except Exception as exc:
                st.error("The assistant could not fetch results.")
                st.exception(exc)
                st.stop()

        st.subheader("Best Products Found:")
        if hasattr(result, "raw"):
            output = result.raw
        elif hasattr(result, "tasks_output") and result.tasks_output:
            output = result.tasks_output[-1].raw
        else:
            output = str(result)

        if output and output.strip():
            st.markdown(output)
        else:
            st.warning("No products were returned. Try a more specific product name or different websites.")
    else:
        st.warning("Please enter a product name first.")
        
