import streamlit as st
st.set_page_config(layout="wide")
st.title("Damla'nın Aplikasyonuna Hoş Geldiniz 🌼")

st.markdown('### Sana yastık vermeden duramıyorum. İşte kanıtı 👇')
st.image("img/damla_asti.png", use_container_width=True)

# Radio button to choose between YouTube video or text
option = st.radio(
    "Ne yapmak istersin?",
    ("Şarkımı dinlemek istiyorum 🎶", "Akrostiş şiirimi okumak istiyorum 📝")
)

# Display content based on the radio button selection
if option == "Şarkımı dinlemek istiyorum 🎶":
    # Embed a YouTube video
    st.markdown("#### O gece söylemek istediklerim ektedir 👇")
    st.video("https://www.youtube.com/watch?v=xR05AUL9uvw")
else:
    # Display a text message
    st.text("Dün gördüm seni, bir insan hiç mi değişmez\nAh o gülüşün hiçbir şeye değişilmez\nManidar olurdu verseydim sana küçük bir yastık\nLa bebe diye kovalayabilirlerdi beni bir tık (şaka)\nAslında her şey seninle güzel, bu da bir gerçek artık")