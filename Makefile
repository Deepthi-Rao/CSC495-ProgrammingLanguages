
pull:  
	@git pull

push:  ready
	@- git status
	@- git commit -am "saving"
	@- git push 


update:; @- git pull origin master
status:; @- git status

view:
	cd doc; echo "Viewing `	ls -t *.md | head -1`"
	open http://localhost:6419/
	cd doc; grip `	ls -t *.md | head -1`

ready: gitting 

gitting:
	@git config --global credential.helper cache
	@git config credential.helper 'cache --timeout=3600'
	@git config --global user.email dgrao2@ncsu.edum
	@git config --replace-all --global user.name 'Deepthi Rao'

F=$(shell ls *.md doc/*.md)

prep:
	@$(foreach f,$F, echo "# updating $f ... "; gawk -f etc/headers.awk $f > .tmp; mv .tmp $f; )



