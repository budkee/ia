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
    
    # Initialize a stack for DFS
    stack = Stack()

    # Push the starting state with an empty path and a cost of 0
    start_state = problem.getStartState()
    stack.push((start_state, [], 0)) # (state, path, cost)

    # Maintain a set to track visited nodes
    visited = set()

    while not stack.isEmpty():
        # Pop the top state from the stack
        state, path, cost = stack.pop()

        # If the state is the goal, return the path
        if problem.isGoalState(state):
            return path

        # If the state has not been visited, process it
        if state not in visited:
            visited.add(state)

            # Get successors and push them onto the stack
            for successor, action, step_cost in problem.getSuccessors(state): #type: ignore
                if successor not in visited:
                    new_path = path + [action]
                    stack.push((successor, new_path, cost + step_cost))

    return []  # Return empty list if no solution is found
    # util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
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
    Realiza una exploración completa del espacio del laberinto.
    Devuelve el camino completo de exploración.
    """
    
    # ----- Inicialización de Variables y Estados iniciales -----
    # Camino de exploración completo
    camino_exploracion = []  
    # Conjunto de nodos visitados
    casillas_visitadas = list()  
    # Pila de nodos a explorar
    frontera = util.Stack()  

    
    # Estado inicial
    inicio = problem.getStartState()
    frontera.push((inicio, []))  # (estado del nodo, camino hasta él)
    casillas_visitadas.append(inicio)  # [nodo1, nodo2, ...]
    

    # ----- Búsqueda en Profundidad -----
    while not frontera.isEmpty():
        
        # Extrae el nodo de la frontera y guarda el camino actual
        nodo_actual, camino_actual = frontera.pop()
        camino_exploracion.extend(camino_actual)
        
        # A cada iteracion se crea un nuevo estado
        acciones_legales = problem.getSuccessors(inicio) # Pasa el state y return (successor, action, stepCost)

        # Explora los sucesores del nodo actual
        for accion in acciones_legales: #type: ignore
            
            sucesor = problem.getSuccessors(nodo_actual) # (successor, action, stepCost)

            if sucesor not in casillas_visitadas:
                # Añade el sucesor a la frontera
                frontera.push((sucesor, camino_actual + [accion]))
                # Añade el sucesor a las casillas visitadas
                casillas_visitadas.append(sucesor)

    return camino_exploracion  # Devuelve el camino de exploración completa

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
exp = exploracion
