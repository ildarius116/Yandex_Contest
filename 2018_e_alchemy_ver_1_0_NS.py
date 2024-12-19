"""
E. Занимательная алхимия

	Все языки	C++20 (GCC 14.1)	C++20 (Clang 18.1.6)
Ограничение времени	5 секунд	2 секунды	2 секунды
Ограничение памяти	511Mb	512Mb	512Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

На рынке зелий произошёл бум и практически в каждом доме появилась своя алхимическая лаборатория. Ресурсы подобных индивидуальных предпринимателей невелики, и их инструментарий сильно ограничен. В результате долгих экспериментов были открыты два универсальных ингредиента для зелий (назовем их A и B), которые оказались доступны любому начинающему алхимику.
Отныне рецепт любого зелья можно свести к этим двум компонентам - зелье состоит из чистых ингредиентов A и/или B, из других зелий или из смеси чистых ингредиентов и зелий.
Одно зелье может требовать несколько экземпляров одного и того же ингредиента / зелья.
Ваш близкий друг Тирания Вампадур только начинает свой путь в алхимии и каждый день задаёт вам Q вопросов вида: если в её подвале осталось X единиц ингредиента A и Y единиц ингредиента B, может ли она изготовить один пузырёк зелья номер S?
Для облегчения своей жизни, вы решаете написать программу, отвечающую на подобные вопросы и подарить её Тирании.
Важно отметить, что некоторые рецепты были записаны со слов почётных алхимиков города, чья память знавала и лучшие времена. Поэтому рецепты для некоторых зелий могут быть записаны неправильно и содержать циклы — такие зелья изготовить никак нельзя.
Формат ввода
В первой строке дано число N (3≤N≤200000) — общее количество ингредиентов и рецептов производных зелий. Ингредиент A имеет номер 1, B — номер 2, все производные зелья пронумерованы от 3 до N.
Следующие N−2 строк содержат информацию о создании зелий: в i-й строке содержится список составных частей для зелья i+2.
Первое число в строке Ki — количество составных частей. Далее через пробел следуют Ki чисел Pij (1≤Pij≤N, 1≤j≤Ki) — номера составных частей для изготовления зелья i+2.
Составные части в строке могут повторяться — каждая часть учитывается столько раз, сколько указана.
Гарантируется, что ∑Ki≤1000000.
В следующей строке задано одно целое число Q (1≤Q≤200000) — количество вопросов Тирании.
Каждый вопрос задаётся в отдельной строке в формате XYS (0≤X,Y≤109, 3≤S≤N) — количество ингредиентов A и B в подвале соответственно, а также номер запрашиваемого для изготовления зелья.
Формат вывода
В единственной строке выведите строку из Q символов:
•	1, если можно изготовить зелье из имеющегося количества ингредиентов;
•	0 в любом ином случае.

Пример
Ввод
7
3 1 1 2
2 1 3
3 4 3 4
1 7
1 6
3
8 4 5
9 2 5
10 10 6
Вывод
100

Примечания
В приведенном тестовом примере есть 5 зелий и 2 чистых ингредиента:
•	Зелье 3 требует для создания два ингредиента A и один ингредиент B;
•	Зелье 4 требует один ингредиент A и одно зелье 3 — значит суммарно три ингредиента A и один ингредиент B;
•	Зелье 5 требует два зелья 4 и одно зелье 3 — суммарно восемь ингредиентов A и три ингредиента B;
•	Зелья 6 и 7 ссылаются друг на друга в рецептах — судя по всему, что-то перепуталось при записи и в данный момент изготовить их никак нельзя.
В первом вопросе Тиранию интересует, можно ли изготовить зелье 5, имея ровно 8 ингредиентов A и 4 ингредиента B. Как мы выяснили выше, для изготовления зелья 5 требуется как раз 8 ингредиентов A и 3 ингредиента B — значит зелье изготовить можно.
Второй вопрос Тирания задаёт также про зелье 5, но теперь ингредиентов A — целых 9, в то время как ингредиентов B всего 2. Хотя ингредиентов A хватает с избытком, но ингредиентов B не хватает (нужно 3), поэтому изготовить зелье нельзя.
В третий раз Тирания спрашивает вас о зелье 6 — вы уже знаете, что независимо от количества ингредиентов это зелье изготовить не получится никак из-за циклической зависимости в рецептуре.
"""
