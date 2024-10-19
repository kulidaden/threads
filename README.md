<p align="center">
  <img width="450px" height='250px' src="./img/Threads.png" align="center" alt="Space Defenders" />
  <h2 align="center">Threads</h2>
</p>
<h2><p align="center">⚜️Глянь як працюють потоки в процесі⚜️</p></h2>
<table>
  <td>
    <img src="./img/thred.jpg" alt="Image";">
  </td>
  <td>
    <h3>Ця програма демонструє<br>роботу 4 прямокутників<br>
      які змінюються за<br>розмірами та над кожним<br>з них 
      є їхні площі. Кожен<br>прямокутник<br>це поток,загальна<br>
      площа теж окремий<br>поток. Знизу продемонстровано<br> загальну 
      площу та зображено кнопки<br>«Start»- для старту потоку<br>
      «Clear» - для зупинки потоку. <br>За допомогою цих кнопок можна<br> керувати потоками.</h3>
  </td>
</table>

# Інсталяція
1. Клонуйте репозиторій: `git clone https://github.com/kulidaden/threads.git`
2. Потім ці команди: `cd threads` -> `pyinstaller --onefile --distpath ./ thread.py` -> `./thread.exe`

# АБО 
### Можна використати Docker. 
> [!WARNING]\
>Для запуску потрібно мати встановлений та запущений Xming<br><b>необхідністю запуску графічного інтерфейсу (GUI)</b>
1. Команда для інсталяції: docker pull denyskulida/thread
2. Команда для запуску: docker run -e DISPLAY=host.docker.internal:0.0 -v /tmp/.X11-unix:/tmp/.X11-unix denyskulida/thread

   
## Використання
Програма демонструє роботу 4 прямокутників які змінюються за розмірами та над кожним з них є їхні площі. Знизу продемонстровано загальну площу та зображено кнопки «Start» - для старту потоку та «Clear» - для зупинки потоку.

## Контакт
Якщо Вам потрібна консультація або допомога по використанні програми: Telegram: @DeLemse

# Threads
 An example of using threads.

# Installation
1. Clone the repository: `git clone https://github.com/kulidaden/threads.git`
2. Then these commands: `cd threads` -> `pyinstaller --onefile --distpath ./ thread.py` -> `./thread.exe`

# OR 
### You can use Docker. 
> [!WARNING]\
>Xming must be installed and running to run
1. Command for installation: docker pull denyskulida/thread
2. Command to run: docker run -e DISPLAY=host.docker.internal:0.0 -v /tmp/.X11-unix:/tmp/.X11-unix denyskulida/thread 
## Usage
The program demonstrates the operation of 4 rectangles that change in size and above each of them are their areas.  The bottom shows the general area and shows the buttons "Start" - to start the flow and "Clear"- to stop the flow.

## Contact
If you need advice or help using the program: Telegram: @DeLemse

