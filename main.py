def grades(*grades, situation=False):
    report_card = dict()
    report_card['total'] = len(grades)
    report_card['greater'] = max(grades)
    report_card['lowest'] = min(grades)
    report_card['average'] = sum(grades)/len(grades)
    if situation:
        if report_card['average'] >= 7:
            report_card['situation'] = 'GOOD'
        elif report_card['average'] >= 5:
            report_card['situation'] = 'REASONABLE'
        else:
            report_card['situation'] = 'BAD'
    return report_card

# Main Program
print('-=' * 30)
answer = grades(5.5, 2.5, 1.5, situation=True)
print(f'\033[1;32m{answer}\033[m')
print('-=' * 30)
print()
help(grades)