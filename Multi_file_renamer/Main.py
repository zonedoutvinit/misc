import os
# Function to rename multiple files
def main():
   i = 0
   # Path of the folder containing the files
   path = "# Path of the folder"
   for filename in os.listdir(path):
      my_dest ="newname" + str(i) + ".extension of the file"
      my_source = path + filename
      my_dest = path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()
