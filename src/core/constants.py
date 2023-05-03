import os



BOOTSTRAP_PATHS = [
    {
        "url_path": "dist/css/bootstrap.min.css",
        "output_path": os.path.join("css", "bootstrap.min.css"),
    },
    {
        "url_path": "dist/css/bootstrap.min.css.map",
        "output_path": os.path.join("css", "bootstrap.min.css.map"),
    },
    {
        "url_path": "dist/js/bootstrap.min.js",
        "output_path": os.path.join("js", "bootstrap.min.js"),
    },
    {
        "url_path": "dist/js/bootstrap.min.js.map",
        "output_path": os.path.join("js", "bootstrap.min.js.map"),
    },
]


PRELINE_PATHS = [
    {
        "url_path": "dist/preline.js",
        "output_path": os.path.join("js", "preline.min.js")
    }
]


HTMX_PATHS = [
    {
        "url_path": "dist/htmx.min.js",
        "output_path": os.path.join("js", "htmx.min.js")
    }
]

APLINE_PATHS = [
    {
        "url_path": "dist/cdn.min.js",
        "output_path": os.path.join("js", "alpine.min.js")        
    }
]