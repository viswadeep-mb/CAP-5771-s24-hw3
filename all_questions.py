# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "In agglomerative clustering, outliers typically persist as singleton clusters or small clusters, remaining separate until higher levels of the clustering hierarchy. This facilitates the identification and removal of outliers. In contrast, the standard K-means clustering algorithm assigns each outlier to a cluster, potentially distorting the centroid of the cluster."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Unless there are ties in the proximity values, agglomerative hierarchical techniques do not involve any random elements in their algorithms"

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Agglomerative hierarchical clustering tends to be more time and memory-consuming compared to k-means, and efficiency depends on the specific characteristics of the data"

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "When a cluster is split during a post-processing step in k-means, the Sum of Squared Errors (SSE) of the clustering decreases because the points are reassigned to centroids, reducing the overall distance"

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "In K-means clustering, whenever SSE decreases, cohesion increases as points are closer to their assigned centroids."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = " In K-means clustering, whenever SSB increases, separation increases, indicating better distinction between clusters."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Cohesion (within-cluster similarity) and separation (between-cluster dissimilarity) are related in K-means"

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "In K-means clustering, the total variance can be decomposed into the sum of the SSE (within-cluster variance) and the BSS (between-cluster variance), which remains constant"

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Enhancing cohesion in k-means clustering generally results in heightened separation, as data points tend to cluster more closely within their assigned clusters, thereby making the centroids more distinguishable from each other."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Since it is a non-globular shape, each of the two final clusters will not consist only of points from one of the shaded regions."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = ""

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4 * R**2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4 * (a**2 + b**2 + R**2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "10 * (R**2)"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The centroids in Circle B are expected to shift towards the centroids of Circle A and Circle C during convergence, owing to the uniform distribution of points within each circle. Consequently, after convergence, each circle should ideally have one centroid, as the centroids redistribute to achieve a balanced distribution of points within each circle."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Circle A centroid will remain unchanged. In the case of Circle B, which initially has two centroids, one of them is likely to shift towards Circle C, promoting a balanced distribution of points. Circle C, initially without centroids, is expected to acquire one centroid from Circle B. Consequently, post-convergence, each circle is anticipated to have a single centroid."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Considering the proximity of Circles A and B, it is probable that the centroid initially located in Circle A would shift towards the midpoint between Circles A and B in the initial stages of the k-means process. In contrast, Circle C, situated farther from Circle B, may exert less influence on the centroid redistribution, maintaining its two centroids"

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {'Group A','Group B'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Groups A and B will be merged since the distance, calculated from the furthest right point in A to the furthest left point in B, is shorter than the distances between A and C, as well as between B and C."

    # type: set
    answers["(b)"] = {'Group A','Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Groups A and C will be consolidated as they exhibit the shortest complete link distance, determined by measuring from a boundary point in A to the farthest point in C. "

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'E', 'B', 'F', 'J', 'C', 'L', 'M', 'I'}

    # type: set
    answers["(a) boundary"] = {'D','G'}

    # type: set
    answers["(a) noise"] = {'A','H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','E','F','G','E','D'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M' }

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'B','C','D','E','F','G','I','J','L','M'}

    # type: set
    answers["(c)-a boundary"] = {'A','H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'A','B','C','D','E','F','G','H','I','J','L','M'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()


    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 is having the highest clustering entropy due to its more evenly distributed objects across various classes, distinguishing it from the other clusters"

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 is characterized by a prominent class with considerably higher counts in contrast to the other classes. This dominance of a single class within the cluster results in reduced entropy"

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "The distinct and prevailing blue color in each diagonal entry signifies a strong level of cohesion within the clusters. This suggests that points within the same cluster are closely grouped, ensuring consistent coherence within each cluster"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Clusters A and C are linked to Rows 1 and 3, respectively, with discernible color variations in the off-diagonal entries. Correspondingly, Rows 2 and 4 are aligned with clusters B and D, respectively, exhibiting analogous observations."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "The diagonal entries display distinct and predominantly blue attributes, setting them apart from the rest. This signifies a heightened level of cohesion within clusters B and C"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Rows 1 and 4 exhibit less defined diagonal entries, showcasing a variety of colors that suggest varying distances from all other clusters. Rows 2 and 3 display two identical colors, indicating equidistant relationships with two clusters while maintaining a greater distance from one specific cluster"

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "In two diagonal entries, there is heightened clarity and intensity in the blue color, signifying robust cohesion within clusters B and C. This consistency implies stronger intra-cluster relationships within these particular clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "In each row, two off-diagonal entries share the same colors, while one entry differs in color. This indicates that each cluster is relatively closer to two other clusters in comparison to the third one."

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "All off-diagonal entries exhibit diverse colors, implying differing distances from other clusters. Cluster A displays varying distances from other clusters, with a less defined diagonal entry suggesting weaker cohesion within this cluster."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "The clearer diagonal entry suggests strong cohesion within Cluster B. Two out of three off-diagonal entries share matching colors, indicating equidistant relationships, notably with A and C. Cluster B is notably farther from D."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "A clearer diagonal entry implies robust cohesion within Cluster C. Two out of three off-diagonal entries have matching colors, indicating equidistant relationships, particularly with B and D. Cluster C is notably farther from A."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "All off-diagonal entries showcase distinct colors, indicating varying distances from other clusters. Cluster D exhibits varying distances from other clusters (closest to C, then B, and farthest from A), with a less defined diagonal entry suggesting weaker cohesion within this cluster."

   

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

     # type: list
    answers["(a)"] = ['Hierarchical','overlapping','partial']

    # type: list
    answers["(b)"] = ['Partitional','exclusive','complete']

    # type: list
    answers["(c)"] = ['Partitional','fuzzy','complete']

    # type: list
    answers["(d)"] = ['Hierarchical','overlapping','partial']

    # type: list
    answers["(e)"] = ['Partitional','Exclusive','partial']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "It can also be hierarchical structure ,grouping students with comparable performance levels together."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "no"

    # type: string
    answers["(a) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The density of points in the nose, eyes, and mouth are much more in figure(b) than figure(a)"

    # type: string
    answers["(b) Figure (a)"] = "no"

    # type: string
    answers["(b) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = " K-means would find the nose, eyes, and mouth, but the lower density points would also be included"

    # type: string
    answers["(c)"] = "Compute the reciprocal of the density to obtain the new density, then apply DBSCAN"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
