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

> [!NOTE]\
> <i><b>Можна використати Docker.<b></i>

> [!WARNING]\
>Для запуску потрібно мати встановлений та запущений Xming<br><b>Необхідністю запуску графічного інтерфейсу (GUI)</b>
1. Команда для інсталяції: docker pull denyskulida/thread
2. Команда для запуску: docker run -e DISPLAY=host.docker.internal:0.0 -v /tmp/.X11-unix:/tmp/.X11-unix denyskulida/thread

## Контакт
> [!NOTE]\
>Якщо Вам потрібна консультація або допомога по використанні програми: Telegram: @DeLemse

##

<p align="center">
  <img width="450px" height='250px' src="./img/Threads.png" align="center" alt="Space Defenders" />
  <h2 align="center">Threads</h2>
</p>
<h2><p align="center">⚜️See how threads work in the process⚜️</p></h2>
<table>
  <td>
    <img src="./img/thred.jpg" alt="Image";">
  </td>
  <td>
      <h3>This program demonstrates<br>working of 4 rectangles<br>
       which vary by<br>sizes and over each<br>of them 
       are their areas.  Each<br>rectangle<br>is a flow, common<br>
       the area is also a separate stream.  The general one is shown below 
       area and the «Start» button is shown - for starting the stream
       "Clear" - to stop the flow.  <br>These buttons can be used to<br> control streams.</h3>
  </td>
</table>

# Installation
1. Clone the repository: `git clone https://github.com/kulidaden/threads.git`
2. Then these commands: `cd threads` -> `pyinstaller --onefile --distpath ./ thread.py` -> `./thread.exe`

> [!NOTE]\
> <i><b>You can use Docker.<b></i>

> [!WARNING]\
>Xming must be installed and running to run<br><b>Need to run a graphical user interface (GUI)</b>
1. Command for installation: docker pull denyskulida/thread
2. Command to run: docker run -e DISPLAY=host.docker.internal:0.0 -v /tmp/.X11-unix:/tmp/.X11-unix denyskulida/thread

## Contact
> [!NOTE]\
>If you need advice or help using the program: Telegram: @DeLemse

