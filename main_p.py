from graph_data import graph_data
import permutation


if __name__ == "__main__":
    all_permutations = permutation.sjt_permutations(graph_data[12])
    all_cycles = permutation.find_hamilition_cycles(graph_data[12], all_permutations)
    optimal_cycles = permutation.find_optimal_ham_cycles(all_cycles, graph_data[12])
    print("All permutations: ")
    print(all_permutations)
    print("All Hamiltonian cycles: ")
    print(all_cycles)
    print("Optimal Cycle:")
    print(optimal_cycles)