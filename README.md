#Updat euler_2

## Алгоритм:
1. Принимаем порядок уравнения и характеристические корни
2. Затем по хар.корням строим характеристическое уравнение.
3. Выделяем коэффициенты при характеристических корнях
(эти коэффициенты будут использованы для расчета нужных нам коэффициентов alpha_i)
4. В зависимости от порядка уравнения - n, создаем массив длинной n , в котором в 
каждой i ячейке лежит i раскрытие y^n т.е 
y' = D
y'' = D(D - 1)
y''' = D(D - 1)(D - 2)
y'''' = D(D - 1)(D - 2)( D - 3)
y''''' =  D(D - 1)(D - 2)( D - 3)( D - N_max - 1)
....................... и так далее
5. Так как нам известна замена, она неизменна в любом случае, тогда зная порядок ур-ия
мы можем посмотреть на "дефолтные" коэффициенты при D^i порядка и сравнив их определенным
образом с коэффициентами характеристического уравнения , найти нужные нам коэффициенты (alpha)
6. Строим  следующий цикл:
(Основной принцип alpha_1 = 1 -> default, alpha_2 = lambda_2 - СУММА ВСЕХ ЗНАЧЕНИЙ ПРИ КОЭФФИЦИЕНТАХ D ИЗ МАССИВА ПУНКТА 5 * АЛЬФЫ ПРИ ЭТИХ РАСКРЫТИЯХ
![image](https://user-images.githubusercontent.com/61281668/135714894-63021fa2-ff56-4b02-8c8f-97823a76a45d.png)
![image](https://user-images.githubusercontent.com/61281668/135715032-2884ee02-2017-47e1-adab-c62e19cef4be.png)

7. В массиве alphas будем содержать все нужные нам значения
#end




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

## 4х4 NxN:
https://www.sympy.org/en/index.html

Основные источники, которые помогли при написании:
https://scask.ru/f_book_vdif.php?id=37
http://mathhelpplanet.com/static.php?p=ldu-s-peremennymi-koeffitsientami
https://publikacija.ru/images/PDF/2018/28/vosstanovlenie-linejnogo.pdf
https://matica.org.ua/metodichki-i-knigi-po-matematike/lineinaia-algebra-uchebnoe-posobie-z-i-andreeva/06-opredeliteli-n-go-poriadka
http://twt.mpei.ac.ru/math/content.html

## Result:
![image](https://user-images.githubusercontent.com/61281668/134803798-6f2b3159-4c60-4244-a540-460dd9727972.png)
