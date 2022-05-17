'''
Deteermine si un tablero de sudoku es válido.
Solo las celdas llenas debe validarce segun las siguientes reglas.

1 Chequear ue el tablero introducido sea un tablero 9 por nueve 
    Usaremos assert palabra reservada q nos permite chequear que se respete irta condicion de nuestro codigo y en el casso de que no se respete da una exepcion, como si uara un ifUsa

2 Cada fila debe conteener los digtos del 1-9 sin repetición.

3 Cada columna debe conteer los digitos del 1-9 sin repetición.

4 Cada uno de los nueve subcuadros de 3 por 3 de la cuadrícula debe cotener los digitos del 1-9 sin repeticion.
'''

board = [
    ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]

class validateSudoku:
    def __init__(self,tablero) -> None:
        self.tablero = tablero
        self.lista_invertida = list()
   
    def chequeo_general(self):  #primera condición
        #assert
       assert len(self.tablero) == 9, "El tablero ingresado no respeta la condición 9 por 9" #filas
       for fila in self.tablero:
           assert len(fila) == 9, "El tablero ingresado no respeta la condición 9 por 9" #columnas

    def chequeoFilas(self,lista_a_chequear='tablero_general'): # segunda condición
        if lista_a_chequear== 'tablero_general':
            lista_a_chequear=self.tablero
        for fila in lista_a_chequear:
            for elemento in fila:
                if elemento != '.':
                    assert fila.count(elemento)== 1, "El tablero ingresado no es valido, se repiten valores"

    def chequeoColumnas(self): #Tercera condición
        for column_index in range(0,9):
            for row_index in range(0,9):
                self.lista_invertida.append(self.tablero[row_index][column_index])
            self.chequeoFilas(self.lista_invertida)
            self.lista_invertida.clear()
                    

# Instanciar el objeto
sudoku= validateSudoku(board)
sudoku.chequeo_general()
sudoku.chequeoFilas()
sudoku.chequeoColumnas()