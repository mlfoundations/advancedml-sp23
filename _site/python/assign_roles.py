import numpy as np

if __name__ == '__main__':

    roles = [
        'Scientific peer reviewer (positive)',
        'Scientific peer revieiwer (negative)',
        'Archaeologist',
        'Academic Researcher',
        # 'Industry Practitioner',
        'Hacker',
        'Private Investigator',
        # 'Social Impact Assesor',
        'Summarizer',
        'Connector',
    ] * 4

    seeds = [4]
    assignments = []
    for i, seed in enumerate(seeds):
        role_freq = {}
        np.random.seed(seed)
        assigment = []
        with open('student_list.txt', 'r') as f:
            names = [s.strip() for s in f.readlines()]
            names.sort()
        for name in names:
            randint = np.random.randint(len(roles))
            assigment.append(roles[randint])
            if roles[randint] not in role_freq:
                role_freq[roles[randint]] = 0
            role_freq[roles[randint]] += 1
            del(roles[randint])

        with open(f'assignment_{seed}.txt', 'w') as f:
            for name, role in zip(names, assigment):
                f.write(f'{name}: {role}\n')

