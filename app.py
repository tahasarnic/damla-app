import streamlit as st
st.title("Damla'nın Aplikasyonuna Hoş Geldiniz 🌼")
st.image("img/ergoterapi.png", use_container_width=True)
st.balloons()
st.set_page_config(layout="wide")


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

st.markdown("#### 7 ay sonra.. D❤️E")

# Radio button to choose between YouTube video or text
option1 = st.radio(
    "Ne yapmak istersin?",
    ("Damloşun doğum günü için Eren'in dileğini görmek istiyorum 🧞‍♂️", "Şarkımızı dinlemek istiyorum 🎶")
)

# Display content based on the radio button selection
if option1 == "Damloşun doğum günü için Eren'in dileğini görmek istiyorum 🧞‍♂️":
    # Embed a Image
    st.image("img/damlos_eros.png", use_container_width=True)
else:
    # Embed a YouTube video
    st.video("https://www.youtube.com/watch?v=HMwPywh7-VY&list=RDHMwPywh7-VY&start_radio=1")