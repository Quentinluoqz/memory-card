import streamlit as st
import time

# 1. 页面配置
st.set_page_config(page_title="To YOU", page_icon="✨",
layout="centered")
st.markdown("""
    <style>
    /* 1. 全局背景色（保持之前的黑色电影感） */
    .stApp {
        background-color: #0e1117;
        color: white;
    }
    
    /* 2. 专门修改按钮的样式 */
    div.stButton > button {
        background-color: #ff4b4b; /* 按钮背景色：新年红 */
        color: white;              /* 按钮文字色：白色 */
        border-radius: 20px;       /* 让按钮变圆润一点 */
        border: 2px solid #ff4b4b; /* 边框颜色 */
        font-weight: bold;         /*文字加粗 */
        padding: 10px 20px;        /* 增加按钮内部空间 */
        transition: all 0.3s;      /* 让鼠标放上去的变色更丝滑 */
    }

    /* 3. 鼠标悬停在按钮上时的样式 */
    div.stButton > button:hover {
        background-color: #ff0000; /* 鼠标放上去变深红 */
        color: #ffff00;            /* 文字变金黄色 */
        border-color: #ffff00;     /* 边框变金黄色 */
    }
    </style>
    """, unsafe_allow_html=True)
# 2. 隐藏无关菜单
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {
        background-color: #0e1117; /* 黑色背景更有电影感 */
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 标题区
st.title("🎞️ 2025")
st.caption("往下滑👇")

# 4. 背景音乐 (设置 autoplay 尽量自动播放，但在部分手机浏览器需手动点)
# 替换为你的音乐文件路径，或者网络链接
audio_file = open('方大同-才二十三-臻品母带2.0.mp3', 'rb') # 假设你本地有名为 bgm.mp3 的文件
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3', start_time=0)

# 5. 回忆照片墙 (使用 Expander 折叠，或者直接列出)
st.header("📸 ")

col1, col2, col3 = st.columns(3)
with col1:
    # 替换为你的照片文件名
    st.image("7.jpg",  use_column_width=True)
    st.image("3.jpg",  use_column_width=True)
with col2:
    st.image("8.jpg",  use_column_width=True)
    st.image("5.jpg",  use_column_width=True)
with col3:
    st.image("9.jpg",  use_column_width=True)
    st.image("6.jpg",  use_column_width=True)

# 7. 心愿与祝福 (交互环节)
st.divider() # 分割线
st.header("💌 ")

# 制造一点神秘感，让对方点击才显示
if st.button("点我"):
    st.balloons() # 再次调用气球特效
    
    st.markdown("""
    ###     To whisky(hh莫名想起你那小号）
    新年快乐🥳
    
    永远开心
    
    *Always by your side.*
    """)

# 底部署名
st.markdown("---")
st.markdown("*Made by lqz*")
