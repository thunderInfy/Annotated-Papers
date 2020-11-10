from html5print import HTMLBeautifier

top = '<!DOCTYPE html><html><head><title>Annotated Papers</title><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous"></head><body><div class="jumbotron jumbotron-fluid text-white text-center" style="background-color: #aaa"><div class="container"><p class="lead">Highlights may not show up in some pdf viewers like Weava Highlighter, please use a different pdf viewer if it happens</p></div></div>'

loop = '<div class="container">'
cols = 3

data = [

		{
		'Image':'/5.jpg',
		'Title':'Grad-CAM',
		'Descr':'Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization',
		'Video': 'https://www.youtube.com/watch?v=xGZfAoh0xKs',
		'Paper':'papers/Grad-CAM.pdf'
		}

		,

		{
		'Image':'/4.jpg',
		'Title':'Momentum Contrastive Learning',
		'Descr':'Momentum Contrast for Unsupervised Visual Representation Learning',
		'Blog': 'https://medium.com/analytics-vidhya/simclr-with-less-computational-constraints-moco-v2-in-pytorch-3d8f3a8f8bf2',
		'Paper':'papers/moco.pdf'
		}

		,

		{
		'Image':'/3.jpg',
		'Title':'PCL',
		'Descr':'Prototypical Contrastive Learning of Unsupervised Representations',
		'Paper':'papers/PCL.pdf'
		}

		,

		{
		'Image':'/2.jpg',
		'Title':'BabyWalk',
		'Descr':'Going Farther in Vision-and-Language Navigation by Taking Baby Steps',
		'Paper':'papers/babywalk.pdf'
		}

		,

		{
		'Image':'/1.jpg',
		'Title':'Multi Head Contrastive Learning',
		'Descr':'What should not be Contrastive in Contrastive Learning',
		'Paper':'papers/multi_head_cl.pdf'
		}

		,

		{
		'Image':'/0.jpg',
		'Title':'SimCLR',
		'Descr':'A Simple Framework for Contrastive Learning of Visual Representations',
		'Paper':'papers/simclr.pdf', 
		'Blog': 'https://medium.com/analytics-vidhya/understanding-simclr-a-simple-framework-for-contrastive-learning-of-visual-representations-d544a9003f3c'
		}

		]

temp0 = '<div class="card text-center" style="width: 18rem;"><img src="images'
temp1 = '" class="card-img-top" alt="..."><div class="card-body"><h5 class="card-title">'
temp2 = '</h5><p class="card-text">'
temp3 = '</p>'
temp4 = '</div></div>'

def onecol(a0):
	s0 = '<div class="container"><div class="row"><div class="col">'
	s2 = '</div></div></div>'
	return s0+a0+s2

def twocols(a0,a1):
	s0 = '<div class="container"><div class="row"><div class="col">'
	s1 = '</div><div class="col">'
	s2 = '</div></div></div>'
	return s0+a0+s1+a1+s2

col = 0

for d in data:

	if col==0:
		loop += '<div class="row justify-content-start">'

	loop += '<div class="col">'

	loop += temp0
	loop += d['Image'] 
	loop += temp1 
	loop += d['Title'] 
	loop += temp2 
	loop += d['Descr'] 
	loop += temp3

	if 'Blog' in d.keys():
		a0 = '<a href='+ d['Paper'] + ' target="_blank" class="btn btn-primary">Paper</a>'
		a1 = '<a href='+ d['Blog'] + ' target="_blank" class="btn btn-primary">Blog</a>'

		loop += twocols(a0, a1);
	elif 'Video' in d.keys():
		a0 = '<a href='+ d['Paper'] + ' target="_blank" class="btn btn-primary">Paper</a>'
		a1 = '<a href='+ d['Video'] + ' target="_blank" class="btn btn-primary">Video</a>'

		loop += twocols(a0, a1);
	else:
		a0 = '<a href='+ d['Paper'] + ' target="_blank" class="btn btn-primary">Paper</a>'
		loop += onecol(a0)		

	loop += temp4 

	loop += '</div>'

	if col==cols-1:
		loop += '</div>'

	col = (col+1)%cols

while col!=0:
	loop += '<div class="col">'
	loop += '</div>'
	if col==cols-1:
		loop += '</div>'

	col = (col+1)%cols

loop += '</div>'


bottom = '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script><script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script><script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script></body></html>'


page = HTMLBeautifier.beautify(top+loop+bottom)

f = open("index.html", "w")
f.write(page)
f.close()