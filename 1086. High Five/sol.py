class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = {}
        if not items:
            return []

        for student, marks in items:
            if student not in students:
                students[student] = []
            students[student].append(marks)
        
        res = []
        for student, marks in students.items():
            numOfScores = len(marks)
            marks.sort(reverse=True)
            if numOfScores < 5:
                res.append([student, sum(marks)//numOfScores])
            else:
                res.append([student, sum(marks[:5])//5])
        return sorted(res, key=lambda x: x[0])