from models.Printer import  Printer
from models.InkjetPrinter import  InkjetPrinter
from models.LaserPrinter  import  LaserPrinter
from models.PhotoPrinter  import  PhotoPrinter 
from models.ThreeDPrinter  import ThreeDPrinter

class PrinterManager:

	def __init__(self):
	    """
	    Initializes the PrinterManager object.

	    Attributes:
	    printers (list): A list of printers, initially empty.
	    """
	    self.printers = []

	def add_printer(self, printer):
	    """
	    Add a printer to the manager.

	    Args:
		printer (Printer): The printer to be added.

	    """
	    self.printers.append(printer)

	def find_printer_with_type(self, type):
	    """
	    Find printers of a specific type.

	    Args:
		type (str): The type of printers to find.

	    Returns:
		   list: A list of printers matching the specified type.

	    """
	    filtered_printers = list(filter(lambda printer : printer.pr_type==type, self.printers))
	    return filtered_printers

	def find_printer_with_more_paper_than(self, paper_count):
	    """
	    Find printers with more paper than a given count.

	    Args:
		paper_count (int): The minimum paper count to filter printers.
 
	    Returns:
		   list: A list of printers with more paper than the specified count.

	    """
	    filtered_printers = list(filter(lambda printer : printer.paper_count>paper_count, self.printers))
	    return filtered_printers
