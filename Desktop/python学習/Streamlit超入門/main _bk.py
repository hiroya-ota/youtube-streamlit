from optparse import Option
from turtle import right
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Strealit 超入門')
st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})
#st.write(df)
#st.table(df)
#st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a','b','c']
)
#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    columns=['lat','lon']
)
#st.map(df)


st.write('Image画像')

if st.checkbox('Show Image'):
    img = Image.open('111.jpg')
    st.image(img, caption='Imageです', use_column_width=True)


st.write('Intaractibe Widget')

option = st.selectbox(
    'あなたが好きな数字を教えて下さい',
    list(range(1,11))
)
'あなたの好きな数字は',option,'です'

option= st.text_input('あなたの趣味をおしえてください')
'あなたの趣味は',option,'です'

con = st.slider('あなたの調子は？', 0,100,50)
'コンディション:', con

left_column, right_columns = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_columns.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせを書く1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせを書く2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせを書く3')


st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0) 

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
