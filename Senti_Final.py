import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt 



#import_reviewfile_and_append_name_of_teacher
l=raw_input("Enter name of teacher:")

#load_file_name_to_test_data
f = open('completeneg.txt','r')
sentence=f.read()
sid=SentimentIntensityAnalyzer()
ss=sid.polarity_scores(sentence)

#piechart
if(sid.polarity_scores(sentence)["neg"] < 0): #if_negative_convert_to_positive
	x=-(sid.polarity_scores(sentence)["neg"])
else:
	x=sid.polarity_scores(sentence)["neg"]
y=sid.polarity_scores(sentence)["pos"]

#to_display_compound
#z=sid.polarity_scores(sentence)["compound"]

j=sid.polarity_scores(sentence)["neu"]
labels=['NEGATIVE','POSITIVE','NEUTRAL']
sizes=[x,y,j]
explode=[0.1,0.1,0.1]
colors=['#ee1111','#00a300', '#ffc40d' ]
fig1, ax1=plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.tight_layout()

#to_save_as_png_and_plot
plt.savefig(l+'.png', bbox_inches='tight')

#to_display_plot
plt.show()

#print_result
z=str(ss)
print(z)
#write_result_to_result.txt
g=open("result.txt","a")
g.write("\n")
g.write(l)
g.write(z)
g.close()



