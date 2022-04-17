import streamlit as st
import time


st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)
'Done!!!!!!!!!!!!!'

##
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2内容を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3内容を書く')

# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなた今の調子は?', 0, 10, 5)

# 'あなたの好きな趣味:' ,text
# 'コンディション:',condition

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img,caption='Test',use_column_width=True)
