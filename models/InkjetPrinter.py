from models.Printer import  Printer
class InkjetPrinter(Printer):
    """
    A class inheriting from the Printer class.
    """

    REQUIRED_COLOUR_PER_PAGE = 5
 
    def __init__(self, model, pr_type, is_color, is_duplex, paper_tray_capacity, paper_count, cyan_ink_type, cyan_ink_level, magenta_ink_type, magenta_ink_level, yellow_ink_type, yellow_ink_level, black_ink_type, black_ink_level):
        """
        Initialize an InkjetPrinter object.

        Args:
            model (str): The model of the inkjet printer.
            pr_type (str): The type of the inkjet printer.
            is_color (bool): True if the inkjet printer supports color printing, False otherwise.
            is_duplex (bool): True if the inkjet printer supports duplex printing, False otherwise.
            paper_tray_capacity (int): The capacity of the paper tray.
            paper_count (int): The current count of paper in the tray.
            cyan_ink_type (str): The type of cyan ink used in the printer.
            cyan_ink_level (float): The current level of cyan ink in the printer.
            magenta_ink_type (str): The type of magenta ink used in the printer.
            magenta_ink_level (float): The current level of magenta ink in the printer.
            yellow_ink_type (str): The type of yellow ink used in the printer.
            yellow_ink_level (float): The current level of yellow ink in the printer.
            black_ink_type (str): The type of black ink used in the printer.
            black_ink_level (float): The current level of black ink in the printer.
        """
        super().__init__(model, pr_type, is_color, is_duplex, paper_tray_capacity, paper_count)
        self.cyan_ink_type = cyan_ink_type
        self.cyan_ink_level = cyan_ink_level
        self.magenta_ink_type = magenta_ink_type
        self.magenta_ink_level = magenta_ink_level
        self.yellow_ink_type = yellow_ink_type
        self.yellow_ink_level = yellow_ink_level
        self.black_ink_type = black_ink_type
        self.black_ink_level = black_ink_level

    def __str__(self):
        """Returns a string that represents the object in a readable format."""
        return f"InkjetPrinter: model={self.model}, pr type={self.pr_type}, color={self.is_color}, duplex={self.is_duplex}, paper tray capacity={self.paper_tray_capacity}, paper count={self.paper_count}, cyan_ink_type={self.cyan_ink_type}, cyan_ink_level={self.cyan_ink_level}, magenta_ink_type={self.magenta_ink_type}, magenta_ink_level={self.magenta_ink_level}, yellow_ink_type={self.yellow_ink_type}, yellow_ink_level={self.yellow_ink_level}, black_ink_type={self.black_ink_type}, black_ink_level={self.black_ink_level}"

    def __repr__(self):
        """Returns a string that is a valid Python expression for reproducing the object."""
        return f"InkjetPrinter(model={self.model}, pr type={self.pr_type}, color={self.is_color}, duplex={self.is_duplex}, paper tray capacity={self.paper_tray_capacity}, paper count={self.paper_count}, cyan_ink_type={self.cyan_ink_type}, cyan_ink_level={self.cyan_ink_level}, magenta_ink_type={self.magenta_ink_type}, magenta_ink_level={self.magenta_ink_level}, yellow_ink_type={self.yellow_ink_type}, yellow_ink_level={self.yellow_ink_level}, black_ink_type={self.black_ink_type}, black_ink_level={self.black_ink_level})"
   
    def getRemainingPagesCount(self):
        """
        Calculate and return the maximum number of pages that can be printed based on the remaining ink levels.

        Returns:
            int: The maximum number of pages that can be printed.
        """
        remainingCyanPages = int(self.cyan_ink_level / REQUIRED_COLOUR_PER_PAGE)
        remainingMagentaPages = int(self.magenta_ink_level / REQUIRED_COLOUR_PER_PAGE)
        remainingYellowPages = int(self.yellow_ink_level / REQUIRED_COLOUR_PER_PAGE)
        remainingBlackPages = int(self.black_ink_level / REQUIRED_COLOUR_PER_PAGE)
        return min(remainingCyanPages, remainingMagentaPages, remainingYellowPages, remainingBlackPages)


    


