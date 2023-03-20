# Question: Create a function that calculates acceleration given initial velocity v1, final velocity v2, start time t1, and end time t2.

# My answer: 
def acceleration(vi, vf, ti, tf):
    return (vf - vi) / (tf - ti)
def main():
    vi = float(input('Please introduce the initial velocity in meters per second: '))
    vf = float(input('Please introduce th final velocity in meters per second: '))
    ti = float(input('Please introduce the initial time in seconds: '))
    tf = float(input('Please introduce the final time in seconds: '))
    print('The acceleration is', acceleration(vi, vf, ti, tf), 'meters per second square')
main()