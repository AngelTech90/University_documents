from fpdf import FPDF
import textwrap
from datetime import datetime

class CustomPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Manual del Jugador: Mokepon World', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', True)
        self.ln(5)

    def chapter_body(self, text):
        self.set_font('Arial', '', 11)
        lines = textwrap.wrap(text, width=85)
        for line in lines:
            self.multi_cell(0, 6, line)
        self.ln(5)

def create_player_manual():
    pdf = CustomPDF()

    # Section 1: Introducción
    pdf.add_page()
    pdf.chapter_title("1. Introducción")
    intro_text = """Bienvenido a Mokepon World, un emocionante juego donde puedes seleccionar diferentes criaturas 
    llamadas Mokepons y luchar contra otros jugadores. Este manual te guiará a través de las reglas del juego, 
    las ventajas de cada Mokepon y cómo interactúan los diferentes tipos."""
    pdf.chapter_body(intro_text)

    # Section 2: Reglas del Juego
    pdf.add_page()
    pdf.chapter_title("2. Reglas del Juego")
    rules_text = """Las reglas del juego son simples:
    
    1. Selecciona tu Mokepon de la lista de criaturas disponibles.
    2. Cada Mokepon tiene un tipo (por ejemplo, fuego, agua, tierra) que determina sus ventajas y desventajas en combate.
    3. Durante el combate, selecciona un ataque de tu Mokepon.
    4. El resultado del combate se determina por las interacciones de tipo entre tu Mokepon y el Mokepon del oponente.
    5. Gana el jugador que logre más victorias al final de la serie de combates."""
    pdf.chapter_body(rules_text)

    # Section 3: Tipos de Mokepons y Ventajas
    pdf.add_page()
    pdf.chapter_title("3. Tipos de Mokepons y Ventajas")
    types_text = """Cada Mokepon pertenece a uno o más tipos, y cada tipo tiene ventajas sobre otros. Aquí están los tipos y sus interacciones:

    - **Fuego**: Ventaja sobre Hielo, Rayo, y Acero.
    - **Agua**: Ventaja sobre Fuego, Tierra, y Rayo.
    - **Tierra**: Ventaja sobre Fuego, Rayo, y Acero.
    - **Hielo**: Ventaja sobre Agua, Tierra, y Aire.
    - **Rayo**: Ventaja sobre Hielo, Acero, y Aire.
    - **Acero**: Ventaja sobre Hielo, Agua, y Aire.
    - **Aire**: Ventaja sobre Fuego, Agua, y Tierra.

    Al seleccionar un Mokepon, considera sus tipos y cómo se enfrentan a los tipos de tus oponentes para maximizar tus posibilidades de ganar."""
    pdf.chapter_body(types_text)

    # Section 4: Ejemplo de Combate
    pdf.add_page()
    pdf.chapter_title("4. Ejemplo de Combate")
    combat_example_text = """Imagina que eliges a Raykiou (tipo Fuego) y te enfrentas a Crabster (tipo Agua). 
    En este caso, Raykiou tiene una desventaja, ya que el Agua es fuerte contra el Fuego. 
    Por lo tanto, Crabster ganaría el combate. Sin embargo, si eliges a Joka (tipo Tierra) contra Crabster, 
    Joka tendría la ventaja, ya que Tierra es fuerte contra Agua."""
    pdf.chapter_body(combat_example_text)

    # Section 5: Consejos para Jugadores
    pdf.add_page()
    pdf.chapter_title("5. Consejos para Jugadores")
    tips_text = """- Conoce las ventajas y desventajas de cada tipo para hacer elecciones estratégicas.
    - Experimenta con diferentes combinaciones de Mokepons para encontrar la que mejor se adapte a tu estilo de juego.
    - Presta atención a las selecciones de tus oponentes y ajusta tu estrategia en consecuencia."""
    pdf.chapter_body(tips_text)

    # Save the PDF
    filename = f"./generated_documents/manual_jugador_mokepon_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(filename)
    return filename

if __name__ == "__main__":
    try:
        output_file = create_player_manual()
        print(f"PDF generado con éxito: {output_file}")
    except Exception as e:
        print(f"Error al generar el PDF: {str(e)}")

