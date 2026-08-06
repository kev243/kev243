from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
)


OUTPUT = Path("output/pdf")
OUTPUT.mkdir(parents=True, exist_ok=True)

NAVY = colors.HexColor("#17324D")
TEAL = colors.HexColor("#147D86")
DARK = colors.HexColor("#20262E")
MUTED = colors.HexColor("#4B5563")
RULE = colors.HexColor("#CCD5DD")


def styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=19, leading=21, textColor=NAVY, alignment=TA_CENTER,
            spaceAfter=2,
        ),
        "title": ParagraphStyle(
            "Title", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=11, leading=13, textColor=TEAL, alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "contact": ParagraphStyle(
            "Contact", parent=base["Normal"], fontName="Helvetica",
            fontSize=8.5, leading=10.2, textColor=MUTED, alignment=TA_CENTER,
            spaceAfter=6,
        ),
        "section": ParagraphStyle(
            "Section", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=11.5, leading=13.5, textColor=NAVY, spaceBefore=10,
            spaceAfter=4, borderWidth=0, borderPadding=0,
        ),
        "body": ParagraphStyle(
            "Body", parent=base["Normal"], fontName="Helvetica",
            fontSize=10, leading=12.8, textColor=DARK, alignment=TA_LEFT,
            spaceAfter=4,
        ),
        "role": ParagraphStyle(
            "Role", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=10.1, leading=12.2, textColor=DARK, spaceBefore=2,
            spaceAfter=3,
        ),
        "meta": ParagraphStyle(
            "Meta", parent=base["Normal"], fontName="Helvetica-Oblique",
            fontSize=9, leading=11, textColor=MUTED, spaceAfter=3,
        ),
        "bullet": ParagraphStyle(
            "Bullet", parent=base["Normal"], fontName="Helvetica",
            fontSize=9.6, leading=12.4, textColor=DARK, leftIndent=10,
            firstLineIndent=-6, bulletIndent=0, spaceAfter=2,
        ),
        "skill": ParagraphStyle(
            "Skill", parent=base["Normal"], fontName="Helvetica",
            fontSize=9.5, leading=12, textColor=DARK, spaceAfter=2.5,
        ),
        "footer": ParagraphStyle(
            "Footer", parent=base["Normal"], fontName="Helvetica",
            fontSize=7, leading=8, textColor=MUTED, alignment=TA_CENTER,
        ),
    }


def section(title, s):
    return [
        Paragraph(title.upper(), s["section"]),
        HRFlowable(width="100%", thickness=0.55, color=RULE, spaceBefore=0, spaceAfter=2),
    ]


def bullet(text, s):
    return Paragraph(f"- {text}", s["bullet"])


def common_header(s, title):
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
    ]


def english_story(s):
    story = common_header(s, "FULL-STACK TYPESCRIPT DEVELOPER | WEB, MOBILE AND SAAS")
    story += section("Professional Summary", s)
    story += [Paragraph(
        "Computer Science graduate and Full-Stack TypeScript Developer building Urlbeo, a SaaS link-in-bio platform. "
        "Hands-on experience across Next.js and React frontends, NestJS REST APIs, PostgreSQL databases, React Native mobile development, cloud deployment and CI/CD. "
        "Known for structured problem-solving, rapid learning and dependable collaboration. Seeking a software developer role in Canada.",
        s["body"],
    )]

    story += section("Technical Skills", s)
    skills = [
        "<b>Languages:</b> TypeScript, JavaScript, SQL, Swift",
        "<b>Frontend and Mobile:</b> Next.js, React, React Native, Expo, Tailwind CSS, shadcn/ui, SwiftUI",
        "<b>Backend and Data:</b> NestJS, Node.js, REST APIs, PostgreSQL, Prisma ORM, Neon",
        "<b>Cloud and DevOps:</b> GitHub Actions, Docker, Vercel, Render, Railway, Heroku, Cloudflare, Git",
        "<b>Services and Tools:</b> Clerk, Stripe, Lemon Squeezy, Veriff KYC, Cloudinary, Postman, Jira, Figma",
        "<b>AI-Assisted Development:</b> Codex for codebase analysis, implementation and testing; GitHub Copilot for contextual suggestions; CodeRabbit for pull request reviews, while retaining ownership of technical decisions and final code validation.",
    ]
    story += [Paragraph(x, s["skill"]) for x in skills]

    story += section("Selected Project", s)
    project = [
        Paragraph("URLBEO - Full-Stack SaaS Platform", s["role"]),
        Paragraph(
            '<link href="https://www.urlbeo.com/" color="#147D86">urlbeo.com</link> | '
            '<link href="https://github.com/kev243/urlbeo-public-nextjs" color="#147D86">Landing Page Source Code</link> | '
            '<link href="https://github.com/kev243/urlbeo-backend-nestjs" color="#147D86">Backend Source Code</link>',
            s["meta"],
        ),
        bullet("Designed a modular NestJS REST API with Prisma and PostgreSQL for authentication, user profiles, link management, validation and an analytics foundation.", s),
        bullet("Built a responsive, SEO-focused landing page with Next.js, React, TypeScript and Tailwind CSS using reusable components and a production-oriented architecture.", s),
        bullet("Developing the mobile application with React Native, Expo and TypeScript for profile management, link management, live preview and analytics.", s),
        bullet("Implemented CI/CD workflows with GitHub Actions and worked with cloud deployment, authentication, payments, media and identity-verification services.", s),
    ]
    story += [KeepTogether(project)]

    story += section("Professional Experience", s)
    experience = [
        Paragraph("MERCHANDISER | Pepsi - Alex Coulombe", s["role"]),
        Paragraph("Trois-Rivieres, Quebec | January 2023 - Present", s["meta"]),
        bullet("Coordinate priorities across multiple retail locations while meeting quality standards and operational deadlines in a fast-paced environment.", s),
        bullet("Resolve unexpected field issues, maintain clear client communication and collaborate with cross-functional teams to ensure product availability.", s),
    ]
    story += [KeepTogether(experience)]

    story += section("Education and Certifications", s)
    story += [
        Paragraph("<b>Bachelor of Computer Science</b> | Université du Québec à Trois-Rivières (UQTR) | March 2026", s["body"]),
        Paragraph("<b>Preparatory Program</b> | EIGSI Engineering School, Morocco | December 2019", s["body"]),
        Paragraph("<b>Training:</b> Cisco Introduction to Cybersecurity | Cisco Linux Unhatched | Microsoft Learn Azure Fundamentals (AZ-900)", s["body"]),
    ]

    story += section("Languages", s)
    story += [Paragraph("French: Native | English: Basic proficiency", s["body"])]
    return story


def french_story(s):
    story = common_header(s, "DÉVELOPPEUR FULL-STACK TYPESCRIPT | WEB, MOBILE ET SAAS")
    story += section("Profil professionnel", s)
    story += [Paragraph(
        "Diplômé d'un baccalauréat en informatique et développeur Full-Stack TypeScript, je développe Urlbeo, une plateforme SaaS de type link-in-bio. "
        "Expérience pratique en interfaces Next.js et React, API REST NestJS, bases de données PostgreSQL, développement mobile React Native, déploiement cloud et CI/CD. "
        "Reconnu pour ma résolution structurée de problèmes, ma capacité d'apprentissage et ma collaboration fiable. À la recherche d'un poste de développeur logiciel au Canada.",
        s["body"],
    )]

    story += section("Compétences techniques", s)
    skills = [
        "<b>Langages :</b> TypeScript, JavaScript, SQL, Swift",
        "<b>Frontend et mobile :</b> Next.js, React, React Native, Expo, Tailwind CSS, shadcn/ui, SwiftUI",
        "<b>Backend et données :</b> NestJS, Node.js, API REST, PostgreSQL, Prisma ORM, Neon",
        "<b>Cloud et DevOps :</b> GitHub Actions, Docker, Vercel, Render, Railway, Heroku, Cloudflare, Git",
        "<b>Services et outils :</b> Clerk, Stripe, Lemon Squeezy, Veriff KYC, Cloudinary, Postman, Jira, Figma",
        "<b>Développement assisté par IA :</b> Codex pour l'analyse, l'implémentation et les tests; GitHub Copilot pour les suggestions contextuelles; CodeRabbit pour la revue des pull requests, tout en conservant la responsabilité des décisions techniques et de la validation finale du code.",
    ]
    story += [Paragraph(x, s["skill"]) for x in skills]

    story += section("Projet sélectionné", s)
    project = [
        Paragraph("URLBEO - Plateforme SaaS Full-Stack", s["role"]),
        Paragraph(
            '<link href="https://www.urlbeo.com/" color="#147D86">urlbeo.com</link> | '
            '<link href="https://github.com/kev243/urlbeo-public-nextjs" color="#147D86">Code source de la landing page</link> | '
            '<link href="https://github.com/kev243/urlbeo-backend-nestjs" color="#147D86">Code source du backend</link>',
            s["meta"],
        ),
        bullet("Conception d'une API REST modulaire avec NestJS, Prisma et PostgreSQL pour l'authentification, les profils, la gestion des liens, la validation et une base analytique.", s),
        bullet("Développement d'une landing page responsive et optimisée pour le SEO avec Next.js, React, TypeScript et Tailwind CSS, fondée sur des composants réutilisables.", s),
        bullet("Développement en cours de l'application mobile avec React Native, Expo et TypeScript pour la gestion des profils et liens, l'aperçu en direct et les statistiques.", s),
        bullet("Mise en place de flux CI/CD avec GitHub Actions et utilisation de services de déploiement cloud, d'authentification, de paiement, de médias et de vérification d'identité.", s),
    ]
    story += [KeepTogether(project)]

    story += section("Expérience professionnelle", s)
    experience = [
        Paragraph("MARCHANDISEUR | Pepsi - Alex Coulombe", s["role"]),
        Paragraph("Trois-Rivières, Québec | Janvier 2023 - Aujourd'hui", s["meta"]),
        bullet("Coordonner les priorités dans plusieurs commerces tout en respectant les normes de qualité et les échéances dans un environnement dynamique.", s),
        bullet("Résoudre les imprévus sur le terrain, maintenir une communication claire avec les clients et collaborer avec plusieurs équipes pour assurer la disponibilité des produits.", s),
    ]
    story += [KeepTogether(experience)]

    story += section("Formation et certifications", s)
    story += [
        Paragraph("<b>Baccalauréat en informatique</b> | Université du Québec à Trois-Rivières (UQTR) | Mars 2026", s["body"]),
        Paragraph("<b>Classe préparatoire</b> | École d'ingénieurs généralistes EIGSI, Maroc | Décembre 2019", s["body"]),
        Paragraph("<b>Formations :</b> Cisco Introduction à la cybersécurité | Cisco Linux Unhatched | Microsoft Learn Azure Fundamentals (AZ-900)", s["body"]),
    ]

    story += section("Langues", s)
    story += [Paragraph("Français : langue maternelle | Anglais : niveau débutant", s["body"])]
    return story


def build(filename, story):
    path = OUTPUT / filename
    doc = BaseDocTemplate(
        str(path), pagesize=letter,
        leftMargin=0.55 * inch, rightMargin=0.55 * inch,
        topMargin=0.42 * inch, bottomMargin=0.4 * inch,
        title="Kevin Nimi - Resume",
        author="Kevin Nimi",
        subject="Full-Stack TypeScript Developer Resume",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates(PageTemplate(id="resume", frames=[frame]))
    doc.build(story)
    return path


if __name__ == "__main__":
    s = styles()
    print(build("Kevin-Nimi-Resume-English.pdf", english_story(s)))
    print(build("Kevin-Nimi-CV-Francais.pdf", french_story(s)))
