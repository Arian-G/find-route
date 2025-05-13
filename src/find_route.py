import sys
import argparse

class Node:
    def __init__(self, name): 
        self.name = name
        self.parent_node = None
        self.depth = 0
        self.total_cost = 0.0
        self.successors = {}
        self.heuristic = 0.0
    
    def set_successors(self, successor, successor_cost):
        self.successors[successor] = successor_cost

def main(args):
    routes, start_state, goal_state, heuristic = process_input(args)

def process_input(args):
    parser = argparse.ArgumentParser \
    (
        add_help = False, 
        usage = "%(prog)s input origin destination [heuristic]"
    )
    parser.add_argument("program_name")
    parser.add_argument("input", help = ".txt filename containing the route")
    parser.add_argument("origin", help = "Origin name")
    parser.add_argument("destination", help = "Destination name")
    parser.add_argument("heuristic", nargs = "?", help = "Optional .txt filename containing the heuristic")
    args = parser.parse_args(args)

    routes = []

    # Handle the input file.
    try:
        filename = open(args.input, "r")
    except IOError:
        print \
        (
            "\n" + str(args.input) + " file not found" +
            "\nEnsure the input file is in the same folder as the python file"
        )
        exit()

    for line in filename:
        if "END OF INPUT" in line:
            break
        items = line.split()
        # Create two entries (since input is bi-directional) with  
        # their successor information and add them to a list.
        #     Node( Name,    Successor,   Cost )
        #     Node( Lubeck,  Hamburg,     63   )
        #     Node( Hamburg, Lubeck,      63   )
        routes.append((items[1], items[0], float(items[2])))
        routes.append((items[0], items[1], float(items[2])))

    routes.sort()
    start_state = args.origin
    goal_state  = args.destination

    # Handle the heuristic file.
    if args.heuristic != None:
        heuristic = []
        try:
            heuristic_filename = open(args.heuristic, "r")
        except IOError:
            print \
            (
                "\n" + str(args.heuristic) + " file not found" +
                "\nEnsure the heuristic file is in the same folder as the python file"
            )
            exit()

        for line in heuristic_filename:
            if "END OF INPUT" in line:
                break
            items = line.split()

            # Create a list with the node name and hueristic.
            #       Node( Name,    Heuristic )
            #       Node( Luebeck, 300       )
            heuristic.append((items[0], float(items[1])))
        
        heuristic_filename.close()
    else:
        heuristic = False

    filename.close()
    return routes, start_state, goal_state, heuristic

if __name__ == "__main__":
    main(sys.argv)