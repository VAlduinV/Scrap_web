# Scrap_web
    
        _____                                                                                     
     __|___  |__    ______    _____     ____       _____           __  __  __    ______    ______  
    |   ___|    |  |   ___|  |     |   |    \    |     |         |  \/  \|  |  |   ___|  |      > 
    `-.`-.     |  |   |__   |     \   |     \    |    _|         |     /\   |  |   ___|  |     <  
    |______|  __|  |______|  |__|\__\  |__|\__\  |___|      ___  |____/  \__|  |______|  |______> 
        |_____|                                            |___|                                   
       
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Arial+Black&weight=500&pause=1000&color=17FF0C&center=true&vCenter=true&width=440&lines=Scrap_web)](https://git.io/typing-svg)

<div>

<h1>Web Scraping Quotes Project</h1>
<p>Проект використовує фреймворк Scrapy та BeautifulSoup для витягування даних з веб-сайту <a href="http://quotes.toscrape.com"><b>http://quotes.toscrape.com</b></a>.</p>

<h2>Дані</h2>
<p>Отримуємо дані про цитати та авторів. Для цитат ми збираємо текст цитати та ім'я автора. Для авторів ми збираємо ім'я автора та всі його цитати з сайту.</p>

<h2>Файли</h2>

<ul>
    <li><b style="color:blue;">quotes.json</b>: цей файл містить всі цитати з сайту. Кожна цитата містить текст цитати та ім'я автора.</li>
    <li><b style="color:yellow;">authors.json</b>: цей файл містить всіх авторів з сайту. Кожен автор містить своє ім'я та список його цитат з сайту.</li>
</ul>

<h2>Код</h2>
<p>Код складається з двох основних скриптів:</p>

<ul>
    <li><b style="color:blue;">quotes_spider.py</b>: цей скрипт використовує Scrapy для скрапінгу всіх цитат з сайту.</li>
    <li><b style="color:red;">authors_spider.py</b>: цей скрипт використовує Scrapy для скрапінгу всіх авторів з сайту.</li>
</ul>

<h2>Використання</h2>
<p>Щоб використати цей проект, ви повинні встановити Python та Scrapy.</p>
<p>Щоб запустити скрапери, виконайте наступні команди:</p>

<b>Перша команда:</b>
    
    scrapy crawl quotes -o quotes.json

<b>Друга команда:</b>

    scrapy crawl authors -o authors.json

<h2 style="background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); -webkit-background-clip: text; color: transparent;">Вимоги до системи:</h2>

<ul>
    <li><b>Python 3.6+</b></li>
    <li><b>Scrapy 2.4.1+</b></li>
</ul>

<p>Проект є прикладом використання <a href="https://scrapy.org/">Scrapy</a> та <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup</a> для скрапінгу веб-сайтів. Ви можете використовувати та модифікувати цей проект відповідно до ваших потреб.</p>
</div>