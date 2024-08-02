import keyboard
import sys, getopt, binascii, time

def chunk_and_type(f, i, c, w): 
   file = open(f, "rb")
   chunk = file.read(c)
   chunk_number=0
   time.sleep(w)
   while chunk:
      time.sleep(0.3)
      keyboard.write('echo "', i)
      x = binascii.hexlify(chunk)
      keyboard.write(str(x)[2:-1], i)
      keyboard.write('" >' + str(chunk_number) + '_' + f + '.txt\n\n', i)
      chunk = file.read(c)
      chunk_number += 1

def main(argv):
   help_msg = 'cbfuk.py -f <inputfile> -i <interval in seconds> -c <chunk size in bytes> -w <wait X seconds before starting to type (default is 5)>'
   inputfile = ''
   interval = 0.1
   chunk_size = 1024
   wait_time = 5
   try:
      opts, args = getopt.getopt(argv,"hf:i:c:w:",["file=","interval=", "chunk=", "wait="])
   except getopt.GetoptError:
      print (help_msg)
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print (help_msg)
         sys.exit()
      elif opt in ("-i", "--interval"):
         interval = arg
      elif opt in ("-f", "--file"):
         inputfile = arg
      elif opt in ("-c", "--chunk"):
         chunk_size = arg
      elif opt in ("-w", "--wait"):
         wait_time = arg
         
   print ('Input file is ', inputfile)
   print ('Chunk size is ', chunk_size)
   print('Interval is ', interval)
   chunk_and_type(inputfile, interval, chunk_size, wait_time)
if __name__ == "__main__":
   main(sys.argv[1:])
