import tkinter as tk

def on_button_click():
    label.config(text="버튼이 눌렸습니다!")

# 기본 윈도우 생성
root = tk.Tk()

# 라벨 생성
label = tk.Label(root, text="안녕하세요!")

# 버튼 생성
button = tk.Button(root, text="클릭하세요", command=on_button_click)

# 위젯 배치
label.pack()
button.pack()

# 이벤트 루프 시작
root.mainloop()