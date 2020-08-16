from tkinter import Tk, Canvas, Frame, BOTH
from src.mars_plateau import Grid_Window
from src.plateau import Plateau
from src.position import Position
from src.rover import Rover
from src.parser_input import parse_input_model_file
import logging
import sys
import os
sys.path.append(os.path.realpath('.'))

logging.basicConfig(filename='marsRovers.log',
                    level=logging.INFO, format='%(asctime)s %(message)s')
logging.info('Mars rover start')

if (len(sys.argv) is 1):
  print ("*********************************************************************")
  print ("                       The basic use of Mars Rovers                  ")
  print ("*********************************************************************")  
  print ()
  print ("FLAG -f inputFileName => This file contains the Mars Rover experience")
  print ("   Example ../somelocalpath/MarsRovers/$ python3 -f input.txt        ")
  print ()
  print ("OPTIONAL FLAG -g         => If you want display a graphic out     ")
  print ("   Example ../somelocalpath/MarsRovers/$ python3 -f input.txt -g     ")
  print ()
  print ("**********************************************************************")
  print ()
  print ("After running it, you can analyze the traceability of rovers into the ")
  print ("plateau just by looking at the file 'marsRovers.log'                  ")
  print ()
  print ("**********************************************************************")
  

elif (len(sys.argv) is 3):
  if sys.argv[1] == '-f':
    try: 
      mars = parse_input_model_file(sys.argv[2])
      print('The Inicial Position')
      mars.print_position_rovers()
       
      mars.run()
       
      print("The Final Position")
      mars.print_position_rovers()
    except Exception:
      logging.info("The Plateau can't be created! Check the input.")
      print("Im sorry! something's wrong. Check the input")

elif (len(sys.argv) is 4):   
  if sys.argv[1] == '-f' and sys.argv[3] == '-g':
    try:
        mars = parse_input_model_file(sys.argv[2])

        raiz = Tk()
        raiz.resizable(True, False)
        raiz.title('Rovers in Mars Plateau')

        myapp = Grid_Window(raiz)
        myapp.draw_grid(mars.width+1, mars.height+1)

        for rover in mars.rovers:
            myapp.draw_rover(rover.position.x, rover.position.y, mars.height+1,
                             rover.id_number, rover.position.cardinal, 'Inicial')

        mars.run()

        for rover in mars.rovers:
            myapp.draw_rover(rover.position.x, rover.position.y, mars.height+1,
                             rover.id_number, rover.position.cardinal, 'Final')

        raiz.mainloop()
    except Exception:
        logging.info("The Plateau can't be created! Check the input.")
        print("Im sorry! something's wrong. Check the input")