from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus.flowables import ListFlowable


def generate_pdf(data):

    doc = SimpleDocTemplate("contract.pdf",pagesize=A4,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    Story = []

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    
    name_text = f"Il/La sottoscritto/a (cognome e nome): {data['name']}"
    Story.append(Paragraph(name_text, styles["Normal"]))
    Story.append(Spacer(1, 12))

    born_in_text = f"nato a: {data['dob']}"
    Story.append(Paragraph(born_in_text, styles["Normal"]))
    Story.append(Spacer(1, 12))

    citizenship_text = f"cittadinanza: {data['city']}"
    Story.append(Paragraph(citizenship_text, styles["Normal"]))
    Story.append(Spacer(1, 12))

    vat_text = f"Codice Fiscale/P.IVA: {data['vat_number']}"
    Story.append(Paragraph(vat_text, styles["Normal"]))
    Story.append(Spacer(1, 12))

    address_text = f"Residente in (indirizzo, n. civico): {data['address']}"
    Story.append(Paragraph(address_text, styles["Normal"]))
    Story.append(Spacer(1, 12))

    city_text = f"(Località̀ - CAP – Provincia): {data['city']}"
    Story.append(Paragraph(city_text, styles["Normal"]))
    Story.append(Spacer(1, 12))

    document_text = f"Documento identificativo (tipo/n.): {data['doc']}"
    Story.append(Paragraph(document_text, styles["Normal"]))
    Story.append(Spacer(1, 12))

    released_text = f"Rilasciato da: {data['released_date']}"
    Story.append(Paragraph(released_text, styles["Normal"]))
    Story.append(Spacer(1, 12))

    expiry_text = f"Scadenza: {data['released_date']}"
    Story.append(Paragraph(expiry_text, styles["Normal"]))
    Story.append(Spacer(1, 12))

    t = ListFlowable(
        [
            Paragraph("in proprio, in quanto persona fisica", styles["Normal"]),
            Paragraph(f"nella sua qualità di rappresentante di: {data['capacity_resistance']}", styles["Normal"]),
        ],
        bulletType='bullet',
        start='square'
    )
    Story.append(t)

    commerce_reg_text = f"N. iscrizione CCIAA: {data['commerce_registeration_number']}"
    Story.append(Paragraph(commerce_reg_text, styles["Normal"]))
    Story.append(Spacer(1, 12))

    office_text = f"Sede legale (Via – n. civico): {data['office_add']}"
    Story.append(Paragraph(office_text, styles["Normal"]))
    Story.append(Spacer(1, 12))

    office_town_text = f"(Località - CAP – Provincia): {data['office_town']}"
    Story.append(Paragraph(office_town_text, styles["Normal"]))
    Story.append(Spacer(1, 12))

    state_office_text = f"Stato: {data['office_state']}"
    Story.append(Paragraph(state_office_text, styles["Normal"]))
    Story.append(Spacer(1, 12))

    doc.build(Story)
    return doc
