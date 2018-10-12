begin = '''\\documentclass[12pt]{article}
\\usepackage{graphicx}
\\usepackage{float}
\\usepackage{enumerate} 
\\usepackage[margin=.75in]{geometry} 
\\usepackage{titlepic} 
\\usepackage{amsmath}
\\usepackage{textcomp}
\\usepackage [english]{babel}
\\usepackage [autostyle, english = american]{csquotes}
\\usepackage[colorlinks]{hyperref}
\\usepackage{xcolor}
\\MakeOuterQuote{"}

\\author{}
\\title{\includegraphics[scale=1]{IV_logo.png}
\\\\InterVision Quality Compliance Report\\\\\\line(1,0){500}\\vspace{-8ex}}

\\date{}
\\begin{document}
\\maketitle
'''


def begin_flush(direction):
    if 'right' == direction or 'left' == direction:
        return '\\begin{flush' + direction + '}\n'
    print 'WRONG SYNTAX for flush direction'
def end_flush(direction):
    if 'right' == direction or 'left' == direction:
        return  '\\end{flush' + direction+ '}\n'
    print 'WRONG SYNTAX for flush direction'

def bold_text(text):
    return '\\textbf{' + text + '} '

def set_title(name, date):
    string = begin_flush('right')
    string += 'Date Tested: ' + date + '\\\\\n'
    string += 'Engineer Name: ' + name + '\\\\\n'
    string += end_flush('right')
    return string


def set_equipment_info(oem, model, serial_num):
    string = begin_flush('left')
    string += bold_text('Equipment Manufacturer: ') + oem + '\\\\\n'
    string += bold_text('Equipment Model: ') + model + '\\\\\n'
    string += bold_text('Serial Number: ') + serial_num + '\\\\\n'
    string += end_flush('left')

    return string

def set_manufacturer_specs_url(url):
    string = begin_flush('left')
    string += bold_text('Manufacturer Specifications:') + '\\\\'
    string += '\\url{' + url + '} \\\\\n'
    string += end_flush('left')

    return string


def set_quality_checks_table(os, visual_inspec, int_test, int_percent_check, burn_in_duration, inventory_check):
    # Begin table
    string = begin_flush('left')
    string += bold_text('Quality Checks:') + '\n'
    string += end_flush('left')
    string += '\\begin{table}[H]\n\\centering\n'
    string += '\\begin{tabular}{|c|l|c|}\n \\hline\n'
    string += '& ' + bold_text('Quality Checks') + ' & ' + bold_text('Pass/Fail') + '\\\\ \\hline\n'
    pass_count = 5
    # Actual Table Contents
    end_line = ' \\\\ \\hline\n'
    if 'no' in os:
        string += '1& Upgraded OS & Fail' + end_line
        pass_count -= 1
    else:
        string += '1& Upgraded OS & Pass' + end_line

    if 'no' in visual_inspec:
        string += '2& Visual Inspection (damage check) & Pass' + end_line
    else:
        string += '2& Visual Inspection (damage check) & Fail' + end_line
        pass_count -= 1
    string += '3& Tested Interfaces/Ports & Pass' + end_line
    if burn_in_duration.isdigit() and int(burn_in_duration):
        string += '4& Burn in Duration: 24+ hours & Pass' + end_line
    else:
        string += '4& Burn in Duration: 24+ hours & Fail' + end_line
        pass_count -= 1
    if inventory_check == 'yes' or inventory_check == 'y':
        string += '5& Inventory Check & Pass ' + end_line
    elif inventory_check == 'no' or inventory_check == 'n':
        string += '5& Inventory Check & Fail ' + end_line
        pass_count -= 1

    # End Table
    string += '\\end{tabular}\n\\end{table}\n'

    return string, pass_count


def set_ending(test_num, tests_passed):
    string = '\\begin{center}\n'
    string += '\\textcolor{gray}{\huge ' + str(test_num) + ' Quality Checks have been performed.}\n\n'
    if test_num == tests_passed:
        string += '\\textcolor{gray}{\huge ALL TESTS HAVE PASSED}\n'
    if test_num > tests_passed:
        string += '\\textcolor{gray}{\huge ' + str(tests_passed) + 'TESTS HAVE PASSED}\n'
    else:
        print 'tests passed > number of tests checked...'
    string += '\\end{center}\n'

    return string


def end_document():
    return '\\end{document}'

