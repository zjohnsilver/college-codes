arquivo = open("ola.html", 'w', encoding = "utf-8")
arquivo.write("""<!DOCTYPE html>
<html lang="pt-R">
<head>
<meta charset="utf-8">
<tittle>Título da Página</title>
</head>
<body>
JOÃO CARLOS!
</body>
</html>""")

arquivo.close()