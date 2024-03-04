# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Hierarchical clustering allows for the detection of outliers at various levels of the hierarchy. Outliers may form small, separate clusters or singletons, but their impact on the overall clustering structure is often limited."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Different runs of agglomerative hierarchical clustering procedures can produce different clusterings due to the nature of the algorithm"

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
    answers["(e) explain"] = "n K-means clustering, whenever SSE decreases, cohesion increases as points are closer to their assigned centroids."

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
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "While improving cohesion in K-means might indicate smaller SSE, it doesn't necessarily guarantee improved separation (larger SSB). The two are related but not strictly dependent on each other."

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
    answers["(a) core"] = set()

    # type: set
    answers["(a) boundary"] = set()

    # type: set
    answers["(a) noise"] = set()

    # type: set
    answers["(b) cluster 1"] = set()

    # type: set
    answers["(b) cluster 2"] = set()

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = set()

    # type: set
    answers["(c)-a boundary"] = set()

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = set()

    # type: set
    answers["(c)-b cluster 2"] = set()

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: string
    answers["(b)"] = ""

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = ""

    # type: string
    answers["(a) Matrix 2"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = ""

    # type: string
    answers["(a) Matrix 3"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = ""

    # type: string
    answers["(b) Row 1"] = ""

    # type: string
    answers["(b) Row 2"] = ""

    # type: string
    answers["(b) Row 3"] = ""

    # type: string
    answers["(b) Row 4"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = ""

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = []

    # type: list
    answers["(b)"] = []

    # type: list
    answers["(c)"] = []

    # type: list
    answers["(d)"] = []

    # type: list
    answers["(e)"] = []

    # type: explanatory string (at least four words)
    answers["(e) explain"] = ""

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = ""

    # type: string
    answers["(a) Figure (b)"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: string
    answers["(b) Figure (a)"] = ""

    # type: string
    answers["(b) Figure (b)"] = ""

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: string
    answers["(c)"] = ""

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
