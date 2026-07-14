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