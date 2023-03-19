#ICA7 Part 2 Kati Johnson CSC302W1

#Use read.csv function in R to the file. 

df = read.csv("C:\\Users\\kati.johnson\\Desktop\\DATA\\boxoffice.csv", header=T)

#show the first lines by using head()
head(df)


#output the amount for Star Wars
df[df['title_short']=='Star Wars', 'amount']
df[1,4]
