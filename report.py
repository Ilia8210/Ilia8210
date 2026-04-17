import os
from datetime import datetime
from fpdf import FPDF

FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")

SEVERITY_COLORS = {
    "critical": (220, 50, 47),
    "high": (203, 75, 22),
    "medium": (181, 137, 0),
    "low": (38, 139, 210),
}


class UXReport(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("DejaVu", "", os.path.join(FONT_DIR, "DejaVuSans.ttf"))
        self.add_font("DejaVu", "B", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"))
        self.set_auto_page_break(auto=True, margin=20)
        self.set_margins(20, 20, 20)

    def header(self):
        if self.page_no() > 1:
            self.set_font("DejaVu", "", 8)
            self.set_text_color(180, 180, 180)
            self.cell(0, 8, "UX Feedback Report", align="R", new_x="LMARGIN", new_y="NEXT")

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "", 8)
        self.set_text_color(180, 180, 180)
        self.cell(0, 8, str(self.page_no()), align="C")

    def h1(self, text):
        self.set_font("DejaVu", "B", 22)
        self.set_text_color(20, 20, 20)
        self.multi_cell(0, 12, text)

    def h2(self, text):
        self.ln(4)
        self.set_font("DejaVu", "B", 13)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 8, text)
        self.ln(2)

    def body(self, text, color=(60, 60, 60)):
        self.set_font("DejaVu", "", 10)
        self.set_text_color(*color)
        self.multi_cell(0, 6, text)

    def small(self, text, color=(120, 120, 120)):
        self.set_font("DejaVu", "", 8)
        self.set_text_color(*color)
        self.multi_cell(0, 5, text)

    def divider(self):
        self.ln(3)
        self.set_draw_color(220, 220, 220)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)


def generate_report(analysis: dict, output_path: str = "report.pdf") -> str:
    pdf = UXReport()
    pdf.add_page()

    pdf.h1("UX Feedback Analysis")
    pdf.set_font("DejaVu", "", 11)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 7, datetime.now().strftime("%B %d, %Y"), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    stats = (
        f"Messages: {analysis.get('total_messages', 0)}   |   "
        f"Screenshots: {analysis.get('total_images', 0)}   |   "
        f"Issues found: {len(analysis.get('issues', []))}"
    )
    pdf.set_font("DejaVu", "", 9)
    pdf.set_text_color(100, 100, 100)
    pdf.set_fill_color(245, 245, 245)
    pdf.multi_cell(0, 8, stats, fill=True, align="C")
    pdf.ln(6)

    if analysis.get("executive_summary"):
        pdf.h2("Executive Summary")
        pdf.body(analysis["executive_summary"])

    issues = analysis.get("issues", [])
    if issues:
        pdf.h2(f"Issues ({len(issues)})")
        for i, issue in enumerate(issues, 1):
            severity = issue.get("severity", "medium")
            color = SEVERITY_COLORS.get(severity, (80, 80, 80))

            pdf.divider()

            pdf.set_font("DejaVu", "B", 11)
            pdf.set_text_color(*color)
            pdf.multi_cell(0, 7, f"{i}. {issue.get('title', '')}")

            freq = issue.get("frequency", 0)
            ux = issue.get("ux_principle", "")
            pdf.small(f"Mentioned {freq}x   |   {severity.upper()}   |   {ux}")

            if issue.get("description"):
                pdf.body(issue["description"])

            for q in issue.get("quotes", [])[:2]:
                pdf.ln(1)
                pdf.set_font("DejaVu", "", 9)
                pdf.set_text_color(110, 110, 110)
                pdf.multi_cell(0, 5, f'"{q}"')

            if issue.get("ux_explanation"):
                pdf.ln(1)
                pdf.small(f"UX insight: {issue['ux_explanation']}", color=(120, 90, 170))

            if issue.get("recommendation"):
                pdf.ln(2)
                pdf.set_font("DejaVu", "B", 9)
                pdf.set_text_color(0, 120, 0)
                pdf.cell(32, 5, "Recommendation:", new_x="END", new_y="TOP")
                pdf.set_font("DejaVu", "", 9)
                pdf.set_text_color(60, 60, 60)
                pdf.multi_cell(0, 5, issue["recommendation"])

            pdf.ln(2)

    quick_wins = analysis.get("quick_wins", [])
    if quick_wins:
        pdf.h2("Quick Wins")
        for qw in quick_wins:
            pdf.set_font("DejaVu", "", 10)
            pdf.set_text_color(60, 60, 60)
            pdf.cell(8, 6, "-", new_x="END", new_y="TOP")
            pdf.multi_cell(0, 6, qw)
        pdf.ln(4)

    if analysis.get("screenshots_insights"):
        pdf.h2("Screenshots Insights")
        pdf.body(analysis["screenshots_insights"])

    if analysis.get("positive_feedback"):
        pdf.h2("What Users Like")
        pdf.body(analysis["positive_feedback"])

    pdf.output(output_path)
    return output_path
