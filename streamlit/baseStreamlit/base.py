import streamlit as st 
st.title("web application")
st.header("streamlit header")
st.text("texte de mali")
st.write("Ml App")
st.markdown("hello")
st.markdown("[Actu Cameroun ](http://actucameroun.com/)")
st.metric(label='wind speed', value='120ms', delta="+1.4ms")

st.video("../assets/Mushishi (Saison 1) - 05 VF.mp4")
st.image("../assets/647741.jpg")
state=st.checkbox('Ckeckbox',value=True)
if state:
    st.write("Your checbox")
else:
    pass
radio_btn = st.radio("Radio Button",("US","UK","Canada"))
btn = st.button('Click moi')
select = st.selectbox("Select box",("audi","bmw","ferari"))
multi_select = st.multiselect('c quoi ton enterprise preferée',('Microsoft','apple','Facebook'))

st.slider('*Ceci est un slider*', min_value=50, max_value=100,value=70)