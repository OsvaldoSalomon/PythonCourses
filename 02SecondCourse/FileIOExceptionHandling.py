try:
    with open('/02SecondCourse/sample', mode='r') as my_file:
        print(my_file.read())
except IOError:
    print('Issue with working with the file')
except TypeError:
    print('There was a type error')
except:
    print('Error Occurred Logging to the System')
finally:
    print("This will always run regardless of whether we have an exception or not")

print('This line was run...')
