# importa bibliotecas
import pyautogui
import time

# tempo que cada comando demora para executar
pyautogui.PAUSE = 1

# instruções
pyautogui.press('win')
pyautogui.write('vscode')
pyautogui.press('enter')

# espera 10 segundos para abrir o vscode e continuar com os comandos
time.sleep(10)

# continua as instruções
pyautogui.hotkey('ctrl', 'shift', "'")
pyautogui.write('git init')
pyautogui.press('enter')
pyautogui.write('git add .')
pyautogui.press('enter')
pyautogui.write('git commit -m "Versão 1.0"')
pyautogui.press('enter')
pyautogui.write('git branch -M main')
pyautogui.press('enter')
pyautogui.write('git remote add origin https://github.com/jaianeoliveira581/automacao_repositorio.git')
pyautogui.press('enter')
pyautogui.write('git push -u origin main')
pyautogui.press('enter')