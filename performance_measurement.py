import time
import matplotlib.pyplot as plt
from ai import AI
from board import Board

ai = AI()
main_board = Board()


def measure_execution_time_minmax(board, algorithm):
    start_time = time.time()
    algorithm(board, maximizing=True, depth=3)
    end_time = time.time()
    return end_time - start_time


def measure_execution_time_alph_beta(board, algorithm):
    start_time = time.time()
    algorithm(board, maximizing=True, depth=3, alpha=-100, beta=100)
    end_time = time.time()
    return end_time - start_time


# Number of nodes expanded
def count_nodes_expanded_alpha_beta(board, algorithm):
    algorithm(board, maximizing=True, depth=3, alpha=-100, beta=100)
    return ai.node_count


def count_nodes_expanded_minimax(board, algorithm):
    algorithm(board, maximizing=True, depth=3)
    return ai.node_count


# Measure execution time
execution_time_minimax = measure_execution_time_minmax(main_board, ai.minimax)
execution_time_minimax_alpha_beta = measure_execution_time_alph_beta(main_board, ai.alpha_beta)

# Count nodes expanded
ai.reset_node_count()
nodes_expanded_minimax = count_nodes_expanded_minimax(main_board, ai.minimax)
ai.reset_node_count()
nodes_expanded_minimax_alpha_beta = count_nodes_expanded_alpha_beta(main_board, ai.alpha_beta)

# Plot the results in one figure
labels = ['Minimax', 'Alpha-Beta Pruning']
execution_times = [execution_time_minimax, execution_time_minimax_alpha_beta]
nodes_expanded = [nodes_expanded_minimax, nodes_expanded_minimax_alpha_beta]

x = range(len(labels))

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# Plot execution time
ax1.bar(x, execution_times, alpha=0.8)
ax1.set_ylabel('Execution Time')
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.set_title('Execution Time Comparison')

# Plot nodes expanded
ax2.bar(x, nodes_expanded, alpha=0.8)
ax2.set_xlabel('Algorithm')
ax2.set_ylabel('Nodes Expanded')
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.set_title('Nodes Expanded Comparison')

# Adjust spacing between subplots
plt.tight_layout()

# Display the combined figure
plt.show()
