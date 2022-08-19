# Minimum Number Of Software Developers
# PEPCODING
# https://nados.io/question/minimum-number-of-software-developers?zen=true
# 1. You are given N strings which represents N different skills related to I.T field.
# 2. You are working on a project and you want to hire a team of software developers for that project.
# 3. There are N applicants. Every applicant has mentioned his/her skills in resume.
# 4. You have to select the minimum number of developers such that for every required skill, there is 
#      at least one person in the team who has that skill.
# 5. It is guaranteed that you can form a team which covers all the required skills.

# Note -> Check out the question video for details.





def get_bit_arr(skill,dev):
    skill_map = {}
    for i in range(len(skills)):
        skill_map[skill[i]] = i
    result = []
    for i in range(len(dev)): 
        code = 0
        for j in dev[i]:
            code = code | (1<<skill_map[j])
        result.append(code)
    return result


def get_solution(map_arr,ans,i,indexes):
    global result
    if i>=len(map_arr):
        if ans == (2**(len(map_arr))-1):
            if (not result) or (len(result)>len(indexes)):
                result = [i for i in indexes]
        return 
    first = map_arr[i]
    get_solution(map_arr,ans,i+1,indexes)
    indexes.append(i)
    get_solution(map_arr,ans | first,i+1,indexes)
    del indexes[-1]

if __name__ == '__main__':
    n = 3
    skills = ["java","nodejs","reactjs"]
    dev = [["java"],["nodejs"],["nodejs","reactjs"]]
    result  = []
    map_arr = get_bit_arr(skills,dev)
    get_solution(map_arr,0,0,[])
    print(result)