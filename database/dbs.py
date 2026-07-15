import sqlite3
conn = sqlite3.connect('BASE_ASMD.db')
cursor = conn.cursor()

cursor.execute('''
	CREATE TABLE PLAYER(
		id_pl INTEGER PRIMARY KEY,
		name_pl TEXT NOT NULL,
		score_pl INTEGER NOT NULL              
	)
''')

cursor.execute('''
	CREATE TABLE PRIMERO_MEDIO(
		id_question_pr INTEGER PRIMARY KEY,
		question_pr TEXT NOT NULL,
		alternative_n1_pr TEXT NOT NULL,
		alternative_n2_pr TEXT NOT NULL,
		alternative_n3_pr TEXT NOT NULL,
		alternative_n4_pr TEXT NOT NULL,
		answer_pr TEXT NOT NULL
	)
''')

cursor.execute('''
	CREATE TABLE SEGUNDO_MEDIO(
		id_question_sg INTEGER PRIMARY KEY,
		question_sg TEXT NOT NULL,
		alternative_n1_sg TEXT NOT NULL,
		alternative_n2_sg TEXT NOT NULL,
		alternative_n3_sg TEXT NOT NULL,
		alternative_n4_sg TEXT NOT NULL,
		answer_sg TEXT NOT NULL               
	)
''')

cursor.execute('''
	CREATE TABLE TERCERO_MEDIO(
		id_question_trc INTEGER PRIMARY KEY,
		question_trc TEXT NOT NULL,
		alternative_n1_trc TEXT NOT NULL,
		alternative_n2_trc TEXT NOT NULL,
		alternative_n3_trc TEXT NOT NULL,
		alternative_n4_trc TEXT NOT NULL,							 
		answer_trc TEXT NOT NULL               
	)
''')

cursor.execute('''
	CREATE TABLE CUARTO_MEDIO(
		id_question_cr INTEGER PRIMARY KEY,
		question_cr TEXT NOT NULL,
		alternative_n1_cr TEXT NOT NULL,
		alternative_n2_cr TEXT NOT NULL,
		alternative_n3_cr TEXT NOT NULL,
		alternative_n4_cr TEXT NOT NULL,							 
		answer_cr TEXT NOT NULL               
	)
''')


PRIMERO_MEDIO=[

	(1,'¿Cuál es el resultado de 12 ÷ 3?','2','3','4','6','4'),
	(2,'¿Cuál es el valor de 3²?','3','6','9','12','9'),
	(3,'¿Cuál es el resultado de (-5) + 8?','-13','-3','3','13','3'),
	(4,'Si tienes 2/3 de pizza y comes 1/3, ¿cuánto queda?','2/3','1/3','0','3/3','1/3'),
	(5,'¿Cuál es el valor de la raíz cuadrada de 81?','9','8','3','27','9'),
	(6,'¿Cuál es el opuesto de -12?','-12','0','12','-1','12'),
	(7,'El perímetro de un cuadrado de lado 5 es:','10','20','25','15','20'),
	(8,'¿Cuál es el valor absoluto de -18?','-18','0','18','-1','18'),
	(9,'¿Cuánto es 7*6?','36','42','56','49','42'),
	(10,'Si un ángulo mide 90°, se llama:','Agudo','Obtuso','Recto','Llano','Recto'),

	(11,'¿Cuál es el resultado de 2x + 3 cuando x=4?','10','11','12','13','11'),
	(12,'Si el promedio de 5, 7 y 9 es p, ¿cuánto vale p?','6','7','8','9','7'),
	(13,'El área de un rectángulo de base 8 y altura 6 es:','14','24','28','48','48'),
	(14,'Simplifica la fracción 24/36','2/3','3/4','4/5','5/6','2/3'),
	(15,'El ángulo suplementario de 120° es:','30°','45°','60°','150°','60°'),
	(16,'Resuelve: (3x - 4) = 11','x=3','x=5','x=7','x=9','x=5'),
	(17,'¿Cuál es el resultado de (-3)² - 4?','-5','5','9','13','5'),
	(18,'Si el perímetro de un triángulo equilátero es 36, ¿cuánto mide cada lado?','9','10','12','15','12'),
	(19,'Factoriza: x² - 9','(x-3)(x+3)','(x-9)(x+1)','(x-1)(x-9)','(x+9)(x-3)','(x-3)(x+3)'),
	(20,'Convierte 150° a radianes (π≈3,14)','5π/6','π/2','3π/4','2π/3','5π/6'),

	(21,'Resuelve: 2(x+3)=4x-6','x=0','x=3','x=6','x=-3','x=3'),
	(22,'Si f(x)=2x²-3x, ¿cuál es f(-2)?','-10','-14','-2','2','-14'),
	(23,'El producto notable (x+2)² es:','x²+2','x²+4x+4','x²+2x+2','x²+2x+4','x²+4x+4'),
	(24,'Resuelve la ecuación: (x-1)(x+2)=0','x=-2 o x=1','x=2 o x=-1','x=0 o x=2','x=1 o x=2','x=-2 o x=1'),
	(25,'Si una recta tiene pendiente 2 y pasa por (0,3), su ecuación es:','y=2x+3','y=3x+2','y=2x-3','y=x+2','y=2x+3'),
	(26,'Simplifica: (2x²y³)(3xy²)','6x³y⁵','5x³y⁵','6x²y⁵','6x³y⁶','6x³y⁵'),
	(27,'El discriminante de x²-4x+3 es:','-2','0','4','16','4'),
	(28,'Si a=2 y b=-3, calcula a²+2ab+b²','1','25','0','9','1'),
	(29,'El mínimo común múltiplo entre 18 y 24 es:','36','72','48','54','72'),
	(30,'Si en un triángulo rectángulo los catetos miden 5 y 12, la hipotenusa mide:','12','13','14','15','13'),
]

SEGUNDO_MEDIO=[
	
	(1,'¿Cuál es el resultado de 4^-1?','4','-1/4','1/4','-4','1/4'),
	(2,'Simplifica: √49','5','6','7','8','7'),
	(3,'El cubo de 2 es:','4','6','8','16','8'),
	(4,'Si log₁₀(100)=x, ¿cuánto vale x?','1','2','10','100','2'),
	(5,'¿Cuál es el coseno de 60°?','0','1/2','√2/2','√3/2','1/2'),
	(6,'Resuelve: (2x+5)=15','x=3','x=5','x=7','x=10','x=5'),
	(7,'¿Cuál es la pendiente de la recta que pasa por (0,0) y (2,4)?','1','2','3','4','2'),
	(8,'El área de un círculo de radio 7 es:','49π','14π','7π','28π','49π'),
	(9,'Factoriza: x²+5x+6','(x+2)(x+3)','(x-2)(x+3)','(x-1)(x+6)','(x+1)(x+5)','(x+2)(x+3)'),
	(10,'Si senθ=0,5 entonces θ=','30°','45°','60°','90°','30°'),
			
	(11,'Resuelve: 2^x=16','x=2','x=3','x=4','x=5','x=4'),
	(12,'Simplifica: (x²y)(3xy²)','3x³y³','3x³y²','3x²y³','3x³y⁴','3x³y³'),
	(13,'La ecuación de una recta con pendiente -1 y que pasa por (0,2) es:','y=-x+2','y=x+2','y=-x-2','y=2x-1','y=-x+2'),
	(14,'El perímetro de un hexágono regular de lado 5 es:','20','25','30','35','30'),
	(15,'Resuelve: 5(x-2)=15','x=1','x=2','x=3','x=4','x=5'),
	(16,'Si log₂(32)=n, entonces n=','4','5','6','16','5'),
	(17,'Convierte 120° a radianes','2π/3','π/2','5π/6','3π/4','2π/3'),
	(18,'Simplifica: (x³)²','x³','x⁵','x⁶','x²','x⁶'),
	(19,'El coseno de 0° es:','0','1','-1','2','1'),
	(20,'Si tanθ=1, entonces θ=','30°','45°','60°','90°','45°'),
			
	(21,'Resuelve: x²-9=0','x=±3','x=±9','x=±√9','x=0','x=±3'),
	(22,'El discriminante de x²+6x+9 es:','-3','0','9','36','0'),
	(23,'Si a=3 y b=4, halla √(a²+b²)','5','6','7','25','5'),
	(24,'El área de un triángulo de base 10 y altura 8 es:','20','40','50','80','40'),
	(25,'Si sen²θ+cos²θ=?','0','1','2','θ','1'),
	(26,'La solución de |x-4|=2 es:','x=2 o x=6','x=-2 o x=6','x=2 o x=-6','x=-2 o x=-6','x=2 o x=6'),
	(27,'Resuelve: 3^(x)=27','x=2','x=3','x=4','x=5','x=3'),
	(28,'Simplifica: (a²b³)/(ab)','a²b²','ab²','a³b²','a²b³','ab²'),
	(29,'Si en un triángulo isósceles los lados iguales miden 5 y la base 6, el perímetro es:','15','14','16','10','16'),
	(30,'El ángulo central que abarca un arco de 1/6 de circunferencia es:','30°','45°','60°','90°','60°')
]

TERCERO_MEDIO=[
	
	(1,'¿Cuál es la derivada de f(x)=x²?','1','x','2x','x²','2x'),
	(2,'La integral de f(x)=2x es:','x²','2x²','x²+C','2x²+C','x²+C'),
	(3,'Si log₁₀(1000)=n, ¿cuánto vale n?','2','3','10','1000','3'),
	(4,'La pendiente de la recta y=3x+5 es:','3','5','-3','1/3','3'),
	(5,'El límite de (2x²)/(x²) cuando x→∞ es:','0','1','2','∞','2'),
	(6,'La derivada de f(x)=senx es:','cosx','-cosx','senx','-senx','cosx'),
	(7,'Resuelve: e^x=1','x=0','x=1','x=∞','x=-1','x=0'),
	(8,'La función inversa de f(x)=x+5 es:','x+5','x-5','1/(x+5)','-x+5','x-5'),
	(9,'El vértice de la parábola y=x²-4x+3 es:','(2,-1)','(2,1)','(-2,-1)','(-2,1)','(2,-1)'),
	(10,'La ecuación de una circunferencia de radio 3 y centro (0,0) es:','x²+y²=3','x²+y²=9','x²+y²=6','x²+y²=12','x²+y²=9'),
			
	(11,'Resuelve: ln(e³)=','1','3','e','0','3'),
	(12,'La derivada de f(x)=3x³ es:','6x²','9x²','3x²','x³','9x²'),
	(13,'Si f(x)=1/x, su dominio es:','Todos los reales','x≠0','x>0','x<0','x≠0'),
	(14,'La ecuación de una recta perpendicular a y=2x+1 es:','y=1/2x+b','y=-1/2x+b','y=-2x+b','y=2x+b','y=-1/2x+b'),
	(15,'El límite de (5x+2)/(x) cuando x→∞ es:','0','5','∞','2','5'),
	(16,'Resuelve: log₂(8)=','1','2','3','4','3'),
	(17,'El discriminante de x²-6x+9 es:','0','9','-9','36','0'),
	(18,'Si senθ=3/5 y θ es agudo, cosθ=','4/5','5/4','-4/5','-3/5','4/5'),
	(19,'La función cuadrática y=x²+6x+5 tiene sus raíces en:','-1 y -5','1 y 5','-2 y -3','2 y 3','-1 y -5'),
	(20,'La derivada de f(x)=ln(x²) es:','1/x','2/x','2x','lnx','2/x'),
			
	(21,'Resuelve: ∫(3x²+2x)dx','x³+x²+C','x³+2x²+C','x³+x²+3x+C','3x³+2x²+C','x³+x²+C'),
	(22,'El dominio de f(x)=√(x-2) es:','x≥2','x>2','x≠2','x≤2','x≥2'),
	(23,'Si f(x)=x² y g(x)=√x, entonces (f∘g)(4)=','2','4','8','16','16'),
	(24,'La pendiente de la recta tangente a y=x² en x=2 es:','2','3','4','8','4'),
	(25,'Resuelve: |2x-5|=7','x=-1 o x=6','x=1 o x=-6','x=0 o x=6','x=6 o x=12','x=-1 o x=6'),
	(26,'Si P(A)=0.4 y P(B)=0.5 y son independientes, P(A∩B)=','0.9','0.2','0.25','0.1','0.2'),
	(27,'El límite de (x²-9)/(x-3) cuando x→3 es:','0','6','3','∞','6'),
	(28,'Resuelve la inequación: x²-4x<0','x<0 o x>4','0<x<4','x>0','x<4','0<x<4'),
	(29,'Si la probabilidad de ganar es 0.2, la de perder es:','0.8','0.2','0.5','1','0.8'),
	(30,'La ecuación exponencial 2^x=1/8 tiene como solución:','x=2','x=3','x=-3','x=-2','x=-3')
]

CUARTO_MEDIO=[
	
	(1,'La derivada de f(x)=e^x es:','1','e^x','x','ln(x)','e^x'),
	(2,'La integral de f(x)=cos(x) es:','sen(x)','-sen(x)','cos(x)+C','-cos(x)+C','sen(x)'),
	(3,'Resuelve: lim (sinx/x) cuando x→0','0','1','∞','No existe','1'),
	(4,'La función inversa de f(x)=2x es:','x/2','2x','1/(2x)','x²','x/2'),
	(5,'Si log₁₀(x)=2, entonces x=','10','100','1000','1/100','100'),
	(6,'La derivada de f(x)=ln(x) es:','1/x','x','ln(x)/x','e^x','1/x'),
	(7,'La integral de f(x)=1/x es:','ln|x|+C','1/x²+C','x+C','e^x+C','ln|x|+C'),
	(8,'El valor de e^0 es:','0','1','e','∞','1'),
	(9,'El vértice de y=(x-3)²+2 es:','(3,2)','(-3,2)','(2,3)','(-2,3)','(3,2)'),
	(10,'El discriminante de x²-2x-8=0 es:','4','36','-36','16','36'),
			
	(11,'La derivada de f(x)=sen(x)·cos(x) es:','cos²(x)-sen²(x)','2sen(x)cos(x)','sen²(x)+cos²(x)','1','cos²(x)-sen²(x)'),
	(12,'Resuelve: ∫(2x+1)dx','x²+x+C','2x²+C','x²+2x+C','2x²+x+C','x²+x+C'),
	(13,'El dominio de f(x)=1/(x²-4) es:','x≠±2','x>2','x<2','Todos los reales','x≠±2'),
	(14,'Si f(x)=ln(x²), su derivada es:','2/x','1/x²','ln(x)/x','x²','2/x'),
	(15,'La recta tangente a y=x³ en x=1 tiene pendiente:','1','2','3','0','3'),
	(16,'Resuelve: lim (x²-4)/(x-2) cuando x→2','0','2','4','∞','4'),
	(17,'El resultado de log₃(81) es:','2','3','4','5','4'),
	(18,'Si P(A)=0.3 y P(B)=0.5 y son independientes, P(A∩B)=','0.15','0.8','0.2','0.3','0.15'),
	(19,'El área bajo la curva f(x)=x en [0,2] es:','1','2','4','3','2'),
	(20,'El dominio de f(x)=√(9-x²) es:','x≤3','-3≤x≤3','x≥-3','Todos los reales','-3≤x≤3'),
			
	(21,'Resuelve: ∫(3x²-4x+1)dx','x³-2x²+x+C','x³-4x²+2x+C','3x³-4x²+C','3x³-2x²+2x+C','x³-2x²+x+C'),
	(22,'El límite de (e^x-1)/x cuando x→0 es:','0','1','e','∞','1'),
	(23,'La ecuación de la recta tangente a y=ln(x) en x=1 es:','y=x-1','y=ln(x)+1','y=x','y=1','y=x-1'),
	(24,'Resuelve: ∫(1/(1+x²))dx','arctan(x)+C','ln(x)+C','1/x+C','arcsin(x)+C','arctan(x)+C'),
	(25,'Si una variable aleatoria sigue distribución normal estándar, su media es:','0','1','-1','e','0'),
	(26,'El límite de (x³-27)/(x-3) cuando x→3 es:','0','9','27','∞','27'),
	(27,'Resuelve la ecuación diferencial dy/dx=2x','y=x²+C','y=2x²+C','y=x+C','y=2x+C','y=x²+C'),
	(28,'El área bajo f(x)=x² en [0,3] es:','3','6','9','27','9'),
	(29,'Si P(A)=0.4 y P(B)=0.6 y son mutuamente excluyentes, P(A∪B)=','0.24','1','0.2','1.0','1'),
	(30,'Resuelve: ∫e^(2x)dx','e^(2x)+C','2e^(2x)+C','1/2 e^(2x)+C','ln(e^(2x))+C','1/2 e^(2x)+C')
]

sql_insert_PR="INSERT INTO PRIMERO_MEDIO (id_question_pr, question_pr, alternative_n1_pr, alternative_n2_pr, alternative_n3_pr, alternative_n4_pr, answer_pr) VALUES (?,?,?,?,?,?,?)"
sql_insert_SG="INSERT INTO SEGUNDO_MEDIO (id_question_sg, question_sg, alternative_n1_sg, alternative_n2_sg, alternative_n3_sg, alternative_n4_sg, answer_sg) VALUES (?,?,?,?,?,?,?)"
sql_insert_TRC="INSERT INTO TERCERO_MEDIO (id_question_trc, question_trc, alternative_n1_trc, alternative_n2_trc, alternative_n3_trc, alternative_n4_trc, answer_trc) VALUES (?,?,?,?,?,?,?)"
sql_insert_CR="INSERT INTO CUARTO_MEDIO (id_question_cr, question_cr, alternative_n1_cr, alternative_n2_cr, alternative_n3_cr, alternative_n4_cr, answer_cr) VALUES (?,?,?,?,?,?,?)"

cursor.executemany(sql_insert_PR,PRIMERO_MEDIO)
cursor.executemany(sql_insert_SG,SEGUNDO_MEDIO)
cursor.executemany(sql_insert_TRC,TERCERO_MEDIO)
cursor.executemany(sql_insert_CR,CUARTO_MEDIO)

conn.commit()

conn.close()