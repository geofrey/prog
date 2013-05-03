((lambda (f x)
   (f f x))
 (lambda (f x)
   (if (< x 1)
       1
       (* x (f f (- x 1)))))
 5)

(define Y (lambda (f x) (f f x)))

(define fact_sr
  (lambda (f x)
   (if (< x 1)
       1
       (* x (f f (- x 1))))))

(Y fact_sr 5)

(define fib_sr
  (lambda (f n)
    (if (< n 2)
        1
        (+ (f f (- n 2)) (f f (- n 1))))))

(define theList '(1 2 3 4 5 6 7 8 9 10))
(Y fib_sr 10)
(map (lambda (n) (Y fib_sr n)) theList)

(define Y2 (lambda (f) (lambda (x) (f f x))))

(map (Y2 fib_sr) theList)

;summation
(Y (lambda (f n) (if (> n 1) (+ n (f f (- n 1))) 1)) 5)
((Y2 (lambda (f n) (if (> n 1) (+ n (f f (- n 1))) 1))) 5)

(define sum (lambda (addables) (if (null? addables) 0 (+ (car addables) (sum (cdr addables))))))
(sum '(1 2 3 4 5))
(define sign (lambda (arg) (if (eq? arg 0) 0 (/ (abs arg) arg))))
(sign 5)
(sign -5)
(sign 0)
(define range (lambda (min max step) (if (> (* (sign step) (- max min)) 0) (cons min (range (+ min step) max step)) '())))
(range 1 (+ 10 1) 1)
(sum (range 1 11 1))
(sum (map (Y2 fib_sr) (range 1 11 1)))
(define reduce (lambda (op list) (if (null? (cdr list)) (car list) (op (car list) (reduce op (cdr list))))))
(reduce + (range 1 11 1))
(reduce + (map (Y2 fib_sr) (range 1 11 1)))
