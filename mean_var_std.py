import numpy as np

def calculate(list):
  if len(list) == 9:
    array = np.array(list)
    matrix = np.reshape(array, (3, 3))
    mean_ax_1 = []
    mean_ax_2 = []
    mean_flat = np.mean(list)
    var_ax_1 = []
    var_ax_2 = []
    var_flat = np.var(list)
    st_dv_ax_1 = []
    st_dv_ax_2 = []
    st_dv_flat = np.std(list)
    max_ax_1 = []
    max_ax_2 = []
    max_flat = np.max(list)
    min_ax_1 = []
    min_ax_2 = []
    min_flat = np.min(list)
    sum_ax_1 = []
    sum_ax_2 = []
    sum_flat = np.sum(list)

    for i in range(matrix[0].size):
      mean_ax_1.append(matrix[:, i].mean())
      var_ax_1.append(matrix[:, i].var())
      st_dv_ax_1.append(matrix[:, i].std())
      max_ax_1.append(matrix[:,i].max())
      min_ax_1.append(matrix[:, i].min())
      sum_ax_1.append(matrix[:, i].sum())

    for i in range(matrix[:,0].size):
      mean_ax_2.append(matrix[i].mean())
      var_ax_2.append(matrix[i].var())
      st_dv_ax_2.append(matrix[i].std())
      max_ax_2.append(matrix[i].max())
      min_ax_2.append(matrix[i].min())
      sum_ax_2.append(matrix[i].sum())

    calculations = {
      'mean': [mean_ax_1, mean_ax_2, mean_flat],
      'variance': [var_ax_1, var_ax_2, var_flat],
      'standard deviation': [st_dv_ax_1, st_dv_ax_2, st_dv_flat],
      'max': [max_ax_1, max_ax_2, max_flat],
      'min': [min_ax_1, min_ax_2, min_flat],
      'sum': [sum_ax_1, sum_ax_2, sum_flat]
    }
    return calculations
  elif len(list) !=9:raise ValueError('List must contain nine numbers ')