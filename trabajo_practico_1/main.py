import time
import statistics
import tracemalloc

#from bfs.bfs import BFS
from dfs.dfs import DFS

def main():
    """
    Función principal para resolver el problema de la Torre de Hanoi de 5 discos con DFS.
    """
    dfs = DFS(number_disks=5)
    solution_node, metrics = dfs.depth_first_search()

    # bfs = BFS(number_disks=num_disks)
    # solution_node, metrics = bfs.breadth_first_search()

    print("Métricas:")
    for key, value in metrics.items():
        print(f"{key}: {value}")

    print("\nCamino completo desde el estado inicial hasta la solución (Nodos)")
    for nodo in solution_node.path():
        print(nodo)

    print("\nAcciones que el agente debería aplicar para llegar al objetivo")
    for act in solution_node.solution():
        print(act)

    performance_results = run_performance_analysis(dfs, num_runs=10)

    print(f"\nPromedio y Desvío Estándar de {performance_results['num_runs']} ejecuciones")
    print(f"Tiempo promedio de ejecución: {performance_results['average_time_seconds']:.4f} segundos")
    print(f"Desvío estándar del tiempo: {performance_results['std_dev_time_seconds']:.4f} segundos")
    print(f"Memoria promedio utilizada: {performance_results['average_memory_kb']:.2f} KB")
    print(f"Desvío estándar de memoria: {performance_results['std_dev_memory_kb']:.2f} KB")
    print(f"Costo: {performance_results['average_cost']}")
    print(f"Desvío estándar del costo: {performance_results['std_dev_cost']} MB")
    
    solution_node.generate_solution_for_simulator()

def run_performance_analysis(dfs, num_runs: int = 10):
    times = []
    memories = []
    cost = [] 
    
    for i in range(num_runs):
        tracemalloc.start()
        start_time = time.perf_counter()
        
        solution_node, metrics = dfs.depth_first_search()
        
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        times.append(end_time - start_time)
        memories.append(peak / 1024)  # Convertir a KB
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

if __name__ == "__main__":
    main()