from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR
import os

def create_free_books_ecommerce_presentation():
    """Crear una presentación integral sobre la plataforma e-commerce de libros gratuitos"""

    prs = Presentation()

    # Define modern color scheme
    PRIMARY_BLUE = RGBColor(41, 128, 185)
    DARK_BLUE = RGBColor(21, 67, 96)
    SUCCESS_GREEN = RGBColor(39, 174, 96)
    WARNING_ORANGE = RGBColor(230, 126, 34)
    DANGER_RED = RGBColor(231, 76, 60)
    PURPLE = RGBColor(142, 68, 173)
    DARK_GRAY = RGBColor(52, 73, 94)
    LIGHT_GRAY = RGBColor(149, 165, 166)

    def add_title_slide(title, subtitle=""):
        slide_layout = prs.slide_layouts[0]
        slide = prs.slides.add_slide(slide_layout)

        title_shape = slide.shapes.title
        subtitle_shape = slide.placeholders[1]

        title_shape.text = title
        title_shape.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE
        title_shape.text_frame.paragraphs[0].font.size = Pt(44)
        title_shape.text_frame.paragraphs[0].font.bold = True

        if subtitle:
            subtitle_shape.text = subtitle
            subtitle_shape.text_frame.paragraphs[0].font.color.rgb = PRIMARY_BLUE
            subtitle_shape.text_frame.paragraphs[0].font.size = Pt(28)

        return slide

    def add_content_slide(title, content_points):
        slide_layout = prs.slide_layouts[1]
        slide = prs.slides.add_slide(slide_layout)

        title_shape = slide.shapes.title
        content_shape = slide.placeholders[1]

        title_shape.text = title
        title_shape.text_frame.paragraphs[0].font.color.rgb = DARK_BLUE
        title_shape.text_frame.paragraphs[0].font.size = Pt(36)
        title_shape.text_frame.paragraphs[0].font.bold = True

        tf = content_shape.text_frame
        tf.clear()

        for i, point in enumerate(content_points):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = point
            p.level = 0
            p.font.size = Pt(20)
            p.font.color.rgb = DARK_GRAY
            p.space_after = Pt(8)

        return slide

    def add_feature_slide(title, features_dict):
        slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(slide_layout)

        title_shape = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.8))
        title_frame = title_shape.text_frame
        title_frame.text = title
        title_frame.paragraphs[0].font.size = Pt(36)
        title_frame.paragraphs[0].font.color.rgb = DARK_BLUE
        title_frame.paragraphs[0].font.bold = True
        title_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

        y_pos = 1.5
        for feature, description in features_dict.items():
            feature_shape = slide.shapes.add_textbox(Inches(0.8), Inches(y_pos), Inches(8.4), Inches(0.5))
            feature_frame = feature_shape.text_frame
            feature_frame.text = f"🔹 {feature}"
            feature_frame.paragraphs[0].font.size = Pt(22)
            feature_frame.paragraphs[0].font.color.rgb = PRIMARY_BLUE
            feature_frame.paragraphs[0].font.bold = True

            desc_shape = slide.shapes.add_textbox(Inches(1.2), Inches(y_pos + 0.4), Inches(8), Inches(0.6))
            desc_frame = desc_shape.text_frame
            desc_frame.text = description
            desc_frame.paragraphs[0].font.size = Pt(16)
            desc_frame.paragraphs[0].font.color.rgb = DARK_GRAY

            y_pos += 1.2

        return slide

    def add_comparison_slide(title, left_title, left_points, right_title, right_points):
        slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(slide_layout)

        title_shape = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.8))
        title_frame = title_shape.text_frame
        title_frame.text = title
        title_frame.paragraphs[0].font.size = Pt(32)
        title_frame.paragraphs[0].font.color.rgb = DARK_BLUE
        title_frame.paragraphs[0].font.bold = True
        title_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

        left_shape = slide.shapes.add_textbox(Inches(0.5), Inches(1.3), Inches(4.2), Inches(5.5))
        left_frame = left_shape.text_frame
        left_frame.text = left_title
        left_frame.paragraphs[0].font.size = Pt(24)
        left_frame.paragraphs[0].font.color.rgb = SUCCESS_GREEN
        left_frame.paragraphs[0].font.bold = True

        for point in left_points:
            p = left_frame.add_paragraph()
            p.text = f"✓ {point}"
            p.font.size = Pt(16)
            p.font.color.rgb = DARK_GRAY
            p.space_after = Pt(6)

        right_shape = slide.shapes.add_textbox(Inches(5.3), Inches(1.3), Inches(4.2), Inches(5.5))
        right_frame = right_shape.text_frame
        right_frame.text = right_title
        right_frame.paragraphs[0].font.size = Pt(24)
        right_frame.paragraphs[0].font.color.rgb = WARNING_ORANGE
        right_frame.paragraphs[0].font.bold = True

        for point in right_points:
            p = right_frame.add_paragraph()
            p.text = f"⚠ {point}"
            p.font.size = Pt(16)
            p.font.color.rgb = DARK_GRAY
            p.space_after = Pt(6)

        return slide

    def add_technical_slide(title, tech_stack):
        slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(slide_layout)

        title_shape = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.8))
        title_frame = title_shape.text_frame
        title_frame.text = title
        title_frame.paragraphs[0].font.size = Pt(32)
        title_frame.paragraphs[0].font.color.rgb = DARK_BLUE
        title_frame.paragraphs[0].font.bold = True
        title_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

        colors = [PRIMARY_BLUE, SUCCESS_GREEN, WARNING_ORANGE, PURPLE]
        x_positions = [1, 3, 5, 7]

        for i, (category, technologies) in enumerate(tech_stack.items()):
            box_shape = slide.shapes.add_textbox(Inches(x_positions[i % 4]), Inches(1.8), Inches(1.8), Inches(3.5))
            box_frame = box_shape.text_frame
            box_frame.text = category
            box_frame.paragraphs[0].font.size = Pt(18)
            box_frame.paragraphs[0].font.color.rgb = colors[i % 4]
            box_frame.paragraphs[0].font.bold = True
            box_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

            for tech in technologies:
                p = box_frame.add_paragraph()
                p.text = f"• {tech}"
                p.font.size = Pt(14)
                p.font.color.rgb = DARK_GRAY
                p.alignment = PP_ALIGN.CENTER

        return slide

    def add_intro_slide():
        return add_content_slide(
            "🔍 ¿Qué es LibraryLink?",
            [
                "LibraryLink es una plataforma e-commerce innovadora enfocada en libros digitales gratuitos",
                "Ofrece una experiencia de usuario centrada en la accesibilidad, curación y descubrimiento eficiente",
                "Nace con el propósito de cerrar la brecha educativa a nivel global",
                "Integra tecnología, comunidad y sostenibilidad en un solo ecosistema"
            ]
        )

    def add_conclusion_slide():
        slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(slide_layout)

        title_shape = slide.shapes.add_textbox(Inches(1), Inches(1), Inches(8), Inches(1))
        title_frame = title_shape.text_frame
        title_frame.text = "🎉 Conclusión y Próximos Pasos"
        title_frame.paragraphs[0].font.size = Pt(36)
        title_frame.paragraphs[0].font.bold = True
        title_frame.paragraphs[0].font.color.rgb = DARK_BLUE
        title_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

        content_shape = slide.shapes.add_textbox(Inches(1.2), Inches(2.2), Inches(7.5), Inches(4))
        content_frame = content_shape.text_frame

        points = [
            "LibraryLink redefine el acceso abierto a recursos educativos digitales",
            "Ofrece un modelo sostenible con impacto social real",
            "Conecta a estudiantes, instituciones y profesionales en una comunidad de aprendizaje",
            "📌 Próximos pasos: Lanzamiento beta, feedback de usuarios, alianzas estratégicas"
        ]

        for point in points:
            p = content_frame.add_paragraph()
            p.text = f"• {point}"
            p.font.size = Pt(20)
            p.font.color.rgb = DARK_GRAY
            p.space_after = Pt(10)

        return slide

    # SLIDES SEQUENCE
    add_title_slide(
        "📚 LibraryLink: Plataforma E-commerce de Libros Gratuitos",
        "Democratizando el Acceso al Conocimiento a través de la Innovación Digital"
    )

    add_intro_slide()

    add_content_slide("🎯 Misión y Visión del Proyecto", [
        "Misión: Hacer que el contenido educativo de alta calidad sea accesible gratuitamente para todos",
        "Visión: Crear la plataforma curada más grande del mundo para libros digitales gratuitos",
        "Objetivo: Estudiantes, investigadores, profesionales y aprendices de por vida",
        "Impacto: Cerrar la brecha digital en recursos educativos",
        "Sostenibilidad: Ingresos a través de publicidad ética y patrocinios"
    ])

    add_content_slide("📊 Análisis del Problema de Mercado", [
        "Desigualdad educativa: 60% de estudiantes carecen de acceso a libros de texto de calidad",
        "Altos costos: Los precios de libros de texto han aumentado 812% desde 1978",
        "Fragmentación digital: Libros gratuitos dispersos en múltiples plataformas",
        "Preocupaciones de calidad: Falta de curación y sistemas de reseñas",
        "Desafíos de descubrimiento: Los usuarios luchan por encontrar contenido relevante",
        "Barreras idiomáticas: Recursos educativos multilingües limitados"
    ])

    add_content_slide("💡 Nuestra Solución Innovadora", [
        "Plataforma centralizada que agrega libros gratuitos de fuentes verificadas",
        "Sistema de curación avanzado con reseñas de expertos y calificaciones",
        "Motor de recomendaciones impulsado por IA para descubrimiento personalizado",
        "Aseguramiento de calidad impulsado por la comunidad a través de comentarios de usuarios",
        "Soporte multiidioma con capacidades de traducción",
        "Diseño accesible siguiendo las pautas WCAG 2.1"
    ])

    add_feature_slide("🚀 Características Principales de la Plataforma", {
        "Búsqueda Inteligente y Descubrimiento": "Búsqueda avanzada con filtros por materia, nivel, idioma y formato",
        "Sistema de Reseñas de Expertos": "Bibliotecarios profesionales y educadores proporcionan reseñas detalladas de libros",
        "Sistema de Calificación de 5 Estrellas": "Calificaciones impulsadas por la comunidad ayudan a los usuarios a identificar contenido de calidad",
        "Recomendaciones Personalizadas": "Algoritmos de IA sugieren libros basados en historial de lectura y preferencias",
        "Listas de Lectura y Colecciones": "Los usuarios pueden crear y compartir colecciones curadas de libros",
        "Características Sociales": "Clubes de lectura, foros de discusión y desafíos de lectura"
    })

    add_content_slide("💰 Modelo de Negocio Sostenible", [
        "Ingresos Principales: Publicidad contextual relevante al contenido educativo",
        "Contenido Patrocinado: Instituciones educativas y editoriales patrocinan recomendaciones de libros",
        "Características Premium: Analíticas avanzadas y listas de lectura ilimitadas ($5/mes)",
        "Asociaciones Corporativas: Soluciones B2B para escuelas y bibliotecas",
        "Marketing de Afiliados: Asociaciones éticas con servicios educativos",
        "Donaciones: Contribuciones opcionales de usuarios para apoyar el desarrollo de la plataforma"
    ])

    add_content_slide("👤 Jornada de Experiencia del Usuario", [
        "1. Descubrimiento: Los usuarios llegan a la página de inicio con libros populares y categorías",
        "2. Búsqueda: Búsqueda avanzada con autocompletado inteligente y filtros",
        "3. Evaluación: Ver detalles del libro, reseñas de expertos y calificaciones de la comunidad",
        "4. Acceso: Acceso con un clic a libros gratuitos de fuentes verificadas",
        "5. Participación: Calificar libros, escribir reseñas y unirse a discusiones",
        "6. Personalización: Recibir recomendaciones personalizadas y listas de lectura"
    ])

    add_content_slide("✅ Marco de Aseguramiento de Calidad", [
        "Verificación de Fuentes: Solo libros de fuentes legítimas y que cumplen con derechos de autor",
        "Curación de Expertos: Bibliotecarios profesionales revisan todas las adiciones de libros",
        "Moderación Comunitaria: Contenido reportado por usuarios revisado dentro de 24 horas",
        "Escaneo Automatizado: Herramientas de IA detectan contenido potencialmente dañino o inapropiado",
        "Pruebas de Accesibilidad: Todos los libros probados para compatibilidad con lectores de pantalla",
        "Auditorías Regulares: Revisiones mensuales de calidad y detección de enlaces rotos"
    ])

    add_comparison_slide("💼 Análisis de Fuentes de Ingresos",
        "Fuentes de Ingresos Principales", [
            "Publicidad de display (70% de ingresos)",
            "Recomendaciones de libros patrocinadas (20%)",
            "Suscripciones premium (8%)",
            "Asociaciones corporativas (2%)"
        ],
        "Estrategias de Crecimiento", [
            "Expandir a instituciones académicas",
            "Desarrollar aplicaciones móviles",
            "Agregar soporte para audiolibros",
            "Expansión a mercados internacionales"
        ]
    )

    add_content_slide("📈 Estrategia de Marketing y Crecimiento", [
        "Marketing de Contenido: Blog educativo con consejos de estudio y recomendaciones de libros",
        "Redes Sociales: Presencia activa en Twitter, LinkedIn y grupos educativos de Facebook",
        "Optimización SEO: Dirigir palabras clave de cola larga relacionadas con recursos educativos gratuitos",
        "Construcción de Comunidad: Asociarse con organizaciones estudiantiles y grupos de estudio en línea",
        "Asociaciones con Influencers: Colaborar con educadores e influencers académicos",
        "Email Marketing: Boletín semanal con recomendaciones curadas de libros"
    ])

    add_comparison_slide("🏆 Ventaja Competitiva",
        "Nuestras Fortalezas", [
            "Contenido curado de calidad",
            "Sistema de reseñas de expertos",
            "Motor de recomendaciones avanzado",
            "Calificaciones impulsadas por la comunidad",
            "Diseño centrado en accesibilidad",
            "Modelo de ingresos éticos"
        ],
        "Diferenciadores de Mercado", [
            "Enfoque en contenido educativo",
            "Proceso de curación profesional",
            "Soporte multiidioma",
            "Características de aprendizaje social",
            "Sourcing transparente",
            "Experiencia de lectura sin anuncios"
        ]
    )

    add_conclusion_slide()

    return prs

def main():
    print("🚀 Generando Presentación de Plataforma E-commerce de Libros Gratuitos...")
    try:
        presentation = create_free_books_ecommerce_presentation()
        filename = "LibraryLink_Plataforma_Libros_Gratuitos_Presentacion.pptx"
        presentation.save(filename)
        print(f"✅ Presentación guardada como '{filename}' en:\n{os.path.abspath(filename)}")
    except Exception as e:
        print(f"❌ Error creando presentación: {str(e)}")

if __name__ == "__main__":
    main()

