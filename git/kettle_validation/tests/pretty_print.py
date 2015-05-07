
__author__ = 'aoverton'


def pretty_print(issues):
    print '\n\n**{}**'.format(" Warnings ")
    for w in issues['warnings']:
        print '{}:  {}'.format(w.step_name, w.message)
    print '\n\n**{}**'.format(" Errors ")
    for w in issues['errors']:
        print '{}:  {}'.format(w.step_name, w.message)
    print '\n\n**{}**'.format(" Notifications ")
    for w in issues['notifications']:
        print '{}:  {}'.format(w.step_name, w.message)
