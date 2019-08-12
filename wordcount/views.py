from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')
	
def about(request):
	return render(request,'about.html')
	
	
	
	

	
def count(request):
	data = request.GET['fulltextare']
	word_list=data.split()
	list_len =len(word_list)
	print(list_len)
	
	
	worddict ={}
	for word in word_list:
		if word in worddict:
			worddict[word]+=1
		else:
			worddict[word]=1
	
	
	sorted_list= sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
	return render(request,'count.html',{'fulltextare':data,'NOW':list_len,'worddict':sorted_list})
	
