
# Нахождение исходного вида ур-ия Эйлера, по корням хар. ур-ия :

Данное задание дано мне преподавателем по дифференциальным уравнениям:

## Задание: по заданным характеристическим корням, найти коэффициенты a_i уравнения Эйлера. 
Я хотел найти более простой способ, но все же пришлось использовать фундаментальную систему решений,
 при помощи которой удалось восстановить исходное уравнение Эйлера


Количество вкладок для написания rofl
![image](https://user-images.githubusercontent.com/61281668/134803556-41405f88-9cbe-45db-b751-d432fac28b54.png)

Анализ : Так как мне вообще то и не важна однородность/неоднородность исходного уравнения( так как коэффициенты,
находятся в левой части), мне нужно было проанализировать только левую часть уравнения, которая всегда будет сводиться
к линейному уравнению с постоянными коэффициентами, по которому мы и получаем характеристическое уравнение. Да и вообще
исследовать замены по типу х = e^t  не имеет большого смысла, т.к мы в любом случае будем исследовать однородное уравнение.
Поэтому мною рассматривается замена вида: y = x^k. Весь анализ основывался только на виде уравнения и данных, которые мне
предоставленны - корни хар. ур-ия . Поэтому первое что пришло в голову - построение ФСР -> определитель Вронского -> 
-> получение левой части уравнения, ну и соответственно решение поставленной задачи - нахождение коэффициентов a_i

В процессе решения нужно было находить определители разных порядков, в зависимости от порядка уравнения, соответственно менялся
принцип их нахождения. По своей глупости я начал писать алгоритмы нахождения для 1,2 и 3 порядка, затем посмотрел в библиотеку
sympy и понял.... что все вообще-то написано.


## 2x2:
Главная диагональ - побочная диагональ

## 3x3:
![image](https://user-images.githubusercontent.com/61281668/134804010-11a79727-b8f2-4172-b99b-7cef2d265367.png)

## 4х4:
https://www.sympy.org/en/index.html

![image](https://user-images.githubusercontent.com/61281668/134803798-6f2b3159-4c60-4244-a540-460dd9727972.png)
