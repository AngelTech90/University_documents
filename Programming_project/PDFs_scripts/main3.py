from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

def crear_parte3_pdf():
    # Crear documento PDF
    doc = SimpleDocTemplate("AngelReads_Parte3_Conclusion_Instrucciones.pdf", pagesize=A4)
    
    # Obtener estilos y crear estilos personalizados
    styles = getSampleStyleSheet()
    
    # Estilos personalizados
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=HexColor('#2c3e50')
    )
    
    section_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=18,
        spaceAfter=20,
        spaceBefore=20,
        textColor=HexColor('#34495e')
    )
    
    subsection_style = ParagraphStyle(
        'SubsectionTitle',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=12,
        spaceBefore=12,
        textColor=HexColor('#7f8c8d')
    )
    
    content_style = ParagraphStyle(
        'ContentStyle',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        leftIndent=20
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=8,
        leftIndent=40,
        bulletIndent=20
    )
    
    design_tip_style = ParagraphStyle(
        'DesignTip',
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
    
    instruction_style = ParagraphStyle(
        'InstructionStyle',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=15,
        leftIndent=20,
        textColor=HexColor('#2980b9'),
        backColor=HexColor('#f8f9fa'),
        borderColor=HexColor('#2980b9'),
        borderWidth=1,
        borderPadding=10
    )
    
    # Lista de contenido
    content = []
    
    # Título
    content.append(Paragraph("Proyecto AngelReads - Parte 3", title_style))
    content.append(Paragraph("Conclusión e Instrucciones Finales", title_style))
    content.append(Spacer(1, 20))
    
    # 6. CONCLUSIÓN
    content.append(Paragraph("6. Conclusión (Aprox. 2 minutos)", section_style))
    
    content.append(Paragraph("Contenido:", subsection_style))
    content.append(Paragraph("• <b>Resumen de Logros:</b> Reafirmar cómo AngelReads cumple sus objetivos ofreciendo acceso fácil y gratuito a libros de calidad.", bullet_style))
    content.append(Paragraph("• <b>Impacto y Valor:</b> Resaltar el valor que tu proyecto aporta a la comunidad de lectores y estudiantes.", bullet_style))
    content.append(Paragraph("• <b>Próximos Pasos/Visión Futura:</b> Mencionar brevemente planes de crecimiento, como buscar activamente patrocinadores y expandir contenido o características [tu consulta].", bullet_style))
    content.append(Paragraph("• <b>Reconocimiento y Llamada a la Acción:</b> (ej., \"Visita AngelReads.com\").", bullet_style))
    
    content.append(Paragraph("<b>Consejo de Diseño (YouTube):</b> Una diapositiva de conclusión debe ser impactante. Aplica la misma filosofía de \"menos es más\" y enfócate en el mensaje principal.", design_tip_style))
    
    content.append(Spacer(1, 20))
    
    # INSTRUCCIONES FINALES
    content.append(Paragraph("Instrucciones y Directrices Finales", section_style))
    
    content.append(Paragraph("Usa como referencia para obtener información para la presentación el repositorio de GitHub y la página de GitHub. Explica en PowerPoint estas páginas usando puntos de tareas como referencia, mejora tu ortografía en el documento de PowerPoint y usa para mejorar la presentación los consejos del video de YouTube.", instruction_style))
    
    content.append(Paragraph("Detalles Clave del Proyecto:", subsection_style))
    content.append(Paragraph("Sobre qué es exactamente el proyecto: es un e-commerce que se enfoca en ofrecer libros gratuitos que están disponibles en internet, facilitando a las personas encontrar contenido de alta calidad para estudiar, investigar, o simplemente leer un buen libro. El modelo de negocio se basa en publicidad del sitio web y en el futuro encontrar patrocinadores.", content_style))
    
    content.append(Paragraph("Características Adicionales:", subsection_style))
    content.append(Paragraph("• La página tiene un extra sobre un pequeño blog, donde yo y otros operadores del proyecto publicamos reseñas sobre libros interesantes", bullet_style))
    content.append(Paragraph("• La página tiene un sistema de reseñas, donde las personas pueden dejar de 1-5 estrellas en cada libro disponible en la página", bullet_style))
    
    content.append(Paragraph("Recordatorio Importante:", subsection_style))
    content.append(Paragraph("Recuerda, puedes agregar una cantidad rica de contenido e información, no te limites, solo imagina que construirás un documento de PowerPoint que presentarás con un proyecto y código en 12 minutos, así que construye todo pensando que no puedes exceder ese tiempo.", instruction_style))
    
    content.append(Spacer(1, 20))
    
    # RESUMEN DE CRONOGRAMA DE PRESENTACIÓN
    content.append(Paragraph("Resumen Completo del Cronograma de Presentación", section_style))
    
    content.append(Paragraph("1. <b>Diapositiva de Portada/Título</b> - 30 segundos", bullet_style))
    content.append(Paragraph("   • Título del proyecto, membrete universitario, nombres de los miembros del grupo", bullet_style))
    content.append(Paragraph("   • Enfoque de diseño: Diseño limpio y bien espaciado", bullet_style))
    
    content.append(Paragraph("2. <b>Introducción</b> - 1 minuto", bullet_style))
    content.append(Paragraph("   • Qué es AngelReads y su propósito principal", bullet_style))
    content.append(Paragraph("   • Enfoque de diseño: Mensajes claros y concisos con elementos visuales", bullet_style))
    
    content.append(Paragraph("3. <b>Planteamiento del Problema</b> - 1 minuto", bullet_style))
    content.append(Paragraph("   • Desafíos actuales y solución propuesta", bullet_style))
    content.append(Paragraph("   • Enfoque de diseño: Guiar la atención hacia información clave", bullet_style))
    
    content.append(Paragraph("4. <b>Objetivos</b> - 1.5 minutos", bullet_style))
    content.append(Paragraph("   • Objetivos generales y específicos", bullet_style))
    content.append(Paragraph("   • Enfoque de diseño: Representación visual con iconos", bullet_style))
    
    content.append(Paragraph("5. <b>Presentación de la Plataforma Web</b> - 5 minutos", bullet_style))
    content.append(Paragraph("   • Demostración en vivo o capturas de pantalla de alta calidad", bullet_style))
    content.append(Paragraph("   • Características de la plataforma, stack tecnológico, referencia a GitHub", bullet_style))
    content.append(Paragraph("   • Enfoque de diseño: Regla de tercios, diseño limpio", bullet_style))
    
    content.append(Paragraph("6. <b>Conclusión</b> - 2 minutos", bullet_style))
    content.append(Paragraph("   • Resumen de logros, impacto, visión futura", bullet_style))
    content.append(Paragraph("   • Enfoque de diseño: Mensaje de cierre impactante", bullet_style))
    
    content.append(Paragraph("<b>Tiempo Total: ~11 minutos</b> (1 minuto de margen para el límite de 12 minutos)", content_style))
    
    content.append(Spacer(1, 20))
    
    # RESUMEN DE PRINCIPIOS DE DISEÑO
    content.append(Paragraph("Resumen de Principios de Diseño", section_style))
    
    content.append(Paragraph("• <b>Menos es Más:</b> Evitar sobrecarga de información en las diapositivas", bullet_style))
    content.append(Paragraph("• <b>Regla de Tercios:</b> Posicionar elementos clave en puntos de intersección", bullet_style))
    content.append(Paragraph("• <b>Espacio en Blanco:</b> Usar el espacio de respiración efectivamente", bullet_style))
    content.append(Paragraph("• <b>Jerarquía Visual:</b> Guiar la atención de la audiencia", bullet_style))
    content.append(Paragraph("• <b>Formato Consistente:</b> Mantener estilos uniformes en toda la presentación", bullet_style))
    content.append(Paragraph("• <b>Visuales de Alta Calidad:</b> Usar capturas de pantalla e iconos claros y grandes", bullet_style))
    content.append(Paragraph("• <b>Gráficos Escalables:</b> Preferir SVGs para evitar pixelación", bullet_style))
    
    content.append(Spacer(1, 20))
    
    # REFERENCIA TÉCNICA
    content.append(Paragraph("Información de Referencia Técnica", section_style))
    
    content.append(Paragraph("Repositorio GitHub: AngelTech90/TailwindCSS-Alpine.JS", subsection_style))
    content.append(Paragraph("• El repositorio demuestra habilidades técnicas en desarrollo web moderno", bullet_style))
    content.append(Paragraph("• Muestra aplicación práctica de TailwindCSS y Alpine.JS", bullet_style))
    content.append(Paragraph("• Sirve como prueba de concepto para proyectos pequeños", bullet_style))
    
    content.append(Paragraph("Estadísticas de la Plataforma:", subsection_style))
    content.append(Paragraph("• Más de 10,000 libros disponibles", bullet_style))
    content.append(Paragraph("• Más de 7,000 clientes registrados", bullet_style))
    content.append(Paragraph("• Múltiples categorías de libros y sistemas de organización", bullet_style))
    content.append(Paragraph("• Sistema integrado de blog y reseñas", bullet_style))
    
    # Construir el PDF
    doc.build(content)
    print("PDF de Parte 3 generado exitosamente: AngelReads_Parte3_Conclusion_Instrucciones.pdf")

if __name__ == "__main__":
    crear_parte3_pdf()
