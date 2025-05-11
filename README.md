# Find Route

<br>

## About
This program implements state space search in order to find a route between any two cities (nodes). <br>
On completion, the program will output the length of the route, all cities (nodes) along that route, <br>
and the total number of nodes expanded and generated.
> [!NOTE]
> This program is a modification of an assignment for UTA's CSE 4308 Artificial Intelligence.

<br>

The input files are stored as .txt files in `/src`; e.g., the graph above would have the follwing representation:
```
Luebeck Hamburg 63      # Defines a 63 km route between Luebeck and Hamburg
Hamburg Bremen 116
Hamburg Hannover 153
Hamburg Berlin 291
...
END OF INPUT            # Required for EOF
```
The routes in the input file do not need to be defined for both directions; i.e., `Luebeck Hambug 63` satisfies <br>
both `Luebeck to Hamburg` and `Hamburg to Luebeck`. For multi-word cities, use an underscore to separate them; <br>
e.g., `New_York`.

<br>

Heuristics are stored as .txt files in `/src` and should have a similar representation:
```
Luebeck 300
Hamburg 200
Hannover 100
...
END OF INPUT
```
Heuristics are optional. If not provided, the program will perform uninformed search instead. 

<br>

The following shows example program output for `find_route Bremen Kassel`:
```
Nodes Popped: 12
Nodes Expanded: 6
Nodes Generated: 20
Distance: 297.0 km
Route:
  Bremen to Hannover, 132.0 km
  Hannover to Kassel, 165.0 km
```

<br>

## Usages
- Use `python find_route.py <input_filename> <origin_city> <destination_city>` to run uninformed search.
- Use `python find_route.py <input_filename> <origin_city> <destination_city> <heuristic_filename>` to run informed search.
- Use `python find_route_test.py` to unit test the program.

<br>

## Creators
- Arian G.
