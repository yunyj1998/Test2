# Libraries
import streamlit as st
from PIL import Image

# Confit
st.set_page_config(page_title='YYJ Test', page_icon=':bar_chart:', layout='wide')

#Title
st.title("yyj test Portfolio dashboard")

# Content
c1  = st.columns(1)

image1 = Image.open("images/123.png.").resize((200, 200))


c1.image(image1)


st.write(
    """
    ### Welcome to my portfolio site.
**This site was created by a young man in his 20s who dreams of becoming a data analyst.**
    """
)

st.subheader('pt')
st.write(
    """
    The data for this cross-chain comparison were selected from the [**Flipside Crypto**](https://flipsidecrypto.xyz)
    data platform by using its **REST API**. These queries are currently set to **re-run every 24 hours** to cover the latest
    data and are imported as a JSON file directly to each page. The data were selected with a **1 day delay** for all
    blockchains to be in sync with one another. The codes for this tool are saved and accessible in its 
    [**GitHub Repository**](https://github.com/alitaslimi/cross-chain-monitoring).

    It is worth mentioning that a considerable portion of the data used for this tool was manually decoded from the raw
    transaction data on some of the blockchains. Besides that, the names of addresses, DEXs, collections, etc. are also
    manually labeled. As the queries are updated on a daily basis to cover the most recent data, there is a chance
    that viewers encounter inconsistent data through the app. Due to the heavy computational power required to execute
    the queries, and also the size of the raw data being too large, it was not feasible to cover data for a longer period,
    or by downloading the data and loading it from the repository itself. Therefore, the REST API was selected as the
    proper form of loading data for the time being.
    """
)

st.subheader('Future Works')
st.write(
    """
    This tool is a work in progress and will continue to be developed moving forward. Adding other blockchains,
    more KPIs and metrics, optimizing the code in general, enhancing the UI/UX of the tool, and more importantly,
    improving the data pipeline by utilizing [**Flipside ShroomDK**](https://sdk.flipsidecrypto.xyz/shroomdk) are
    among the top priorities for the development of this app. Feel free to share your feedback, suggestions, and
    also critics with me.
    """
)

c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Data Analyst: [@AliTslm](https://twitter.com/AliTslm)**', icon="💡")
with c2:
    st.info('**GitHub: [@alitaslimi](https://github.com/alitaslimi)**', icon="💻")
with c3:
    st.info('**Data: [Flipside Crypto](https://flipsidecrypto.xyz)**', icon="🧠")