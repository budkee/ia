# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from pacman import GameState
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

# ------------ Estrategias de Búsqueda ------------
def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w] #type: ignore

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    
    # ------- Inicialización -------
    pila = Stack()
    start_state = problem.getStartState()
    pila.push((start_state, [], 0)) # (state, path, cost)
    visited = set()

    # ------- Bucle de exploración -------
    while not pila.isEmpty():
        # Pop the top state from the stack
        state, path, cost = pila.pop()

        # Test de Objetivo
        if problem.isGoalState(state):
            return path

        # If the state has not been visited, process it
        if state not in visited:
            visited.add(state)

            # Get successors and push them onto the stack
            for successor, action, step_cost in problem.getSuccessors(state): #type: ignore
                if successor not in visited:
                    new_path = path + [action]
                    pila.push((successor, new_path, cost + step_cost))

    return [] 
    # util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue

    # ------- Inicialización -------
    fila = Queue()
    start_state = problem.getStartState()
    fila.push((start_state, []), 0)
    visited = {}

    # ------- Bucle de exploración -------
    while not fila.isEmpty():
        state, path = fila.pop()
        cost = problem.getCostOfActions(path)

        # Test de Objetivo
        if problem.isGoalState(state):
            return path
        
        # Solo se actualiza si se encuentra un camino de menor costo
        if state not in visited or cost < visited[state]:
            visited[state] = cost
            for successor, action, step_cost in problem.getSuccessors(state): #type: ignore
                new_path = path + [action]
                new_cost = cost + step_cost
                fila.push((successor, new_path), new_cost)
    return []

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    """Busca expandiendo el nodo de menor costo acumulado primero."""
    from util import PriorityQueue
    pq = PriorityQueue()
    start_state = problem.getStartState()
    # La prioridad inicial es 0
    pq.push((start_state, []), 0)
    visited = {}
    
    while not pq.isEmpty():
        state, path = pq.pop()
        cost = problem.getCostOfActions(path)
        if problem.isGoalState(state):
            return path
        
        # Solo se actualiza si se encuentra un camino de menor costo
        if state not in visited or cost < visited[state]:
            visited[state] = cost
            for successor, action, step_cost in problem.getSuccessors(state): #type: ignore
                new_path = path + [action]
                new_cost = cost + step_cost
                pq.push((successor, new_path), new_cost)
    return []

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """Búsqueda A* que utiliza la función heurística para guiar la búsqueda."""
    # ----------------- Inicialización de Variables -----------------
    pq = util.PriorityQueue()
    start_state = problem.getStartState()
    start_priority = heuristic(start_state, problem)
    pq.push((start_state, []), start_priority)
    visited = {}
    
    while not pq.isEmpty():
        state, path = pq.pop() # (estado, camino)
        cost = problem.getCostOfActions(path)
        
        # Test de Objetivo
        if problem.isGoalState(state):
            return path
        
        # Verifica si el estado ya fue visitado y si el costo de este estado es menor que el anterior
        if state not in visited or cost < visited[state]:
            visited[state] = cost
            for successor, action, step_cost in problem.getSuccessors(state): #type: ignore
                new_path = path + [action]
                new_cost = cost + step_cost
                priority = new_cost + heuristic(successor, problem)
                pq.push((successor, new_path), priority)
    return []

# ------------ Agente de Exploración ------------

def exploracion(problem: SearchProblem) -> List[Directions]:
    """
    Realiza una exploración completa del espacio del laberinto usando BFS.
    Devuelve el camino completo de exploración.
    """
    
    # ----- Inicialización -----
    camino_exploracion = []  # Lista que almacenará el camino completo
    casillas_visitadas = set()  # Conjunto de nodos ya explorados
    frontera = util.Stack()  # Pila para manejar la exploración
    
    # Estado inicial
    inicio = problem.getStartState()
    casillas_visitadas.add(inicio)
    frontera.push((inicio, []))
    # nodo_actual = inicio
    # camino_actual = []
    
    # ----- Bucle de exploración -----
    while not frontera.isEmpty():
        # Extraer el nodo actual y su camino    
        nodo_actual, camino_actual = frontera.pop()
        casillas_visitadas.add(nodo_actual)
        print(nodo_actual, camino_actual)
    
        # Agregar el camino tomado hasta el momento
        if camino_actual:
            camino_exploracion.append(camino_actual[-1])  # Solo la última acción

        # Test Objetivo
        if problem.isGoalState(nodo_actual):
            return camino_exploracion
        
        sucesores = problem.getSuccessors(nodo_actual)
        # print(sucesores)
        # Obtener los sucesores del nodo actual
        for sucesor, accion, _ in sucesores:  
            if sucesor not in casillas_visitadas:
                
                # Agregar a la pila con el camino actualizado
                frontera.push((sucesor, camino_actual + [accion]))
        

    return camino_exploracion


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
exp = exploracion
