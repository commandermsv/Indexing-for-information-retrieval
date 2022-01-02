from Simple_indexing import Store_data1
from Indexing_after_stemming import Store_data2


data1 = Store_data1() #simple indexing
data2 = Store_data2() #index after stemming


file = open("Data.txt", 'w')

file.write(" Simple Inverted Index \n")
file.write("\n Total No. of Documents         :")
file.writelines(str(data1[0]))

file.write("\n Total No. of posting List      :")
file.writelines(str(data1[1]))

file.write("\n Time taken for Index Formation :")
file.writelines(str(data1[2]) + "  Seconds")

file.write("\n For Computing AND/OR Operation -------:")

file.write("\n Posting list  of term need         :")
file.writelines(str(data1[3]))
                          
file.write("\n Posting list  of term use       :")
file.writelines(str(data1[4]))

file.write("\n Posting list  of term think      :")
file.writelines(str(data1[5]))

file.write("\n Posting list  of term surface     :")
file.writelines(str(data1[6]))

file.write("\n\n Computing (pl1 AND pl2) OR (pl3 AND pl4):")
file.writelines(str(data1[7]))

file.write("\n Computing (pl1 OR pl2) AND (pl3 OR pl4):")
file.writelines(str(data1[8]))

file.write("\n\n\n")

file.close()

file = open("Data.txt", 'a')

file.write(" Inverted Index after Stemming and Lemmatization\n")
file.write("\n Total No. of Documents         :")
file.writelines(str(data2[0]))

file.write("\n Total No. of posting List      :")
file.writelines(str(data2[1]))

file.write("\n Time taken for Index Formation :")
file.writelines(str(data2[2]) + "  Seconds")

file.write("\n For Computing AND/OR Operation -------:")

file.write("\n Posting list  of term need         :")
file.writelines(str(data2[3]))
                          
file.write("\n Posting list  of term use       :")
file.writelines(str(data2[4]))

file.write("\n Posting list  of term think      :")
file.writelines(str(data2[5]))

file.write("\n Posting list  of term surface     :")
file.writelines(str(data2[6]))

file.write("\n\n Computing (pl1 AND pl2) OR (pl3 AND pl4) :")
file.writelines(str(data2[7]))

file.write("\n Computing (pl1 OR pl2) AND (pl3 OR pl4)  :")
file.writelines(str(data2[8]))


file.close()