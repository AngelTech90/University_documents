from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

def create_part1_pdf():
    # Crear documento PDF
    doc = SimpleDocTemplate("AngelReads_Parte1_Introduccion_Problema.pdf", pagesize=A4)
    
    # Obtener estilos y crear estilos personalizados
    styles = getSampleStyleSheet()
    
    # Estilos personalizados
    title_style = ParagraphStyle(
        'TituloPersonalizado',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=HexColor('#2c3e50')
    )
    
    section_style = ParagraphStyle(
        'TituloSeccion',
        parent=styles['Heading2'],
        fontSize=18,
        spaceAfter=20,
        spaceBefore=20,
        textColor=HexColor('#34495e')
    )
    
    subsection_style = ParagraphStyle(
        'TituloSubseccion',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=12,
        spaceBefore=12,
        textColor=HexColor('#7f8c8d')
    )
    
    content_style = ParagraphStyle(
        'EstiloContenido',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        leftIndent=20
    )
    
    bullet_style = ParagraphStyle(
        'EstiloViñeta',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=8,
        leftIndent=40,
        bulletIndent=20
    )
    
    design_tip_style = ParagraphStyle(
        'ConsejosDiseño',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=15,
        leftIndent=20,
        textColor=HexColor('#e74c3c'),
        backColor=HexColor('#fdf2f2'),
        borderColor=HexColor('#e74c3c'),
        borderWidth=1,
        borderPadding=10
    )
    
    # Lista de contenido
    content = []
    
    # Título
    content.append(Paragraph("Proyecto AngelReads - Parte 1", title_style))
    content.append(Paragraph("Introducción y Planteamiento del Problema", title_style))
    content.append(Spacer(1, 20))
    
    # 1. DIAPOSITIVA DE PORTADA/TÍTULO
    content.append(Paragraph("1. Diapositiva de Portada/Título (Aprox. 30 segundos)", section_style))
    
    content.append(Paragraph("Contenido:", subsection_style))
    content.append(Paragraph("• <b>Título del Proyecto:</b> [Nombre de tu proyecto, por ejemplo: \"AngelReads: Acceso Gratuito a Contenido de Calidad\"]", bullet_style))
    content.append(Paragraph("• <b>Membrete de la Universidad:</b> (Si aplica)", bullet_style))
    content.append(Paragraph("• <b>Nombres de los Miembros del Grupo</b>", bullet_style))
    
    content.append(Paragraph("<b>Consejo de Diseño (YouTube):</b> Usa espacio en blanco para que el título y los nombres destaquen. Asegúrate de que el texto sea lo suficientemente grande y generosamente espaciado. Menos es más en la portada.", design_tip_style))
    
    content.append(Spacer(1, 20))
    
    # 2. INTRODUCCIÓN
    content.append(Paragraph("2. Introducción (Aprox. 1 minuto)", section_style))
    
    content.append(Paragraph("Contenido:", subsection_style))
    content.append(Paragraph("• <b>¿Qué es AngelReads?</b> Presenta tu plataforma como un sitio de comercio electrónico que se enfoca en ofrecer <b>libros gratuitos disponibles en internet</b> [tu consulta].", bullet_style))
    content.append(Paragraph("• <b>Propósito Principal:</b> Facilitar la búsqueda de contenido de alta calidad para estudio, investigación o simplemente lectura [tu consulta].", bullet_style))
    
    content.append(Paragraph("<b>Consejo de Diseño (YouTube):</b> Evita el \"bombardeo de información\". Mantén los puntos clave claros y concisos. Puedes visualizar la idea principal con un icono o imagen relevante si es posible, usando Gráficos Vectoriales Escalables (SVG) para evitar pixelación al cambiar de tamaño.", design_tip_style))
    
    content.append(Spacer(1, 20))
    
    # 3. PLANTEAMIENTO DEL PROBLEMA
    content.append(Paragraph("3. Planteamiento del Problema (Aprox. 1 minuto)", section_style))
    
    content.append(Paragraph("Contenido:", subsection_style))
    content.append(Paragraph("• <b>El Desafío:</b> La dificultad actual de encontrar libros gratuitos de alta calidad y relevantes en internet de manera organizada y accesible [tu consulta].", bullet_style))
    content.append(Paragraph("• <b>Solución que Ofrece el Proyecto:</b> Cómo AngelReads resuelve esta dispersión y dificultad de acceso.", bullet_style))
    
    content.append(Paragraph("<b>Consejo de Diseño (YouTube):</b> Guía la mirada de la audiencia hacia la información más importante y evita distracciones. Puedes usar un gráfico simple o icono para representar la \"dispersión\" de información.", design_tip_style))
    
    content.append(Spacer(1, 20))
    
    # Resumen del Proyecto
    content.append(Paragraph("Resumen del Proyecto", section_style))
    content.append(Paragraph("AngelReads es una plataforma de comercio electrónico que se enfoca en ofrecer libros gratuitos disponibles en internet, facilitando a las personas encontrar contenido de alta calidad para estudio, investigación o simplemente leer un buen libro. El modelo de negocio se basa en publicidad del sitio web y búsqueda de futuros patrocinadores.", content_style))
    
    content.append(Paragraph("Características Principales:", subsection_style))
    content.append(Paragraph("• Blog integrado donde los operadores del proyecto publican reseñas sobre libros interesantes", bullet_style))
    content.append(Paragraph("• Sistema de reseñas donde las personas pueden dejar calificaciones de 1-5 estrellas para cada libro disponible en la página", bullet_style))
    content.append(Paragraph("• Más de 10,000 libros disponibles", bullet_style))
    content.append(Paragraph("• Más de 7,000 clientes registrados", bullet_style))
    
    # Construir el PDF
    doc.build(content)
    print("PDF Parte 1 generado exitosamente: AngelReads_Parte1_Introduccion_Problema.pdf")

if __name__ == "__main__":
    create_part1_pdf()
