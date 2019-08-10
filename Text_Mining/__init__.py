from Text_Mining.model import SamsungReport

if __name__ == '__main__':
   #sam = SamsungReport()
   #f = sam.read_file()
   #print(f)
   #print(SamsungReport.extract_hangul(f))
   sam = SamsungReport()
   #sam.download()
   print(sam.extract_noun())