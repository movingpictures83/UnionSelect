# UnionSelect
# Language: Python
# Input: TXT
# Output: DIR
# Tested with: PluMA 1.1, Python 3.6
# Dependency: pandas==1.1.5

PluMA plugin that filters data within two sets based on a condition, then outputs the union of both filters

Input is a tab-delimited text file of keyword-value pairs:

GroupA: observables from group A
GroupB: observables from group B
annotations: chemical annotations

Output will be produced in the user-specified output directory
