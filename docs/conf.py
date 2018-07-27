from datetime import datetime


extensions = []
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

project = u"poliastro"
year = datetime.now().year
copyright = u"%d Juan Luis Cano and poliastro development team" % year

exclude_patterns = ["_build"]

html_theme = "alabaster"
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        "donate.html",
    ]
}
html_theme_options = {
    "description": "Astrodynamics in Python",
    "github_user": "poliastro",
    "github_repo": "poliastro",
    "fixed_sidebar": True,
}
