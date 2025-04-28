# import streamlit as st
#
# st.title('☑️To-do App☑️')
#
# # 1. todo 입력칸 제공
# # 2. todos(session_state)에 새 todo 저장
# # 3. todos 목록화
# # 4. 완료한 todo는 checkbox를 통해 완료처리
#
# class Todo:
#     def __init__(self, task: str, done: bool=False):
#         self.task = task
#         self.done = done
#
#     def __repr__(self):
#         return f'Todo(task={self.task}, done={self.done})'
#
# def add_todo():
#     new_task = st.session_state["new_task"]
#     print(f'add_todo: new_task = {new_task}')
#     if new_task:
#         new_todo = Todo(new_task)
#         st.session_state["todos"].append(new_todo)
#         st.session_state["new_task"] = ""
#
# def toggle_done(index: int):
#     todo = st.session_state["todos"][index]
#     todo.done = not todo.done # 반전
#
#
# # todos 초기화
# if "todos" not in st.session_state:
#     st.session_state.todos: list[Todo] = []
#
# # 입력창
# # - key매개변수는 session_state 자동등록 및 관리
# # - on_change콜백함수는 사용자입력후 엔터를 누르면 지정한 함수를 자동호출
# st.text_input("새로운 할일 추가", key="new_task", on_change=add_todo)
#
# # 목록
# print(f'todos = {st.session_state["todos"]}')
# if st.session_state['todos']:
#     for i, todo in enumerate(st.session_state['todos']):
#         col1, col2 = st.columns([0.2, 0.8])
#         col1.checkbox("", value=todo.done, key=f"done_{i}", on_change=toggle_done, args=(i, ))
#         col2.markdown(f'~~{todo.task}~~' if todo.done else todo.task)
# else:
#     st.info('할일을 추가해보세요😊')


import streamlit as st

# 페이지 제목 설정
st.title("로그인 페이지")

# 입력 폼 생성
with st.form(key='login_form'):
    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type="password")
    submit_button = st.form_submit_button(label='로그인')

# 로그인 버튼 클릭시 실행
if submit_button:
    if username == "your_username" and password == "your_password":
        st.success("로그인 성공!")
        # 로그인 성공 시 후속 작업(예: 다른 페이지 이동 등)
    else:
        st.error("아이디 또는 비밀번호가 잘못되었습니다.")

















