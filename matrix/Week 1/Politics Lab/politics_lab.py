# version code 542eddf1f327+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





# Be sure that the file voting_record_dump109.txt is in the matrix/ directory.
voting_data = list(open("voting_record_dump109.txt"))
## 1: (Task 2.12.1) Create Voting Dict
def create_voting_dict():
    """
    Input: a list of strings.  Each string represents the voting record of a senator.
           The string consists of 
              - the senator's last name, 
              - a letter indicating the senator's party,
              - a couple of letters indicating the senator's home state, and
              - a sequence of numbers (0's, 1's, and negative 1's) indicating the senator's
                votes on bills
              all separated by spaces.
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting record.
    Example: 
        >>> vd = create_voting_dict(['Kennedy D MA -1 -1 1 1', 'Snowe R ME 1 1 1 1'])
        >>> vd == {'Snowe': [1, 1, 1, 1], 'Kennedy': [-1, -1, 1, 1]}
        True

    You can use the .split() method to split each string in the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.

    You can use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    The lists for each senator should preserve the order listed in voting data.
    In case you're feeling clever, this can be done in one line.
    """
    voting_dic = {}

    for s in voting_data:
        s = s.strip()
        items = s.split(' ')
        voting_dic[items[0]] = [int(v) for v in items[3:]]

    return voting_dic



## 2: (Task 2.12.2) Policy Compare
def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    
    The code should correct compute dot-product even if the numbers are not all in {0,1,-1}.
        >>> policy_compare('A', 'B', {'A':[100,10,1], 'B':[2,5,3]})
        253
        
    You should definitely try to write this in one line.
    """
    assert len(voting_dict[sen_a]) == len(voting_dict[sen_b])

    return sum([voting_dict[sen_a][k]*voting_dict[sen_b][k] for k in range(0,len(voting_dict[sen_a]))])



## 3: (Task 2.12.3) Most Similar
def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'
        >>> vd == {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        True
        >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0], 'd': [-1,0,0], 'e': [1, 0, 0]}
        >>> most_similar('c', vd)
        'd'

    Note that you can (and are encouraged to) re-use your policy_compare procedure.
    """
    
    score_map = {policy_compare(sen,another_guy,voting_dict):another_guy for another_guy in voting_dict.keys() if another_guy != sen}
    return score_map[max(score_map.keys())]



## 4: (Task 2.12.4) Least Similar
def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        >>> least_similar('a', vd)
        'c'
        >>> vd == {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        True
        >>> vd = {'a': [-1,0,0], 'b': [1,0,0], 'c': [-1,0,0]}
        >>> least_similar('c', vd)
        'b'
    """
    score_map = {policy_compare(sen,another_guy,voting_dict):another_guy for another_guy in voting_dict.keys() if another_guy != sen}

    return score_map[min(score_map.keys())]

    return ""



## 5: (Task 2.12.5) Chafee, Santorum

most_like_chafee = most_similar('Chafee',create_voting_dict())
least_like_santorum = least_similar('Santorum',create_voting_dict())  



## 6: (Task 2.12.7) Most Average Democrat
def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        >>> sens = {'Fox-Epstein','Ravella','Oyakawa','Loery'}
        >>> find_average_similarity('Klein', sens, vd)
        -0.5
        >>> sens == {'Fox-Epstein','Ravella', 'Oyakawa', 'Loery'}
        True
        >>> vd == {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        True
    """
    
    score_list = [policy_compare(sen,another_guy,voting_dict) for another_guy in sen_set]
    if 0 < len(score_list):
        return sum(score_list) / len(score_list)
    else:
        return 0

# Not in the function
set_of_Democrat = set()
set_of_all_sen = set()
for s in voting_data:
    s = s.strip()
    items = s.split(' ')
    set_of_all_sen.add(items[0])
    if items[1] == 'D':
        set_of_Democrat.add(items[0])
        

score_sen_map = {find_average_similarity(sen,set_of_Democrat, create_voting_dict()):sen for sen in set_of_all_sen}

most_average_Democrat = score_sen_map[max(score_sen_map.keys())] 




## 7: (Task 2.12.8) Average Record
def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> senators = {'Fox-Epstein','Ravella'}
        >>> find_average_record(senators, voting_dict)
        [-0.5, -0.5, 0.0]
        >>> voting_dict == {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        True
        >>> senators
        {'Fox-Epstein','Ravella'}
        >>> d = {'c': [-1,-1,0], 'b': [0,1,1], 'a': [0,1,1], 'e': [-1,-1,1], 'd': [-1,1,1]}
        >>> find_average_record({'a','c','e'}, d)
        [-0.6666666666666666, -0.3333333333333333, 0.6666666666666666]
        >>> find_average_record({'a','c','e','b'}, d)
        [-0.5, 0.0, 0.75]
        >>> find_average_record({'a'}, d)
        [0.0, 1.0, 1.0]
    """
    assert len(sen_set) > 0
    rlt_vec = list()
    for sen in sen_set:
        rlt_vec = [0]*len(voting_dict[sen])
        break
    for sen in sen_set:
        for i in range(0, len(voting_dict[sen])):
            rlt_vec[i] += voting_dict[sen][i]/len(sen_set)
    return rlt_vec

average_Democrat_record = find_average_record(set_of_Democrat, create_voting_dict()) # (give the vector)

new_vd = create_voting_dict()
new_vd['ALLDemocrat'] = average_Democrat_record

most_average_Democrat2 = most_similar('ALLDemocrat', new_vd)



## 8: (Task 2.12.9) Bitter Rivals
def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein':[-1,0,1], 'Fox-Epstein':[-1,-1,-1], 'Ravella':[0,0,1], 'Oyakawa':[1,1,1], 'Loery':[1,1,0]}
        >>> br = bitter_rivals(voting_dict)
        >>> br == ('Fox-Epstein', 'Oyakawa') or br == ('Oyakawa', 'Fox-Epstein')
        True
    """
    score_person_pair_dic = {policy_compare(p1,p2,voting_dict):(p1,p2) for p1 in voting_dict.keys() for p2 in voting_dict.keys()}
    return score_person_pair_dic[min(score_person_pair_dic.keys())]

