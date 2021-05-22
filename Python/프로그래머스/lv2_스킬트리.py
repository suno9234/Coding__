def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        _skill=skill
        for s in skill_tree:
            if s in _skill:
                if s!=_skill[0]:
                    break
                else:
                    _skill=_skill[1:]
                
        else:
            print(skill_tree)
            answer+=1
    return answer