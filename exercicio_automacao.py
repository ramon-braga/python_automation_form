import pyautogui

pyautogui.PAUSE = 0.5

pyautogui.sleep(3)

# Coordenadas
url_position_x = 496
url_position_y = 53
username_position_x = 588
username_position_y = 608

# Abrir navegador Edge
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")
pyautogui.sleep(1)
pyautogui.hotkey("alt", "space")
pyautogui.sleep(0.5)
pyautogui.press("x")


# Acessar site
pyautogui.click(url_position_x, url_position_y)
pyautogui.write("https://hashtagtreinamentos.com")
pyautogui.press("enter")

# Acessar área do curso de python
pyautogui.sleep(3)
curso_python_position = pyautogui.locateCenterOnScreen("curso_de_python.png")
pyautogui.sleep(1)
pyautogui.click(curso_python_position)

# Cadastro
pyautogui.sleep(1)
pyautogui.click(username_position_x, username_position_y)
pyautogui.write("Nome do usuario")
pyautogui.sleep(1)
pyautogui.press("tab")
pyautogui.write("email_do_usuario@dominio.com")
pyautogui.sleep(1)
pyautogui.press("tab")
pyautogui.write("(87)98765-1234")