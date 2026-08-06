from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import BaseDocTemplate, Frame, HRFlowable, PageTemplate, Paragraph, Spacer


OUTPUT = Path("output/pdf")
OUTPUT.mkdir(parents=True, exist_ok=True)

NAVY = colors.HexColor("#17324D")
TEAL = colors.HexColor("#147D86")
DARK = colors.HexColor("#20262E")
MUTED = colors.HexColor("#4B5563")
RULE = colors.HexColor("#CCD5DD")


def make_styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=20, leading=23, textColor=NAVY, alignment=TA_CENTER,
            spaceAfter=3,
        ),
        "title": ParagraphStyle(
            "Title", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=10.5, leading=13, textColor=TEAL, alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "contact": ParagraphStyle(
            "Contact", parent=base["Normal"], fontName="Helvetica",
            fontSize=8.5, leading=10.5, textColor=MUTED, alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "date": ParagraphStyle(
            "Date", parent=base["Normal"], fontName="Helvetica",
            fontSize=10, leading=13, textColor=DARK, alignment=TA_LEFT,
            spaceAfter=10,
        ),
        "recipient": ParagraphStyle(
            "Recipient", parent=base["Normal"], fontName="Helvetica",
            fontSize=10, leading=13, textColor=DARK, alignment=TA_LEFT,
            spaceAfter=12,
        ),
        "subject": ParagraphStyle(
            "Subject", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=10.5, leading=13, textColor=NAVY, alignment=TA_LEFT,
            spaceAfter=13,
        ),
        "body": ParagraphStyle(
            "Body", parent=base["Normal"], fontName="Helvetica",
            fontSize=10.2, leading=14.4, textColor=DARK, alignment=TA_LEFT,
            spaceAfter=11,
        ),
        "closing": ParagraphStyle(
            "Closing", parent=base["Normal"], fontName="Helvetica",
            fontSize=10.2, leading=14.4, textColor=DARK, alignment=TA_LEFT,
            spaceBefore=2, spaceAfter=4,
        ),
        "signature": ParagraphStyle(
            "Signature", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=10.5, leading=14, textColor=NAVY, alignment=TA_LEFT,
        ),
    }


def header(s, title):
    return [
        Paragraph("Kevin Nimi", s["name"]),
        Paragraph(title, s["title"]),
        Paragraph(
            "Trois-Rivieres, Quebec | (819) 244-8382 | "
            '<link href="mailto:k.nimi73@gmail.com" color="#4B5563">k.nimi73@gmail.com</link> | '
            '<link href="https://github.com/kev243" color="#4B5563">github.com/kev243</link> | '
            '<link href="https://www.linkedin.com/in/kevin-nimi/" color="#4B5563">linkedin.com/in/kevin-nimi</link>',
            s["contact"],
        ),
        HRFlowable(width="100%", thickness=0.7, color=RULE, spaceBefore=0, spaceAfter=15),
    ]


def english_story(s):
    story = header(s, "FULL-STACK TYPESCRIPT DEVELOPER | WEB, MOBILE AND SAAS")
    story += [
        Paragraph("August 4, 2026", s["date"]),
        Paragraph("Hiring Manager<br/>Software Development Team", s["recipient"]),
        Paragraph("RE: APPLICATION FOR A FULL-STACK TYPESCRIPT DEVELOPER POSITION", s["subject"]),
        Paragraph("Dear Hiring Manager,", s["body"]),
        Paragraph(
            "I am writing to express my interest in a software development opportunity within your organization. "
            "As a Computer Science graduate from the Université du Québec à Trois-Rivières and a Full-Stack TypeScript Developer, "
            "I am motivated to contribute to a collaborative team building reliable web, mobile and SaaS products.",
            s["body"],
        ),
        Paragraph(
            "My main project, Urlbeo, has allowed me to work across an entire product ecosystem. I designed a modular REST API using NestJS, Prisma and PostgreSQL, "
            "built a responsive and SEO-focused landing page with Next.js, React, TypeScript and Tailwind CSS, and am developing a mobile application with React Native and Expo. "
            "I also use GitHub Actions for CI/CD and work with cloud, authentication, payment, media and identity-verification services.",
            s["body"],
        ),
        Paragraph(
            "I use Codex, GitHub Copilot and CodeRabbit to accelerate analysis, implementation, testing and code review while retaining full responsibility for technical decisions and final code validation. "
            "This workflow supports my productivity without replacing the engineering judgment, verification and attention to maintainability required for production-quality software.",
            s["body"],
        ),
        Paragraph(
            "My current experience at Pepsi - Alex Coulombe has strengthened skills that transfer directly to software teams: prioritizing work in a fast-paced environment, solving unexpected problems, "
            "communicating clearly with clients and collaborating reliably across teams. I learn quickly, accept feedback constructively and approach problems with curiosity, discipline and persistence.",
            s["body"],
        ),
        Paragraph(
            "I would welcome the opportunity to discuss how my technical foundation, product-building experience and motivation to grow could contribute to your team. "
            "Thank you for considering my application.",
            s["body"],
        ),
        Paragraph("Sincerely,", s["closing"]),
        Paragraph("Kevin Nimi", s["signature"]),
    ]
    return story


def french_story(s):
    story = header(s, "DÉVELOPPEUR FULL-STACK TYPESCRIPT | WEB, MOBILE ET SAAS")
    story += [
        Paragraph("Le 4 août 2026", s["date"]),
        Paragraph("À l'attention de la personne responsable du recrutement<br/>Équipe de développement logiciel", s["recipient"]),
        Paragraph("OBJET : CANDIDATURE À UN POSTE DE DÉVELOPPEUR FULL-STACK TYPESCRIPT", s["subject"]),
        Paragraph("Madame, Monsieur,", s["body"]),
        Paragraph(
            "Je souhaite vous présenter ma candidature pour une occasion en développement logiciel au sein de votre organisation. "
            "Diplômé d'un baccalauréat en informatique de l'Université du Québec à Trois-Rivières et développeur Full-Stack TypeScript, "
            "je suis motivé à contribuer à une équipe collaborative qui conçoit des produits web, mobiles et SaaS fiables.",
            s["body"],
        ),
        Paragraph(
            "Mon principal projet, Urlbeo, m'a permis d'intervenir sur l'ensemble d'un écosystème produit. J'ai conçu une API REST modulaire avec NestJS, Prisma et PostgreSQL, "
            "développé une landing page responsive et optimisée pour le SEO avec Next.js, React, TypeScript et Tailwind CSS, et je développe actuellement une application mobile avec React Native et Expo. "
            "J'utilise également GitHub Actions pour le CI/CD ainsi que différents services de cloud, d'authentification, de paiement, de médias et de vérification d'identité.",
            s["body"],
        ),
        Paragraph(
            "J'utilise Codex, GitHub Copilot et CodeRabbit pour accélérer l'analyse, l'implémentation, les tests et la revue de code, tout en conservant l'entière responsabilité des décisions techniques et de la validation finale. "
            "Cette méthode améliore ma productivité sans remplacer le jugement d'ingénierie, les vérifications et l'attention portée à la maintenabilité d'un logiciel de qualité.",
            s["body"],
        ),
        Paragraph(
            "Mon expérience actuelle chez Pepsi - Alex Coulombe m'a permis de renforcer des compétences directement transférables à une équipe logicielle : organiser les priorités dans un environnement dynamique, "
            "résoudre les imprévus, communiquer clairement avec les clients et collaborer de manière fiable avec plusieurs équipes. J'apprends rapidement, j'accueille les commentaires de façon constructive et j'aborde les problèmes avec curiosité, rigueur et persévérance.",
            s["body"],
        ),
        Paragraph(
            "Je serais heureux d'échanger avec vous afin de discuter de la contribution que ma base technique, mon expérience de développement de produit et ma motivation à progresser pourraient apporter à votre équipe. "
            "Je vous remercie de l'attention portée à ma candidature.",
            s["body"],
        ),
        Paragraph("Veuillez agréer, Madame, Monsieur, mes salutations distinguées.", s["closing"]),
        Paragraph("Kevin Nimi", s["signature"]),
    ]
    return story


def build(filename, story, title, subject):
    path = OUTPUT / filename
    doc = BaseDocTemplate(
        str(path), pagesize=letter,
        leftMargin=0.72 * inch, rightMargin=0.72 * inch,
        topMargin=0.5 * inch, bottomMargin=0.55 * inch,
        title=title, author="Kevin Nimi", subject=subject,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates(PageTemplate(id="letter", frames=[frame]))
    doc.build(story)
    return path


if __name__ == "__main__":
    styles = make_styles()
    print(build(
        "Kevin-Nimi-Cover-Letter-English.pdf",
        english_story(styles),
        "Kevin Nimi - Cover Letter",
        "Application for a Full-Stack TypeScript Developer Position",
    ))
    print(build(
        "Kevin-Nimi-Lettre-Presentation-Motivation.pdf",
        french_story(styles),
        "Kevin Nimi - Lettre de présentation et de motivation",
        "Candidature à un poste de développeur Full-Stack TypeScript",
    ))
