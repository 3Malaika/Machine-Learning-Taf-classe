import streamlit as st
st.title("Welcome to the BMI calculatrice")

weight = st.number_input('Entrer un nombre en kg')
status = st.radio('select your height format :',('cms','meters','feet'))

try:
    if status == 'cms':
        height = st.number_input('cms')
        bmi = weight/((height/100)**2)
    elif status == 'meters':
        height = st.number_input('meters')
        bmi = weight/((height**2))
    else:
        height = st.number_input('cms')
        bmi = weight/((height/3.2)**2)
except:
    print('Zero division error')

if(st.button('Calculate BMI')):
    st.write('Your BMI index is {}'.format(round(bmi)))
    if bmi < 16 :
        st.error('You skiny ass! Damn bitch')
    elif (bmi >=16 and bmi<18.5):
        st.warning('C bien ma puce ')
    elif (bmi >=18.5 and bmi<25):
        st.success('C bien ma puce ')
    elif (bmi >=25 and bmi<30):
        st.warning('Degonffle gros ballon')
    else:
       st.error('You skiny ass! Damn bitch')