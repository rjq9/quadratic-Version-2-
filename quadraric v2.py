import my_utilities as util
def retry():
    if str(input('Run again? (y/n)')) == 'y':
        main()
        return True
    else:
        return None
def terms():
    try:
        inp1 = int(input('Term 1'))
        inp2 = int(input('Term 2'))
        inp3 = int(input('Term 3'))
        return [inp1, inp2, inp3]
    except Exception as e:
        raise ValueError('Terms invalid. Restarting.')
def main():
    #GET TERM:
    try:
        quad = util.quadratic_coeff(str(input('Quadratic: (ax^2+bx+c form)')))
    except ValueError as e:
        print('Improperly formatted quadratic.')
        try_again = str(input('Try again? (`y` = type again, all else: term by term input)'))
        if try_again == 'y': #typed wrong?
            main()
            return None
        else: #if terms cannot be formatted to quadratic_coeff()
            quad = terms()
    print(f'Here are your terms: {quad}')
    #ACTUAL MATH
    discrim = (quad[1] ** 2) - (4 * quad[0] * quad[2])
    #THREE FORMS: sqrt elem of {Q, R, C}
    #Q:
    if util.sqrt(discrim) % 1 == 0: #if Q
        SQRT = util.sqrt(discrim)
        mode = 'Q'
    elif util.sign(discrim) == -1: #C
        SQRT = 0 + util.sqrt(abs(discrim)) * 1j
        mode = 'C'
    else: #R
        SQRT = f'sqrt({discrim})'
        mode = 'R'
    print('X-INTS:')
    print(f'Sol: {-quad[1]} ± {SQRT} all over {2 * quad[0]}')
    if mode == 'R':
        print(f'Approx (R, +): {(-quad[1] + util.sqrt(discrim)) / (2 * quad[0])}')
        print(f'Approx (R, -): {(-quad[1] - util.sqrt(discrim)) / (2 * quad[0])}')
    else:
        print(f'Approx (+): {(-quad[1] + SQRT) / (2 * quad[0])}')
        print(f'Approx (-): {(-quad[1] - SQRT) / (2 * quad[0])}')    
    print(f'VERTEX FORM: {quad[0]}(x+{quad[1]}/{2 * quad[0]})^2+{quad[2]}-{(quad[1]**2)}/{4*quad[0]}')
    print(f'VERTEX: {-quad[1]}/{2*quad[0]}, {quad[2]}-{(quad[1]**2)}/{4*quad[0]}')
    print(f'Approx: ({-quad[1]/(2*quad[0])}), ({quad[2]-(quad[1]**2)/(4*quad[0])})')
    print(f'Y-INT: {quad[2]}')
    try:
        fifth = int(input('Fifth point?'))
        if fifth != 0:
            print(f'FIFTH POINT: {(quad[0] * (fifth ** 2)) + (quad[1] * fifth) + quad[2]}')
    except ValueError:
        print('Something went wrong with fifth point assignment.')
    retry()
    return None
        
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Something went wrong. Error: {e}')
        retry()
    print('The end.')
    
