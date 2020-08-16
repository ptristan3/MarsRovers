import sys,os
sys.path.append(os.path.realpath('.'))
import logging
from parser_input import parse_input_model_file
from tkinter import Tk, Canvas, Frame, BOTH 
from rover import Rover
from position import Position
from plateau import Plateau
from mars_plateau import Grid_Window

logging.basicConfig(filename='marsRovers.log', level=logging.INFO, format='%(asctime)s %(message)s')
logging.info('Mars rover start')

input_model_file= sys.argv[1]

if len(input_model_file) > 0:
  try:
    mars=parse_input_model_file(input_model_file)

    raiz=Tk()
    raiz.resizable(True, False)
    raiz.title('Rovers in Mars Plateau')

    myapp = Grid_Window(raiz)
    myapp.draw_grid(mars.width+1, mars.height+1)
  
    logging.info(mars.print_position_rovers())

    for rover in mars.rovers:
      myapp.draw_rover(rover.position.x, rover.position.y, mars.height+1, rover.id_number, rover.position.cardinal, 'Inicial')
    
    mars.run()

    print("Final Position")
    mars.print_position_rovers()

    for rover in mars.rovers:
      myapp.draw_rover(rover.position.x, rover.position.y, mars.height+1, rover.id_number, rover.position.cardinal, 'Final')

    raiz.mainloop()
  except Exception:
    print("No se ha podido iniciar el plateau")