import re

Input = open("data/2017/dag 20. input.txt", "r").read().split("\n")[0:-1]
particles = [list(map(int,re.findall(r"[-\d]+", line))) for line in Input]

def move_particles(particles, seconds, part):
    for step in range(seconds):
        new_particles = []
        for x,y,z,vx,vy,vz,ax,ay,az in particles:
            vx,vy,vz = vx+ax, vy+ay, vz+az
            x,y,z = x+vx,y+vy,z+vz
            new_particles.append([x,y,z,vx,vy,vz,ax,ay,az])

        particles = new_particles

        if part == 2:
            positions = [(x,y,z) for x,y,z,vx,vy,vz,ax,ay,az in particles]
            collides = [index for index, pos in enumerate(positions) if positions.count(pos) > 1]
            particles = [particle for index, particle in enumerate(particles) if index not in collides]

    return sorted([(index, abs(x)+abs(y)+abs(z)) for index, [x,y,z,vx,vy,vz,ax,ay,az] in enumerate(particles)],
                  key=lambda x: x[1])[0][0] if (part == 1) else len(particles)


part1 = move_particles(particles, 500, 1)
part2 = move_particles(particles, 500, 2)

print(part1, part2)