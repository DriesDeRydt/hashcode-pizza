def to_file(slices):
    with open('output.txt', 'w') as the_file:

        the_file.write(str(len(slices)) +'\n')
        for slice in slices:
            the_file.write(slice.getText() + "\n")