class BasePage:
    def __init__(self, page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")

    def goto(self, path: str = ""):
        if path.startswith("https"):
            self.page.goto(path)
            return
        normalized_path = path if path.startswith("/") else f"/{path}" if path else ""
        self.page.goto(f"{self.base_url}{normalized_path}")
