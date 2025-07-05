from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

def create_part2_pdf():
    # Crear documento PDF
    doc = SimpleDocTemplate("AngelReads_Parte2_Objetivos_Plataforma.pdf", pagesize=A4)
    
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
    content.append(Paragraph("Proyecto AngelReads - Parte 2", title_style))
    content.append(Paragraph("Objetivos y Presentación de la Plataforma Web", title_style))
    content.append(Spacer(1, 20))
    
    # 4. OBJETIVOS
    content.append(Paragraph("4. Objetivos (General y Específicos) (Aprox. 1.5 minutos)", section_style))
    
    content.append(Paragraph("Contenido:", subsection_style))
    content.append(Paragraph("• <b>Objetivo General:</b> Proporcionar una plataforma centralizada y fácil de usar para acceder a una vasta colección de libros gratuitos en línea [tu consulta].", bullet_style))
    
    content.append(Paragraph("• <b>Objetivos Específicos:</b>", bullet_style))
    content.append(Paragraph("  - Ofrecer una amplia gama de libros (+10,000 Libros)", bullet_style))
    content.append(Paragraph("  - Facilitar el descubrimiento de contenido de alta calidad [tu consulta]", bullet_style))
    content.append(Paragraph("  - Fomentar una comunidad a través de un blog y sistema de reseñas [tu consulta]", bullet_style))
    content.append(Paragraph("  - Establecer un modelo de negocio sostenible a través de publicidad del sitio web y futuros patrocinadores [tu consulta]", bullet_style))
    
    content.append(Paragraph("<b>Consejo de Diseño (YouTube):</b> Visualiza estos objetivos. Podrías usar iconos para cada objetivo específico en lugar de solo texto, o un gráfico de lista que sea fácil de escanear. Recuerda el principio de \"menos es más\" para que la audiencia no se sienta abrumada con texto.", design_tip_style))
    
    content.append(Spacer(1, 20))
    
    # 5. PRESENTACIÓN DE LA PÁGINA WEB
    content.append(Paragraph("5. Presentación de la Página Web (Funcionalidad y Características) (Aprox. 5 minutos)", section_style))
    
    content.append(Paragraph("<b>IMPORTANTE:</b> Esta es la sección más importante. Debes hacer una <b>demostración en vivo</b> del sitio web si es posible, o usar capturas de pantalla bien diseñadas y grandes si no puedes.", content_style))
    
    content.append(Paragraph("Resumen General de la Plataforma \"AngelReads\":", subsection_style))
    
    content.append(Paragraph("• <b>Interfaz de Usuario:</b> Menciona secciones clave como \"Iniciar Sesión\", \"Inicio\", \"Libros\", \"Libros Electrónicos\", \"Audiolibros\"", bullet_style))
    content.append(Paragraph("• <b>Contenido Disponible:</b> Destaca que tienen <b>+10,000 Libros</b> y <b>+7,000 Clientes</b>", bullet_style))
    content.append(Paragraph("• <b>Categorías de Libros:</b> Muestra cómo se organizan los libros (Libros Populares, Tendencias de la semana, Top 10 del mes, Más vendidos, Ofertas relámpago, Libros destacados)", bullet_style))
    content.append(Paragraph("• <b>Blog Integrado:</b> Explica que la sección \"Últimas noticias\" funciona como un blog donde tú y otros operadores publican reseñas sobre libros interesantes", bullet_style))
    content.append(Paragraph("• <b>Sistema de Reseñas:</b> Describe cómo los usuarios pueden dejar calificaciones de 1 a 5 estrellas para cada libro y cómo se muestran los \"Testimonios\"", bullet_style))
    content.append(Paragraph("• <b>Modelo de Negocio:</b> Reitera que la monetización se basa en <b>publicidad del sitio web</b> y búsqueda de <b>futuros patrocinadores</b>. (Aunque \"AngelReads\" menciona \"Pago Seguro\", \"Entrega Rápida\", \"Mejor Calidad\", \"Garantía de Devolución\", dado tu enfoque en libros gratuitos y modelo de negocio, prioriza y explica cómo estas características se integran en el valor general de la plataforma de acceso gratuito, o si son características generales del sitio que podrían usarse para futuros modelos premium no directamente relacionados con los libros gratuitos ofrecidos actualmente)", bullet_style))
    
    content.append(Paragraph("Tecnología y Desarrollo (Referencia de GitHub):", subsection_style))
    content.append(Paragraph("• <b>Propósito del Repositorio:</b> Menciona que el repositorio de GitHub (AngelTech90/TailwindCSS-Alpine.JS) sirve para <b>probar características de Tailwind y desarrollar proyectos pequeños</b>. Esto muestra tu base técnica.", bullet_style))
    content.append(Paragraph("• <b>Tecnologías Utilizadas:</b> Destaca los lenguajes principales del repositorio: <b>HTML (88.4%)</b>, <b>CSS (9.7%)</b>, y <b>JavaScript (1.9%)</b>. Esto indica cómo construiste la interfaz.", bullet_style))
    content.append(Paragraph("• <b>Sitio Desplegado:</b> Menciona que el sitio tiene una versión desplegada (\"Sitio desplegado\")", bullet_style))
    
    content.append(Paragraph("<b>Consejo de Diseño (YouTube):</b>", design_tip_style))
    content.append(Paragraph("• <b>Visualiza tus datos:</b> Si muestras capturas de pantalla, asegúrate de que sean de alta calidad y guíen la vista hacia lo más importante.", design_tip_style))
    content.append(Paragraph("• <b>Usa la \"Regla de los Tercios\":</b> Al organizar capturas de pantalla y texto, considera colocar elementos clave en los puntos de intersección de \"PowerPoint\" (puntos de intersección de la regla de los tercios) o a lo largo de las líneas de cuadrícula imaginarias. Esto hace que la diapositiva sea más atractiva visualmente. Puedes activar guías en PowerPoint para ayudarte.", design_tip_style))
    content.append(Paragraph("• <b>Diseño Limpio:</b> Evita la sobrecarga visual. Si usas capturas de pantalla, deja \"espacio para respirar\" o espacio en blanco.", design_tip_style))
    
    content.append(Spacer(1, 20))
    
    # Detalles de Implementación Técnica
    content.append(Paragraph("Detalles de Implementación Técnica", section_style))
    content.append(Paragraph("La plataforma AngelReads está construida usando tecnologías web modernas que aseguran una experiencia receptiva y amigable para el usuario:", content_style))
    
    content.append(Paragraph("Tecnologías Frontend:", subsection_style))
    content.append(Paragraph("• <b>HTML (88.4%):</b> Estructura y organización del contenido", bullet_style))
    content.append(Paragraph("• <b>CSS (9.7%):</b> Estilizado y diseño receptivo con TailwindCSS", bullet_style))
    content.append(Paragraph("• <b>JavaScript (1.9%):</b> Características interactivas y contenido dinámico con Alpine.JS", bullet_style))
    
    content.append(Paragraph("Características de la Plataforma:", subsection_style))
    content.append(Paragraph("• Diseño receptivo que funciona en todos los dispositivos", bullet_style))
    content.append(Paragraph("• Tiempos de carga rápidos y rendimiento optimizado", bullet_style))
    content.append(Paragraph("• Interfaz de usuario limpia e intuitiva", bullet_style))
    content.append(Paragraph("• Arquitectura escalable para crecimiento futuro", bullet_style))
    
    # Construir el PDF
    doc.build(content)
    print("PDF Parte 2 generado exitosamente: AngelReads_Parte2_Objetivos_Plataforma.pdf")

if __name__ == "__main__":
    create_part2_pdf()
