	1) Сортировать значения объема одной акции за один месяц по возрастанию;
	2) Отсечь 25% самых мелких и 25% самых крупных;
	3) Найти среднее значение оставшихся величин;
	4) Поочередно найти разницу (отклонение) между значением каждого объема и средним значением объема (шаг 3);
	5) Каждое значение найденной разницы (отклонения) возводим в квадрат, затем суммируем между собой, делим на количество исходных значений объемов (после отсечения 25%) и возводим в квадратный корень. Получаем среднеквадратическое отклонение (σ).
Пояснение: Полученное значение отображает величину, в пределах которой могут распределиться величины. ~68% наблюдений находятся в рамках этого среднеквадратического отклонения. То есть мы от среднего отнимаем (или прибавляем) данное отклонение и смотрим, находится ли исследуемое значение в рамках этого отклонения
Дополним в анализ Z-преобразование для приведения вычислений в единую формулу сравнительного анализа

**Z_i=(X_i-X_cp)/σ**
	
 *Где Xi – значение объема, которое мы получили в реальном времени
Xср = среднее значение (3 шаг)
σ – среднеквадратическое отклонение (5 шаг)*

 
При подсчете Z-преобразования мы будем получать проценты (то есть величину, показывающую, в скольких стандратных отклонениях от среднего значения находится изучаемое значение объема). Например, в пределах двух σ находится ~95 всех значений. И если искомое значение выходит в предел этих 95.44% (двух σ), то оно считается нормальным. Если же выходит за рамки – то аномальным. (то есXть если Z > 0.9544, то аномальный объем)
P.s = если аномальные объемы будут маркаться слишком часто, то можно передвинуть предел аномальности. Сделать например между 2 σ и 3 σ (0.9758)
