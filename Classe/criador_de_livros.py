from livro import Livro

livro1 = Livro('Curso de Python em 6h','Alcimar Costa', 'Udemy', '878-98-9988-988-9', 2018)
livro2 = Livro('Python para web', 'Alcimar Costa', 'Udemy', '999-99-999-9999-9', 2018)
livro3 = Livro('Inteligência Artificial', 'Alcimar Costa', 'Udemy', '888-88-8888-88', 2018)


livros = [livro1, livro2, livro3]

for l in livros:
    print(l)