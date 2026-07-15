from schemas.product import ProductSpec


def generate_product_markdown(product: ProductSpec):

    md = f"# {product.product_name}\n\n"

    md += "## Vision\n\n"

    md += product.vision + "\n\n"

    md += "## Problem Statement\n\n"

    md += product.problem_statement + "\n\n"

    md += "## Target Users\n"

    for item in product.target_users:
        md += f"- {item}\n"

    md += "\n## Core Features\n"

    for item in product.core_features:
        md += f"- {item}\n"

    md += "\n## MVP Scope\n"

    for item in product.mvp_scope:
        md += f"- {item}\n"

    md += "\n## Future Scope\n"

    for item in product.future_scope:
        md += f"- {item}\n"

    md += "\n## Risks\n"

    for item in product.risks:
        md += f"- {item}\n"

    md += "\n## Success Metrics\n"

    for item in product.success_metrics:
        md += f"- {item}\n"

    return md

from schemas.srs import SRS


def generate_srs_markdown(srs: SRS):

    md = f"# Software Requirements Specification\n\n"

    md += f"## Project Name\n\n{srs.project_name}\n\n"

    md += f"## Executive Summary\n\n{srs.executive_summary}\n\n"

    sections = [
        ("Functional Requirements", srs.functional_requirements),
        ("Non Functional Requirements", srs.non_functional_requirements),
        ("User Stories", srs.user_stories),
        ("Use Cases", srs.use_cases),
        ("Assumptions", srs.assumptions),
        ("Constraints", srs.constraints),
        ("Acceptance Criteria", srs.acceptance_criteria),
    ]

    for title, items in sections:
        md += f"## {title}\n"
        for item in items:
            md += f"- {item}\n"
        md += "\n"

    return md

from schemas.ui_design import UIDesign


def generate_ui_markdown(ui: UIDesign) -> str:
    """
    Convert a UIDesign object into a Markdown document.
    """

    md = "# UI / UX Design Specification\n\n"

    md += "## Design Vision\n\n"
    md += f"{ui.design_vision}\n\n"

    sections = [
        ("Color Palette", ui.color_palette),
        ("Typography", ui.typography),
        ("Screens", ui.screens),
        ("Navigation Flow", ui.navigation_flow),
        ("Components", ui.components),
        ("Responsive Design", ui.responsiveness),
        ("Accessibility", ui.accessibility),
        ("Animations", ui.animations),
    ]

    for title, items in sections:
        md += f"## {title}\n\n"

        for item in items:
            md += f"- {item}\n"

        md += "\n"

    return md

from schemas.database_design import DatabaseDesign


def generate_database_markdown(db: DatabaseDesign) -> str:

    md = "# Database Design\n\n"

    md += f"## Database Technology\n\n{db.database_type}\n\n"

    sections = [
        ("Collections", db.collections),
        ("Relationships", db.relationships),
        ("Indexes", db.indexes),
        ("Validation Rules", db.validation_rules),
        ("Mongoose Models", db.mongoose_models),
        ("API Dependencies", db.api_dependencies),
    ]

    for title, items in sections:

        md += f"## {title}\n\n"

        for item in items:
            md += f"- {item}\n"

        md += "\n"

    return md