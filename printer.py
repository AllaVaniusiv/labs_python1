class Printer:
    default_printer = None

    def __init__(self, model='', pr_type='', is_color=False, is_duplex=False, paper_tray_capacity=0, paper_count=0):
        self._model = model
        self._pr_type = pr_type
        self._is_color = is_color
        self._is_duplex = is_duplex
        self._paper_tray_capacity = paper_tray_capacity
        self._paper_count = paper_count
        
    def __str__(self):
        return f"Model: {self._model}\nPr Type: {self._pr_type}\nColor: {self._is_color}\nDuplex: {self._is_duplex}\nPaper Tray Capacity: {self._paper_tray_capacity}\nPaper Count: {self._paper_count}"

    def __repr__(self):
        return f"Printer(model='{self._model}', pr_type='{self._pr_type}', is_color={self._is_color}, is_duplex={self._is_duplex}, paper_tray_capacity={self._paper_tray_capacity}, paper_count={self._paper_count})"

    @property
    def printer_model(self):
        return self._model

    @printer_model.setter
    def printer_model(self, new_model):
        self._model = new_model

    @property
    def printer_pr_type(self):
        return self._pr_type

    @printer_pr_type.setter
    def printer_pr_type(self, new_pr_type):
        self._pr_type = new_pr_type

    @property
    def printer_is_color(self):
        return self.is_color

    @printer_is_color.setter
    def printer_is_color(self, new_is_color):
        self._is_color = new_is_color

    @property
    def printer_is_duplex(self):
        return self._is_duplex

    @printer_is_duplex.setter
    def printer_is_duplex(self, new_is_duplex):
        self._is_duplex = new_is_duplex

    @property
    def printer_paper_tray_capacity(self):
        return self._paper_tray_capacity

    @printer_paper_tray_capacity.setter
    def printer_paper_tray_capacity(self, new_paper_tray_capacity):
        self._paper_tray_capacity = new_paper_tray_capacity

    @property
    def printer_paper_count(self):
        return self._paper_count

    @printer_paper_count.setter
    def printer_paper_count(self, new_paper_count):
        self._paper_count = new_paper_count

    @staticmethod
    def get_instance(cls):
        if cls.default_printer is None:
            cls.default_printer = Printer()
        return cls.default_printer
    
    @classmethod
    def print_pages(self, pages):
        if pages <= self.paper_count:
            self.paper_count -= pages
            print(f"Printing {pages} pages...")
        else:
            print("Not enough paper in the tray!")

    def load_paper(self, count):
        self.paper_count += count
        if self.paper_count > self.paper_tray_capacity:
            self.paper_count = self.paper_tray_capacity

    


