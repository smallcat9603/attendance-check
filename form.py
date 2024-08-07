import streamlit as st
from datetime import datetime

st.title(':cat2: 出欠確認 (経営情報システム II)')

now = datetime.now()
current_date = now.strftime('%Y-%m-%d')
current_weekday = now.strftime('%A')
st.caption(f'{current_date} ({current_weekday})')

form = st.form('info')
id = form.text_input('学籍番号 *:')
name = form.text_input('名前 *:')
group = form.selectbox('クラス *:', ['A', 'B', 'C', 'D'], index=None, placeholder='ドロップダウンリストから選択')
note = form.text_input("補足 (遅刻の理由など):")

if form.form_submit_button("送信", type="primary"):
    if id.strip() == "" or name.strip() == "" or group.strip() == "":
        form.warning("必要な情報をご記入ください", icon='⚠')
        st.stop()
    else:
        st.write("ご協力いただき、ありがとうございました!")
