import time
import statistics
import psutil
import os

import aima_libs.hanoi_states as hanoi_states
from aima_libs.tree_hanoi import NodeHanoi

class DFS:
    """
    Clase para resolver el problema de la Torre de Hanoi usando Búsqueda en Profundidad (DFS).
    """

    def __init__(self, number_disks: int = 5):
        """
        Inicializa DFS.

        Args:
            number_disks (int): Número de discos.
        """
  
        self.number_disks = number_disks
        self.problem = self._initialize_problem()
        self.nodes_explored = 0
        self.max_depth_reached = 0

    def _initialize_problem(self):
        list_disks = [i for i in range(self.number_disks, 0, -1)]
        initial_state = hanoi_states.StatesHanoi(list_disks, [], [], max_disks=self.number_disks)
        goal_state = hanoi_states.StatesHanoi([], [], list_disks, max_disks=self.number_disks)
        return hanoi_states.ProblemHanoi(initial=initial_state, goal=goal_state)

    def depth_first_search(self):
        frontier = [NodeHanoi(self.problem.initial)] # Stack LIFO con el nodo inicial
        explored = set() # Conjunto de estados ya visitados
        self.nodes_explored = 0
        self.max_depth_reached = 0

        while frontier: # while len(frontier) != 0
            node = frontier.pop()
            self.nodes_explored += 1
            
            if node.depth > self.max_depth_reached:
                self.max_depth_reached = node.depth
            
            if node.state in explored:
                continue
            
            explored.add(node.state)
            
            if self.problem.goal_test(node.state):
                return node, self._build_metrics(node, explored, frontier, True)
            
            # Agregamos a la frontera los nodos sucesores que no hayan sido visitados
            for child in node.expand(self.problem): #'mueve' y retorna la lista de nodos hijos
                if child.state not in explored:
                    frontier.append(child)

        # Si no se encuentra solución, devolvemos métricas igualmente
        return None, self._build_metrics(node, explored, frontier, False)
    
    def _build_metrics(self, node, explored, frontier, solution_found):
        return {
            "solution_found": solution_found,
            "nodes_explored": self.nodes_explored,
            "states_visited": len(explored),
            "nodes_in_frontier": len(frontier),
            "max_depth": self.max_depth_reached,
            "cost_total": node.state.accumulated_cost if solution_found else None,
        }

    def run_performance_analysis(self, num_runs: int = 10):
        times = []
        memories = []
        cost = [] 
        
        process = psutil.Process(os.getpid())
        
        for i in range(num_runs):
            mem_before = process.memory_info().rss / (1024 ** 2)  # Convertir a MB
            start_time = time.perf_counter()
            
            solution_node, metrics = self.depth_first_search()
            
            end_time = time.perf_counter()
            mem_after = process.memory_info().rss / (1024 ** 2)  # Convertir a MB

            memories.append(mem_after - mem_before)
            times.append(end_time - start_time)
            cost.append(metrics['cost_total'] if metrics['solution_found'] else None)  

        return {
            "average_time_seconds": statistics.mean(times),
            "std_dev_time_seconds": statistics.stdev(times) if num_runs > 1 else 0.0,
            "average_memory_kb": statistics.mean(memories),
            "std_dev_memory_kb": statistics.stdev(memories) if num_runs > 1 else 0.0,
            "num_runs": num_runs,
            "average_cost": statistics.mean(cost) if cost else None,
            "std_dev_cost": statistics.stdev(cost) if num_runs > 1 else None,
            "last_run_metrics": metrics
        }
        