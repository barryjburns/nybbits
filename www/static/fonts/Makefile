FONTS := $(wildcard *.ttf)
CSS := $(FONTS:.ttf=.css)

all:	$(CSS)

%.woff:	%.ttf
	sfnt2woff $<

%.woff2:	%.ttf
	woff2_compress $<

%.eot:	%.ttf
	mkeot $< > $@

%.svg:	%.ttf
	ttf2svg $< -autorange -id $* -o $@

%.css:	%.woff %.svg %.woff2 %.eot %.ttf
	./mkfontcss.sh $* > $@
