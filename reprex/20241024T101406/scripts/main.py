import rpy2.robjects as ro
from rpy2.robjects.packages import importr

# Load the R base package
base = importr('base')

# Load a specific R package (e.g., ggplot2)
ggplot2 = importr('ggplot2')

# Define an R function and use it
ro.r('''
my_function <- function(x) {
    return(x + 1)
}
''')

# Call the R function from Python
r_my_function = ro.globalenv['my_function']
result = r_my_function(5)
print(result[0])  # Output will be 6
