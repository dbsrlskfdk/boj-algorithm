import sys
def print_star(star, N, origin_size):
    if N < 3:
        return star
    else:    
        for i in range(origin_size):
            for j in range(origin_size):
                if (i // (N//3)) % 3 == 1 and (j // (N//3)) % 3 == 1:
                    star[i][j] = ' '
        return print_star(star, N//3, origin_size)

N = int(input())
star_list = [['*'] * N for i in range(N)]

star = print_star(star_list, N, N)
for i in range(N):
    for j in range(N):
        sys.stdout.write(star[i][j])
    sys.stdout.write("\n")
