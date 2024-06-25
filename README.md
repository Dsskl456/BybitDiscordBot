# Instructions
Create your own Discord bot on https://discord.com/developers/applications with sending messages permission and connect it with discord sever

copy channel id from channel you want bot to send messages

![image](https://github.com/Dsskl456/BybitDiscordBot/assets/94761798/9728a2b5-39c6-4ade-8e29-eb4d666a7a53)


if you can't see this option turn on developer mode in settings>advanced
![image](https://github.com/Dsskl456/BybitDiscordBot/assets/94761798/004a3654-4926-46f4-96bf-6c1b2cbcbb0b)


in dcbot.py change CHANNEL_ID to your channel_id and BOT_TOEN to yours discord bot token in ""

![image](https://github.com/Dsskl456/BybitDiscordBot/assets/94761798/321bffc7-9ad9-4c49-b4c6-bc7421edcad7)

On Bybit.com create your api key (can be read-only and with USDC Contracts permission)
In Bybitcollect.py change KEY and SECRET to your bybit tokens in ""

![image](https://github.com/Dsskl456/BybitDiscordBot/assets/94761798/189f89c9-4553-439c-95a8-9574eb13bc64)


build docker using command 
"docker build -t bybitdiscordbot ."

![image](https://github.com/Dsskl456/BybitDiscordBot/assets/94761798/76c3dc04-c433-4e4c-8132-d2ed71fc014e)


run program inside container using command
"docker run bybitdiscordbot"

![image](https://github.com/Dsskl456/BybitDiscordBot/assets/94761798/128706d3-7ecf-420e-a70e-be1603532aee)


or using docker hub inside images tab by clicking run in actions
![image](https://github.com/Dsskl456/BybitDiscordBot/assets/94761798/116d1dce-37b5-455c-a513-4fa74a11a75d)

