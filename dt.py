import nbformat
from deep_translator import GoogleTranslator

# Ruta del notebook original
entrada = "Data_Cleaning_with_Python_and_Pandas.ipynb"

# Ruta del notebook traducido
salida = "Data_Cleaning_Traducido.ipynb"

# Cargar el notebook
with open(entrada, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Inicializar traductor
translator = GoogleTranslator(source='auto', target='es')

def traducir_markdown(texto):
    resultado = []
    bloque_codigo = False
    for linea in texto.split("\n"):
        if linea.strip().startswith("```"):
            bloque_codigo = not bloque_codigo
            resultado.append(linea)
        elif bloque_codigo or linea.strip() == "":
            resultado.append(linea)
        else:
            try:
                resultado.append(translator.translate(linea))
            except Exception as e:
                print(f"Error al traducir línea: {linea}\n{e}")
                resultado.append(linea)
    return "\n".join(resultado)

# Traducir celdas de tipo markdown
for celda in nb.cells:
    if celda.cell_type == "markdown":
        celda.source = traducir_markdown(celda.source)

# Guardar el nuevo notebook
with open(salida, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Traducción completa guardada en: {salida}")
