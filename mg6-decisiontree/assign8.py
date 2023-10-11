from assign7 import dtc
from sklearn import tree
from assign7 import train_data
import graphviz

dot_data = tree.export_graphviz(dtc, out_file=None, feature_names = train_data.columns, max_depth=4)

graph = graphviz.Source(dot_data, format="png")
graph.render(view=True)