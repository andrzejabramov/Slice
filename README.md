Описание алгоритма:
Решение выстроено с помощью класса Slice, где каждому заданию назначен свой метод. Вызываются методы с помощью
функции с конструкцией match_case (релиз python 3.10)
Особо необходимо пояснение в дополнительном методе reverce_half:
Дело в том, что я неверно понял задание и почему-то мне показалось, что вторая половина строки должна быть выведена в консоль
в обратном направлении и нечетное количество символов должно обязательно быть не менее невыводимого остатка. Вообщем, придумал
себе лишнюю проблему и, как потом оказалось, что существует 4 варианта определения stop в slice в зависимости от того, четное или нечетное количество вводимых символов и в том и другом случае может половина символов без остатка быть четной или нечетной.
Для каждого из вариантов своя формула вычисления stop. И отдельно пришлось выделить в исключение вариант, когда введены 3 символа, потому, что при этом нечетная половина либо 1 символ, либо все 3 (то есть полная строка). Поэтому для 3 символов сделано исключение и настроен вывод нечетного количества в виде только одного символа.
ввод одного символа валидацией запрещен, так как не имеет смысла.
