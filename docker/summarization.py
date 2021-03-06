#!/usr/bin/env python
# coding: utf-8

# In[1]:
from IPython import get_ipython

get_ipython().run_line_magic('config', 'IPCompleter.use_jedi = False')

# In[2]:


from transformers import MBartTokenizer, MBartForConditionalGeneration

model_name = "IlyaGusev/mbart_ru_sum_gazeta"
tokenizer = MBartTokenizer.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

# In[4]:


get_ipython().run_line_magic('pinfo', 'model.generate')

# tokenizer?

# [text],
#     src_lang="en_XX", # fairseq training artifact
#     return_tensors="pt",
#     padding="max_length",
#     truncation=True,
#     max_length=600


# In[9]:


article = '''[\'Ассоциации "Все вместе" составили Декларацию о добросовестности в сфере благотворительности при 
сборе средств через ящики-копилки.текст Декларации:"Настоящий документ претендует на то, чтобы выражать мнение 
профессиональной российской благотворительности.нами стоит задача донести до максимально широкой аудитории нашу 
оценку набирающей силу опасной практики. Нам представляется необходимым сформировать общую позицию и всеми средствами 
распространить ее как можно шире.идёт о практике сбора пожертвований от имени организаций в местах скопления людей 
(на улицах, в электричках, в пробках) как с применением внешних признаков благотворительного сбора (прозрачный ящик, 
фотографии подопечных, информация о фонде-сборщике и так далее), так и под видом "благотворительной продажи сувениров". 
Как правило, этим занимаются люди, выдающие себя за волонтеров, а на деле получающие процент от собранных денег – то 
есть коммерческие агенты, которые обманывают общественность.расследований, проведённых СМИ, 
показывают:— никаких подтверждений того, что собранные средства в полном или хотя бы значительном объеме доходят 
до нуждающихся, не существует;— большая часть собранных наличных денег изымается руководством лжеволонтёров 
в собственный карман;— в лучшем случае их небольшая часть используется для создания видимости благотворительной 
работы.практика признаётся нами порочной и недопустимой для прозрачной и профессиональной организации.сбор наличных 
денег на постоянной основе провоцирует их нецелевое использование и подрывает доверие к благотворительности в целом. 
Использование не заинтересованных в декларируемых гуманистических целях, получающих комиссионное вознаграждение 
работников (что не соответствует принципам Этического кодекса Ассоциации Фандрайзеров России) только
 усиливает негативный эффект. Случаи, когда нечистоплотные организации используют для такой формы фандрайзинга 
 наивных молодых людей, верящих, что собирают деньги на хорошее дело, тоже приводят к разочарованиям и дискредитации
  благотворительности.документом мы, члены Ассоциации "Все Вместе", предлагаем всем благотворительным организациям 
  подписаться под следующими утверждениями.– Мы однозначно осуждаем практику сбора наличных денег от имени организации 
  вне мест проведения организованных благотворительных мероприятий и вне стационарных ящиков для сбора наличных денег, 
  опечатанных и вскрываемых в присутствии независимых контролеров.– Мы не будем применять такого рода технологии для 
  сбора пожертвований.– Мы призываем общественность и частных жертвователей не вносить пожертвования деньгами вне мест 
  проведения организованных благотворительных мероприятий.– Мы призываем все честные организации присоединиться к этому 
  документу.мы призываем СМИ и просто небезразличных людей присоединиться к инициируемой нами информационной кампании и
донести до максимально широкой аудитории материалы, которые мы предложим в дальнейшем. На наших глазах ширится и 
крепнет мошенническое движение, ставящее под угрозу благотворительный сектор. Всякого мошенника рано или поздно 
разоблачают, но любые скандалы серьезно ударят и по всем нам, а значит — по нашим подопечным. Ушли годы, прежде 
   чем нам начали доверять – и если мы не будем сами бороться с обманом в благотворительной среде, то мы ничем не 
   будем отличаться в глазах общественности от тех, кто обманывает"."Все вместе" призывает благотворительные 
   организации присоединиться к данной инициативе и поставить свою подпись под Декларацией. Напишите нам на 
   info@wse-wmeste.ru.организации, подписавшие Декларацию:. Некоммерческая организация "Благотворительный Фонд "АдВИТА".
    Фонд "Благотворительное общество "Адреса милосердия". Благотворительный фонд "В твоих руках". Автономная 
    некоммерческая организация "Центр равных возможностей для детей-сирот "Вверх". Благотворительный фонд помощи 
    хосписам "Вера". Некоммерческая организация "Благотворительный фонд помощи нуждающимся гражданам "Весна в сердце".
     Благотворительный фонд "Во имя жизни" Помощь инвалидам — больным муковисцидозом". Благотворительный фонд 
     "ВОЛОНТЕРЫ В ПОМОЩЬ ДЕТЯМ-СИРОТАМ". Благотворительный фонд содействия решению проблем аутизма "Выход". 
Благотворительный фонд помощи детям с органическими поражениями центральной нервной системы "ГАЛЧОНОК". 
Благотворительный фонд помощи тяжелобольным людям "Гольфстрим". Межрегиональное молодежное общественное движение в
поддержку православных молодежных инициатив во имя святого благоверного князя Даниила "Даниловцы". Благотворительный 
фонд помощи детям, страдающим заболеванием буллезный эпидермолиз, "Дети БЭЛА". Региональная общественная организация 
по развитию художественных способностей детей-сирот "ХУДОЖЕСТВЕННЫЙ ЦЕНТР "ДЕТИ МАРИИ". Благотворительный фонд 
"Дети наши". Благотворительный фонд "Детская больница". Региональный благотворительный общественный фонд помощи детям с
врожденными заболеваниями сердца и нервной системы "Детские сердца". Фонд благотворительной помощи детям-сиротам и 
инвалидам "Димина Мечта". Межрегиональная общественная организация помощи детям с особенностями психоречевого развития 
и их семьям "Дорога в мир". Автономная некоммерческая организация "Центр социальных и культурно-просветительских 
услуг""Друзья общины святого Эгидия". Благотворительный Фонд помощи взрослым "Живой". Благотворительный фонд помощи 
детям с онкологическими и онкогематологическими заболеваниями "Жизнь". Некоммерческая организация Благотворительный 
фонд помощи детям-сиротам "Здесь и сейчас". Благотворительный фонд содействия семейному устройству детей-сирот "Измени 
одну жизнь". Благотворительный фонд "Кислород". Межрегиональная общественнаяволонтеров "Клуб волонтеров". Региональная 
общественная организация инвалидов и родителей детей-инвалидов "Ковчег".Благотворительный фонд помощи детям с 
онкологическими заболеваниями "Настенька". Фонд содействия гармонизации отношений животных и общества "НЕ ПРОСТО 
СОБАКИ". Благотворительный фонд содействия развитию социально-культурных инициатив и попечительства "Образ жизни". 
Благотворительный фонд помощи детям с онкогематологическими и иными тяжелыми заболеваниями "ПОДАРИ ЖИЗНЬ". 
Благотворительный фонд "Фонд помощи детям с нарушениями иммунитета "ПОДСОЛНУХ". Благотворительный Интернет-фонд Помоги.
Орг. Благотворительный фонд помощи социально незащищенным лицам имени святой преподобномученицы Великой Княгини 
Елизаветы "Православие и Мир". Автономная некоммерческая организация «Консультационно-методический центр комплексного 
сопровождения семей с детьми, нуждающихся в психолого-педагогической и медико-социальной помощи "Про-мама". 
Региональный благотворительный общественный фонд содействия духовному развитию общества "Предание". Автономная 
некоммерческая организация "РОСТ — развитие, образование, социализация и трудоустройство для воспитанников и выпусников
 детских домов и интернатов и детей, оставшихся без попечения родителей". Благотворительный фонд поддержки социально 
 незащищенных лиц "Жизнь как чудо". Межрегиональный Благотворительный Общественный Фонд Содействия развитию человека, 
 общества, культуры "СОФИЯ". Межрегиональная общественная организация программе воспитания подрастающего поколения 
 "Старшие Братья Старшие Сестры". Благотворительный фонд помощи пожилым людям и инвалидам "Старость в радость". 
 Региональная благотворительная общественная организация "Центр лечебной педагогики". Благотворительный фонд помощи 
 детям-сиротам, инвалидам, и людям в трудной жизненной ситуации "Река детства". Благотворительный фонд "Фонд поддержки 
 слепоглухих "Со-единение". Благотворительный фонд "Сохраняя жизнь", г. Оренбург. Приморская общественная 
 благотворительная организация помощи подросткам и молодежи "Ты не один", г. Уссурийск. Благотворительный фонд 
 одействия семейному устройству "Найди семью", г. Москва. Автономная некоммерческая организация "Центр развития 
 филантропии "Сопричастность", г. Москва. Благотворительный фонд помощи людям с боковым амиотрофическим склерозом и 
 другими нейромышечными заболеваниями "Живи сейчас", г. Москва. Благотворительный фонд имени Марины Силковой, г. Москва.
  Благотворительный фонд помощи больным несовершенным остеогенезом и другой костной патологией "Хрупкие люди", г. 
  Москва. Санкт-Петербургская благотворительная общественная организация "Перспективы". Благотворительный фонд 
  содействия образованию, культурному развитию и социальной поддержке населения "Планета добра", г. Москва. Региональная
   общественная организация инвалидов "Перспектива", г. Москва. Фонд поддержки лиц с нарушением развития и интеллекта 
   "Лучшие друзья", г. Москва. Фонд "Нижегородский онкологический научный центр", г. Нижний Новгород. Белгородская 
   региональная общественная организация "Святое Белогорье против детского рака", г. Белгород. Благотворительный 
   детский фонд "Мы вместе", г. Екатеринбург. Благотворительный фонд "География добра", г. Кострома. Алтайская 
   региональная общественная организация "Мать и дитя", г. Барнаул. Благотворительный фонд помощи детям "Доброе сердце",
г. Курчатов. Санкт-Петербургский Благотворительный фонд помощи детям с онкозаболеваниями "СВЕТ". Автономная 
некоммерческая организация помощи детям, оказавшимся в тяжёлых жизненных обстоятельствах "Больничные Клоуны", г. 
Москва. Оренбургская областная общественная организация родителей детей больных онкологическими заболеваниями "Оренонк".
Некомерческая организация Благотворительный фонд "Защита детей от насилия", г. Москва. Автономная некоммерческая 
организация "Лаборатория социальной рекламы", г. Москва. Благотворительный фонд "НАШИ ДЕТИ 56", г. Оренбург. 
Благотворительный фонд "Тёплый дом", г. Санкт-Петербург. Благотворительный фонд помощи пенсионерам и инвалидам 
"Наше дело", Ставропольский край, г. Михайловск. Некоммерческая организация социо-культурное частное учреждение 
"Доркас Эйд Интернешнл СНГ", г. Москва. Воронежская региональная благотворительная общественная организация 
"РАССВЕТ". Благотворительный фонд помощи гражданам с заболеваниями органа зрения и защиты их прав в сфере лечения и 
профилактики слепоты "Право на зрение", Московская обл., г. Реутов. Региональный Благотворительный Фонд помощи детям 
"Лучик света", г. Нижневартовск. Благотворительный фонд помощи тяжелобольным детям "Потерь нет", г. 
Уфа. Благотворительный фонд "Дорога вместе", г. Москва. Благотворительный фонд "Красивые дети в красивом мире". 
Благотворительный фонд "Добрый город Петербург". Ульяновский региональный благотворительный общественный фонд "Дари 
добро". Некоммерческая организация Фонд поддержки местного сообщества "Территория успеха". 
Межрегиональный благотворительный общественный фонд "Право матери", г. Москва. Благотворительный фонд содействия 
образованию детей-сирот "Большая Перемена". Автономная некоммерческая благотворительная организация Синяя птица, г. 
Краснодар. Благотворительный фонд помощи детям-сиротам и детям-отказникам "Бюро Добрых Дел". Всемирный фонд дикой 
природы (WWF Росcии). Благотворительный фонд помощи бездомным животным "РЭЙ". Межрегиональная благотворительная 
общественная организация – Российский Комитет "Детские деревни – SOS", г. Москва. Культурно-просветительский РУССКИЙ 
ФОНД. Волонтерский проект по росписи больниц "Веселый коридор". Некоммерческая организация Благотворительный фонд 
социальной поддержки и помощи населению "Неопалимая Купина", г. Москва. Благотворительный фонд помощи больным детям и 
пожилым людям "Река Добра", Белгородская обл.. Благотворительный фонд Служба социального обслуживания "Дом старчества"
, Свердловская обл.. Региональный общественный фонд помощи в поиске пропавших детей "Поиск пропавших детей", г.
Москва. Свердловская региональная общественная организация по содействию семьям с детьми в трудной жизненной ситуации 
"Аистенок", г. Екатеринбург. Фонд "Национальный фонд развития реабилитации", г. Москва. Благотворительный фонд 
"Святителя Николая Чудотворца по оказанию помощи нуждающимся", г. Ростов-на-Дону. Автономная некоммерческая 
организация поддержки интересов семьи и детства "ПроДетство", г. Рязань. Благотворительный фонд "АК БАРС СОЗИДАНИЕ", 
г. Казань. Благотворительный фонд развития паллиативной помощи "Детский паллиатив", г. Москва. Благотворительный фонд 
помощи детям с тяжелыми заболеваниями и их семьям "КОРАБЛИК", г. Москва. Астраханская региональная благотворительная 
общественная организация "Я с Тобой!". Благотворительный фонд социальной поддержки защиты прав ребенка на жизнь и 
воспитание в семье "Колыбель надежды", г. Пермь. Краснодарская краевая общественная организация помощи детям инвалидам 
"Всем сердцем". Благотворительный Фонд помощи осужденным и их семьям, г. Москва. Санкт-Петербургская благотворительная 
общественная организация помощи детям, находящимся в трудной жизненной ситуации, "Мята". Фонд "Центр содействия 
еврейской жизни молодежи "Гилель", г. Москва. Автономная некоммерческая организация "Центр детства и семьи "Мечта", 
Брянская обл.. Благотворительный фонд "Наследие Тамбовщины", г. Тамбов. Региональная общественная организация 
родителей детей-инвалидов "Дорогою добра", Кировская обл.. Московский областной благотворитеольный фонд реабилитации 
детей-инвалидов, поддержки и развития детско-юношеских лыжных гонок "От детской мечты к вершинам Олимпа". 
Некоммерческое партнерство тренеров и консультантов "Девелопмент — групп", г. Москва. Автономная некоммерческая 
организация "Центр социальной помощи и адаптации для людей с диагнозом ДЦП и другими ограниченными возможностями 
здоровья "Лыжи мечты" Сергея Белоголовцева", г. Москва. Межрегиональная благотворительная общественная организация 
"Центр развития некоммерческих организаций", г. Санкт-Петербург. Благотворительный центр детского больничного и 
социального волонтерства "Верю в чудо", г. Калининград. Благотворительный фонд "Созвездие сердец", г. Новосибирск. 
"Добро.Мэйл.Ру", г. Москва. Благотворительный фонд добровольной помощи детям "Владмама", г. Владивосток. 
Благотворительный фонд "Добро24.ру", г. Красноярск. Иркутское региональное отделение Международной общественной 
организации инвалидов "Стеллариум". Благотворительный фонд "РОДИНА И ЧЕСТЬ", г. Белгород. Благотворительный фонд 
помощи детям, оставшимся без попечения родителей, и детям в трудной жизненной ситуации "Дети без мам", г. 
Нижний Новгород. Благотворительный фонд "Сохранение культурного наследия "Белый Ирис", г. Москва. Благотворительный 
фонд помощи детям-сиротам "Иван да Марья", г. Москва. Благотворительный Фонд содействия деятельности в сфере 
профилактики и охраны здоровья граждан, а также пропаганды здорового образа жизни "Живи, малыш", г. Нижний Тагил. 
Детский благотворительный фонд "Счастливые дети", г. Красноярск. Благотворительный Фонд в поддержку развития спорта 
инвалидов "ТОЧКА ОПОРЫ", г. Санкт-Петербург. Санкт-Петербургская благотворительная общественная организация помощи 
детям и взрослым с ограниченными возможностями "Шаг Навстречу". Ростовская городская организация инвалидов "Надежда", 
г. Ростов-на-Дону. Межрегиональная общественная организация инвалидов с несовершенным остеогенезом "Хрустальные люди", 
г. Санкт-Петербург. Благотворительный фонд поддержки и развития театра и театральной деятельности "Александринский 
Меценат", г. Санкт-Петербург. Благотворительный Фонд "Делай Добро Легко", г. Санкт-Петербург. Санкт-Петербургская 
ассоциация общественных объединений родителей детей-инвалидов "ГАООРДИ". Некоммерческий благотворительный фонд помощи 
детям "Дедморозим", г. Пермь. Частное образовательное учреждение дополнительного образования, 
психолого-педагогического сопровождения и коррекции "Странник", г. Санкт-Петербург. Благотворительный фонд 
помощи детям "Асенька", г. Москва. Нижегородская областная общественная организация "Инновационный центр в XXI век 
с 21 хромосомой "Сияние". Региональная общественная организация поддержки социальной деятельности Русской 
Православной Церкви "Милосердие". Межрегиональный общественные фонд помощи родственникам больных с инсультом 
"ОРБИ". Благотворительный фонд "Добрый мир", г. Тверь. Благотворительная общественная организация "Апельсин" 
Санкт-Петербурга. Санкт-Петербургская благотворительная общественная организация "Ночлежка". Отделение международной 
неправительственной некоммерческой организации "Совет Гринпис", г. Москва. Благотворительный фонд святителя 
Василия Великого, Московская обл.. Фонд поддержки и развития филантропии "КАФ", г. Москва. Благотворительный фонд 
"Капля добра", г. Калининград. Благотворительный фонд "Дети ждут родителей", г. Петропавловск-Камчатский. Хабаровская 
краевая общественная организация замещающих семей "Чужих детей не бывает". Благотворительный фонд "Дари еду", г. 
Москва. Благотворительный фонд "Возрождение Веры", г. Ростов-на-Дону. Национальная ассоциация организаций помощи 
животным "Мы вместе", г. Санкт-Петербург. Фонд помощи попавшим в трудные жизненные ситуации имени Яны Поплавской, 
г. Москва. Благотворительный фонд "Добро мира — волонтеры Крыма", г. Симферополь. Благотворительный фонд социальных 
рограмм "Помощь бездомным собакам", г. Санкт-Петербург. Автономная некоммерческая организация по оказанию услуг в 
области содержания животных "Помощь бездомным собакам", г. Санкт- Петербург. Некоммерческое Объединение 
Благотворительный Фонд "Друг", г. Санкт-Петербург. Автономная некоммерческая организация "Островок надежды", г. 
Санкт-Петербург. Благотворительный фонд помощи бездомным животным "Верность", г. Санкт-Петербург. Автономная 
некоммерческая организация приют для животных "Преданное сердце", г. Санкт-Петербург. РОО "Котопёс", г. Сосновый Бор, 
Ленинградская область. Автономная некоммерческая организация "Все в музей", г. Санкт-Петербург. Тематический 
парк "Добромир", г. Сочи. Межрегиональная общественная организация "Лига декоративного хорьководства "Мелиан", г. 
Санкт-Петербург. Некоммерческая организация Благотворительный фонд "Счастливый Мир", г. Москва. Благотворительный 
фонд помощи детям и малоимущим гражданам "Простые вещи", г. Москва. Благотворительный фонд "Это чудо", г. Киров. 
Благотворительный Фонд "Искорка надежды", г. Курск. Некоммерческое партнерство Зоозащитный центр "Новый Ковчег", г. 
Обнинск. Некоммерческое Учреждение "Редакция "Благотворительной газеты "РУССКИЙ ИНВАЛИД" г. Санкт-Петербург. 
Региональная общественная организация "Санкт-Петербургское объединение родителей учащихся и выпускников, учителей и 
выпускников школ по содействию развитию школьного образования и условий образовательного процесса в школах", г. 
Санкт-Петербург. Общественное движение спортивных волонтеров Санкт-Петербурга. Региональная ассоциация молодежных и 
детских общественных объединений "Санкт-Петербургский круглый стол молодежных и детских объединений". Автономная 
некоммерческая организация "Центр социально-правовой защиты населения", г. Санкт-Петербург. Фонд социальной поддержки 
населения "Мост поколений", г. Санкт-Петербург. Региональная общественная организация по содействию охране и 
обеспечению общественного порядка "Народная Дружина", г. Санкт-Петербург. Санкт-Петербургская Региональная 
общественная организация "Северо-Славянская Народная Дружина". Фонд помощи детям "Город на Неве", г. Санкт-Петербург. 
Общероссийское общественное движение "Социал-демократический союз молодежи России СПРАВЕДЛИВАЯ СИЛА", г. 
Санкт-Петербург. Автономная некоммерческая организация "Центр социальных и благотворительных проектов "ОГОНЕК ДОБРА", 
г. Санкт-Петербург. Благотворительный фонд помощи нуждающимся детям Санкт-Петербурга "Солнце". Межрегиональная 
общественная организация "Центр содействия реализации социальных инициатив «Живой Питер", г. Санкт-Петербург. 
Региональная общественная организация "Врачи Санкт-Петербурга". Региональная общественная организация автомобилистов 
"СПБ.АВТО", г. Санкт-Петербург. Региональная общественная организация "Центр содействия социально-культурному, 
творческому и спортивно-оздоровительному развитию "Нестор", г. Санкт-Петербург. Региональная общественная организация 
"Центр защиты и развития личности", г. Санкт-Петербург. Санкт-Петербургская региональная общественная организация 
по поиску пропавших, защите и спасению людей в условиях чрезвычайных ситуаций "Питер – Поиск". Общественное движение
 »Энергия Жизни», г. Санкт-Петербург. Благотворительный фонд "Алёша", г. Санкт-Петербург. Автономная некоммерческая
организация культурных, социальных, спортивных программ и проектов "Невские берега", г. Санкт-Петербург. Курская 
региональная общественная организация "Культурно-просветительское общество "Возрождение". Межрегиональная общественная 
организация инвалидов "Родничок надежды", г. Санкт-Петербург. Некоммерческий детский благотворительный фонд имени 
Алёны Петровой, г. Томск. Тверской Благотворительный фонд помощи онкобольным им. Виктории Рудневой. Благотворительный 
фонд помощи детям с онкогематологическими заболеваниями "ДАРИНА",. Ростов-на-Дону. Некоммерческий Благотворительный 
Фонд "Наши дети", г. Уфа. Благотворительный фонд помощи детям с онкогематологическими и иными тяжелыми заболеваниями 
"ДоброСвет", г. Воронеж. Самарская областная общественная организация помощи детям, страдающим онкогематологическими 
заболеваниями "Виктория". Благотворительный фонд помощи детям и их семьям "Спасибо за жизнь", г. Саратов. 
Благотворительный фонд поддержки детей с особенностями развития "Я есть!", г. Москва. Благотворительный фонд 
помощи детям с онкогематологическими и иными тяжелыми заболеваниями "Ванечка", г. Брянск. Благотворительный фонд 
помощи детям с онкогематологическими и иными тяжелыми заболеваниями "Пчелка Майя", г. Чита. Некоммерческая организация 
Благотворительный фонд "Берегиня", г. Пермь. Фонд поддержки и укрепления современной культуры, г. Москва. 
Благотворительный фонд "СЛАВИК", г. Курган. Ростовская региональная общественная организация семей воспитывающих 
детей-инвалидов и детей-сирот "Ветер перемен". Благотворительный фонд "Защити жизнь" г. Новосибирск. Благотворительный 
фонд "ТЕШАМ", г. Назрань, Ингушетия. Благотворительный Фонд "Чужих детей не бывает!", г. Великий Новгород. 
Благотворительный Фонд Профсоюзный, Алтайский край, г. Барнаул. Благотворительный фонд "Нужна помощь", г. Москва. 
Санкт-Петербургское региональное общественное движение помощи детям, оставшимся без попечения родителей "Петербургские 
Родители". Северо-Западный благотворительный фонд помощи детям, оставшимся без попечения родителей "Дети ждут", г. 
Санкт-Петербург. Благотворительный фонд помощи детям "ДОБРЫЙ ЖУРАВЛИК" г. Брянск. Некоммерческая организация 
"Благотворительный фонд "Личное участие", г. Самара. Ивановская областная общественная организация инвалидов "Аврора". 
Благотворительный фонд поддержки и развития любительского спорта для людей с ограниченными возможностями "Спорт 
для жизни", г. Москва. Благотворительный фонд "Подари надежду", г. Москва. Благотворительный образовательный фонд 
"Мархамат", г. Уфа\', \'21 декабря с:00:00«Музее Москвы» (Зубовский бульвар, дом 2) пройдет благотворительный праздник 
«Снежный день». Этой ярмаркойхотим напомнить,Новый год – это время не только верить в чудеса, но и творить их.
большом зале на третьем этаже музея разместятся представительства 20 благотворительных организаций, среди которых: 
благотворительный фонд социальной поддержки и защиты населения«Созидание»,помощи взрослым «Живой», фонд помощи 
хосписам «Вера» и фонд помощи детям«Подсолнух». Здесь развернется основная часть ярмарочной программы. На ярмарке 
можно будет купить новогодние сувениры, игрушки и подарки, изготовленные вручную волонтерами и подопечными 
представленных орагнизаций. Это возможность запастись милыми новогодними подарками, сделанными с душой, и при этом 
поучаствовать в большом добром деле. Главный спонсор ярмарки – компания Panasonic –обеспечит зал звуковы
благотворительный проект«Вешалка»«Лавка радостей», куда люди приносят ненужные вещи в хорошем состоянии. 
осетители могут получитьобмен на пожертвования. Все собранные средства идут на благотворительность. 
 этот день в «Музее Москвы» в благотворительных магазинах можно будет приобрести также новую одежду и
 звестных брендов и вещи, пожертвованные знаменитостями. Рядом — старые детские книги, виниловые пластинки 
 и для ценителей — CD-диски, предоставленные рекорд-компанией SOYUZ MUSIC.соседству разместится просторная 
 детская зона, где весь день с юными гостями ярмарки будут работать аниматоры. Для родителей, которые хотят провести 
 время вместе с детьми, да еще и с пользой, пройдут мастер-классы по декупажу и изготовлению игрушек.стилистов’studioк 
 участию в проекте своих выпускников. Молодые стилисты и визажисты сделаюти макияж всем желающим. Тут же специалисты 
 покомпании«АртАква»на лицах детей красивые новогодние узоры или мордочки сказочных персонажей. Поэкспериментировать 
 с образом также можно будет с помощью «мехенди» — росписи тела узорами из хны.На память об этом событии в специальной 
 зоне для васпрофессиональную фотографию. Всё это – за символическое пожертвование.течение всего дня на ярмарке будет 
 работать фудкорт, где можно выпить хорошего кофе или чая и перекусить., великодушный «Теремок» порадует гостей 
 горячими блинами за благотворительное пожертвоание. Еще на улице обязательно загляните в вагончик TWIX, где будут 
 бесплатно раздавать мороженое всем желающим.собранные средства на мероприятии будут направлены на благотворительные 
 проекты.мастер-классов:<!--td {border: 1px solid #ccc;}br {mso-data-placement:same-cell;}-->столстолстолстолстол.
 00-13.00как чудо: Роспись деревянных овечек"В твоих руках": изготовление брошек и ёлочных игрушек из вощинына улице: 
 мехенди — роспись хной.00-13.00.00-14.00: Роспись пряников глазурью.00-14.00.00-15.00"Жизнь": роспись пряников 
 глазурью: елочная игрушка — коньки из фетра"Помоги.орг": роспись сумок.00-15.00.00-16.00милосердия: новогодняя 
 икебана.00-16.00.00-17.00Журавлева — новогодние коты: мастер-класс на мольбертах.00-17.00.00-18.00браслетов из кожи 
 и деревянных бусин:-)"В твоих руках": декупаж елочных шаров.00-18.00.00-19.00"Живой": изготовление новогодних шаров.
 00-19.00.00-20.00.00-20.00.00-21.00.00-21.00\', \'Если вам не безразлична судьба благотворительных организаций, 
 присоединяйтесь к нашему обращению в Государственную Думу. Поставьте свою подпись под петицией."Ассоциация 
 циально-ориентированных некоммерческих организаций «Благотворительное собрание «Все вместе»», объединяющая 43 
 благотворительные организации, выражает обеспокоенность внесёнными в Государственную Думу поправками к закону 
 «О некоммерческих организациях», уточняющими понятие «политической деятельности». Фактически поправки являются 
 дополнением к законодательству, регулирующему внесение некоммерческих организаций в реестр «организаций, выполняющих 
 функции иностранных агентов».сожалению, качество уже существующих правовых норм, касающихся «иностранных агентов», 
 таковы, что соблюсти их невозможно по техническим причинам, и в своё время общественные организации пытались обратить 
 на это внимание законодателей и общества. Если же предложенные поправки о содержании «политической деятельности» 
 будут приняты, иностранным агентом станет любая некоммерческая организация в России, чем бы она ни занималась.ранее 
 признаки "получения имущества из иностранных источников" сами по себе чрезвычайно широки. В действующем законе не 
 указан (ни в абсолютных, ни в относительных цифрах) размер необходимого для включения в реестр иностранного 
 финансирования. Также необязательным является целевой характер поступлений. Более того, к финансированию из 
 ностранных источников относится не только прямое получение средств из-за рубежа, но и поступление денег и 
 иного имущества от иностранных граждан, а также от российских юридических лиц, получавших иностранное финансирование, 
 а также любых иностранных граждан. В результате даже минимальное пожертвование от случайного гражданина Казахстана 
 или Беларуси, или же от компании, которая занимается любой международной экономической деятельностью, может считаться 
 признаком финансирования из-за рубежа. В таких условиях получение иностранного финансирования для НКО, получающей 
 средства или имущество от кого-либо, кроме государства, становится почти неизбежным, и к тому же неконтролируемым: 
 проверить гражданство жертвователя, который просто переводит деньги на счёт организации, в принципе невозможно, как и 
 источники доходов жертвователей-юридических лиц.образом этот подход вынуждает включать в реестр иностранных агентов 
 обычные НКО, которые просто существуют и намерены существовать на добровольные пожертвования граждан и организаций. 
 В то же время фальшивые НКО, которые созданы определенными лицами или структурами для достижения конкретных 
 политических целей (и, соответственно, имеют один или несколько основной источник финансирования) как раз могут 
 избежать включения в реестр, если их настоящий владелец или создатель достаточно тщательно замаскирует перечисление 
 им своих средств. То есть, закон в этом вопросе не достигает поставленной цели.признания некоммерческой 
 организации выполняющей функции иностранного агента необходимо также, чтобы её деятельность была признана 
 политической. Но внесённые в Государственную Думу поправки расширяют это понятие до полного совпадения с 
 понятием «общественная деятельность», которой, собственно, и занимаются общественные организации – по определению. 
 Поправки не конкретизируют и уточняют, а бесконечно размывают определение "политической деятельности". Если они будут 
 приняты, то к ней будут относиться любые действия, направленные на "выработку и реализацию государственной политики, 
 на формирование государственных органов, органов местного самоуправления, на их решения и действия". В этом свете 
 любая попытка некоммерческой организации взаимодействовать с любыми государственными органами окажется политической –
  потому что такого рода взаимодействие в принципе имеет своей целью влияние на принимаемые государственными органами 
  решения и на их действия. Если некоммерческая организация стремится расширить зону "доступной среды" для инвалидов в
   городе или хотя бы в районе – она, несомненно, влияет на решения органов местного самоуправления. Если НКО добивается изменения списка льготных лекарств, расширения поддержки доноров крови, смягчения условий ввоза в Россию импортных лекарственных препаратов, реформирования учреждений для детей, оставшихся без попечения родителей, вообще любых изменений форм и направлений социальной поддержи населения, то опять же, всё это подпадает под новое определение "политической деятельности".же, что в законопроекте также перечислены практически все возможные формы публичной деятельности НКО, включая организацию исследований и опросов, получается, что даже попытка просто точно выяснить и сравнить, например, содержание списков льготных лекарственных препаратов в департаментах здравоохранения различных субъектов Федерации, уже будет достаточным основанием для того, чтобы благотворительный фонд превратился в политическую организацию. Совместная работа НКО и государственных органов, улучшение качества работы последних станет невозможным. В то время как очевидно, что принципиальный разрыв между НКО и государственной властью чреват серьёзным ухудшением социальной обстановки в стране, а также противоречит приоритетам, обозначенным в речи Президента Владимира Путина на пленарном заседании Общероссийского форума "Государство и гражданское общество: сотрудничество во имя развития", где Президент ясно указал, что необходимо как можно плотнее налаживать взаимодействие между государственными органами и социально ориентированными НКО (вплоть до передачи НКО части функций государственной социальной защиты в регионах), а также оградить социально ориентированные НКО от подозрений в политической деятельности.то время как внесённые поправки наоборот – придают политическую окраску любой публичной деятельности НКО.отметить, что в последнее время многие органы государственной власти по своей инициативе привлекают авторитетные НКО к совместной работе, в том числе к принятию решений, разработке нормативно-правовых актов, контролю за своей деятельностью. Более того, подобные механизмы прямо предусмотрены действующим законодательством, в частности Федеральным законом «Об общественном контроле». Следуя буквальной логике предлагаемых поправок, НКО будут вынуждены отказываться от подобных предложений, если получили какое-либо иностранное финансирование, или даже просто финансирование, чьи источники они не в состоянии проверить, чтобы не быть признанными иностранными агентами. Вряд ли это соответствует интересам общества и государства.с чрезвычайно широким описанием "иностранного финансирования" в законе новые поправки делают получение статуса "организации, выполняющей функции иностранного агента" практически неизбежным для всех членов Ассоциации «Все вместе». Это приведёт к существенному падению качества и объёма оказываемой нами помощи. Повышенные требования к учёту и отчётности отвлекут значительные ресурсы от и без того скудных бюджетов организаций, а указание пугающего статуса "организация, выполняющая функции иностранного агента" оттолкнёт жертвователей, и сильно отбросит Россию назад в мировых рейтингах благотворительности. Сейчас мы на 126-м месте.также не обратить внимание на то, что действующий закон требует от организаций самостоятельно заявлять о своём статусе иностранного агента. Слишком широкие и неопределённые описания «политической деятельности» и «иностранного финансирования» будут вынуждать НКО самостоятельно включаться в реестр при малейших подозрениях, что их деятельность может быть признана «деятельностью иностранного агента», из опасения подвергнуться предусмотренным законом наказаниям. Либо наоборот, избыточно осторожно относиться к своей деятельности и предупредительно отсекать возможные «подозрительные» источники финансирования или отказываться от «подозрительных» проектов из тех же опасений. Более логичным и вполне достаточным было бы предоставить регулирующему органу (Минюсту) уведомлять НКО о наличии в их деятельности признаков иностранного агента, предоставляя организациям уже после получения такого уведомления согласиться с этим, возражать либо скорректировать свою деятельность и источники финансирования, а до получения уведомления чувствовать себя более свободно.благотворительных фондов, составляющих Ассоциацию «Все вместе» совпадает с целями государственной политики Российской Федерации. Мы стремимся, чтобы российские больные получали своевременное качественное лечение, а те, кого нельзя вылечить – чтобы были обеспечены должным уходом. Чтобы дети, лишённые попечения родителей, были устроены в семьи либо получили полноценный опыт социализации силами волонтёров, чтобы получали помощь старики, не оставались без защиты жертвы чрезвычайных ситуаций и бездомные. В сферу нашего внимания входят даже лишенные заботы домашние животные. Ежедневно наши организации, напрягая все силы, без помощи государства снижают социальную напряжённость в стране, помогая гражданам там, где государственных ресурсов и возможностей не хватает.если поправки будут приняты в том виде, в каком они внесены, наша деятельность окажется затруднена, а во многих случаях и вовсе невозможна. Не будет выполнена и формальная цель закона – при таких размытых критериях маркировать агентов иностранного политического влияния станет не проще, а сложнее. Поэтому мы призываем, в целях улучшения социальной ситуации в стране, не принимать данные поправки, а вернуться к диалогу между государственной властью и социально ориентированными некоммерческими организациями.целесообразным с одной стороны сузить определение «политической деятельности», с другой стороны установить абсолютный или относительный порог иностранного финансирования для приобретения статуса агента, а с третьей – исключить обязанность организаций подавать заявку на включение в реестр по собственной инициативе и ответственность организаций за непредоставление сведений о себе, как об иностранных агентах, до получения уведомления регулирующего органа. Со своей стороны, при новом обсуждении поправок в закон готовы предложить конкретные формулировки".директор«Все вместе» Н.ВБФ «Здесь и сейчас»,Совета Ассоциации «Все вместе» Т.В.Фонда Владимира СмирноваСовета Ассоциации «Все вместе» Е.Б.БФ «Детские сердца»,Совета Ассоциации «Все вместе» Е.М.БФ «Предание»,Совета Ассоциации «Все вместе» Берхин В.Б.Фонда «Подсолнух»,Совета Ассоциации «Все вместе» Кожерева В.В.проектов МОО "Дорога в мир",Совета «Ассоциации «Все вместе» Долотова И.БФ «Дети наши»,Совета «Ассоциации «Все вместе» Пензова В.С.Фонда «Нужна помощь»,Совета «Ассоциации «Все вместе» Семёнова А.А.АНО «РОСТ»,Совета «Ассоциации «Все вместе» М.В.БФ "Тепло сердец" Ирикина М.А.директор БФ "AdVita." Грачева Е.БФ "Гольфстрим" Зубова М.А.БФ "Старость в радость" Олескина Е.А.директор БФ "Во имя жизни" Гапонова Н.Д.директор"Старшие Братья Старшие Сестры" А.Ю.директор БИФ «Помоги.Орг» Нежельская С.С.Благотворительного фондахосписам «Вера», член СоветаПравительстве РФ по вопросамв социальной сфере А.К.проектов РООИ "Ковчег" Саяпина Ю.В.БФ "Живой" В.И.Фонда «БО «Адреса милосердия» Пинскер О. А.МОО "Дорога в мир" Леонова Е.И.БФ "Река детства" Поздеева О.П.Фонда "Не просто собаки" Дубинина О.М.АНО «РОСТ» А.С.БФ "Жизнь" К.Г.БФ "Измени одну жизнь" Юдина Ю.В.проектов БФ "В твоих руках" Коновалова Е.В.Центра равных возможностейдетей-сирот "Вверх" Тихомирова О.В.директор«Художественный центр «Дети Марии» Елисеева М.Л.ФондХабенского А.В.БФ «Галчонок» Вайе РейторБФ «Детская больница» Казбеков М.И."Центр лечебной педагогики" Битова А.Л.БФ «Настенька» Д.М.подпись\''''


inputs = tokenizer(article[:5000], src_lang="en_XX", padding="max_length",
                   truncation=True, max_length=600, return_tensors="pt")

# In[ ]:


# In[10]:


translated_tokens = model.generate(**inputs, decoder_start_token_id=tokenizer.lang_code_to_id["ro_RO"])
summary = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]

# In[11]:


summary

# In[15]:


for i in range(len(article) // 5000 + 1):
    print(i * 5000 + 5000)

# In[16]:


# for i in range(len(article) // 5000 + 1):
#     inputs = tokenizer(article[i * 5000: i * 5000 + 5000], src_lang="en_XX", padding="max_length", 
#                    truncation=True, max_length=600, return_tensors="pt")
#     translated_tokens = model.generate(**inputs, decoder_start_token_id=tokenizer.lang_code_to_id["ro_RO"])
#     summary = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
#     print(summary)


# In[17]:


print('Hello world')

# In[ ]:
