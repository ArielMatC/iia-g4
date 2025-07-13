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

    performance_results = dfs.run_performance_analysis(num_runs=10)

    print("\nPromedio y Desvío Estándar de 10 ejecucioens")
    print(f"Tiempo promedio de ejecución: {performance_results['average_time_seconds']:.4f} segundos")
    print(f"Desvío estándar del tiempo: {performance_results['std_dev_time_seconds']:.4f} segundos")
    print(f"Memoria promedio utilizada: {performance_results['average_memory_kb']/ 1024:.2f} MB")
    print(f"Desvío estándar de memoria: {performance_results['std_dev_memory_kb']/ 1024:.2f} MB")
    print(f"Costo: {performance_results['average_cost']}")
    print(f"Desvío estándar del costo: {performance_results['std_dev_cost']} MB")
    
    solution_node.generate_solution_for_simulator()

if __name__ == "__main__":
    main()