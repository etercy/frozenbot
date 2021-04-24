# importa o módulo "spammer" (pyautogui) e o time,
# pra não zoar o código e você conseguir trocar de tela
import pyautogui, time

# tempo que você quer na operação de troca de telas
time.sleep(5)

# arquivo com as palavras que você vai spammar
movie = open("frozen.txt" , 'r')
# iteração entre todas as palavras do roteiro
for word in movie:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

