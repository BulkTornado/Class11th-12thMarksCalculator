#MarksCalculator

def subject_input(subject, MaxSubMark):
    mark = MaxSubMark

    PeriodicTest1 = float(input(f'\nEnter your marks in Periodic Test-1 (out of 40) in {subject}: '))
    HalfYearly = float(input(f'\nEnter your marks in Half Yearly (out of {mark}) in {subject}: '))
    PeriodicTest2 = float(input(f'\nEnter your marks in Periodic Test-2 (out of 40) in {subject}: '))
    SSE = float(input(f'\nEnter your marks in Session Ending Exam (out of {mark}) in {subject}: '))

    return PeriodicTest1, HalfYearly, PeriodicTest2, SSE

def aggregateOutof100(PT1, HY, PT2, SSE, maxMarks,minMarks):
    outof10_1, outof10_2  = (PT1 * 10), (PT2 * 10)
    outof30, outof50 = (HY * 30), (SSE * 50)

    totalOutof100 = outof10_1 + outof10_2 + outof30 + outof50
    totalOutof100percent = totalOutof100 / 100

    outofmaxMarks = totalOutof100percent * maxMarks

    print(f'\nPT-1 marks out of 10: {outof10_1 :.2f}, HY  marks out of 30: {outof30 :.2f}')
    print(f'\nPT-2 marks out of 10: {outof10_2 :.2f}, SSE marks out of 50: {outof50 :.2f}')
    print(f'\nTotal marks obtained out of 100: {totalOutof100:.2f}')
    print(f'\nTotal marks obtained out of {maxMarks}: {outofmaxMarks:.2f}')

    if outofmaxMarks < minMarks:
        print(f'\nSorry, you will fail because you were {minMarks-outofmaxMarks:.2f} marks short from {minMarks} to pass')
    else:
        print(f'\nCongratulations! You have passed :D')

def PracticalSubjects(subject):
    MaxMarks, PassMarks = 70, 24

    PeriodicTest1, HalfYearly, PeriodicTest2, SSE = subject_input(subject, MaxMarks)

    PT1percent, PT2percent = (PeriodicTest1 / 40), (PeriodicTest2 / 40)
    HYpercent, SSEpercent = (HalfYearly / 70), (SSE / 70)

    print(f'\n%age in PT-1: {PT1percent * 100:.2f}%, %age in HY : {HYpercent * 100:.2f}%')
    print(f'\n%age in PT-2: {PT2percent * 100:.2f}%, %age in SSE: {SSEpercent * 100:.2f}%')

    aggregateOutof100(PT1percent, HYpercent, PT2percent, SSEpercent, MaxMarks, PassMarks)

def NonPracticalSubjects(subject):
    MaxMarks, PassMarks = 80, 27

    PeriodicTest1, HalfYearly, PeriodicTest2, SSE = subject_input(subject, MaxMarks)

    PT1percent, PT2percent = (PeriodicTest1 / 40), (PeriodicTest2 / 40)
    HYpercent, SSEpercent = (HalfYearly / 80), (SSE / 80)

    print(f'\n%age in PT-1: {PT1percent * 100:.2f}%, %age in HY : {HYpercent * 100:.2f}%')
    print(f'\n%age in PT-2: {PT2percent * 100:.2f}%, %age in SSE: {SSEpercent * 100:.2f}%')

    aggregateOutof100(PT1percent, HYpercent, PT2percent, SSEpercent, MaxMarks, PassMarks)

def StartProgram():
    is_running = True

    while is_running:
        subjects = ('Physics','Chemistry','Math','Computer Science (CS)','English')
        for index, sub in enumerate(subjects, start = 1):
            print(f'{index}. {sub}')
        print('0. Exit')
        try:
            sub_input = int(input('Enter subject (1-5 or 0 to Exit): '))
        except ValueError:
            print('Invalid input!')
            continue
        if sub_input == 0:
            is_running = False
            print('Thank you for using the Marks Calculator and Estimator :D')
        elif 1 <= sub_input <= 5:
            if sub_input in (1,2,4):
                PracticalSubjects(subjects[sub_input - 1])
            else:
                NonPracticalSubjects(subjects[sub_input - 1])
        else:
            print('Please enter a valid subject number (1-5)')

if __name__ == '__main__':
    StartProgram()


