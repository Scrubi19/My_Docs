# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile.

# .PHONY: autobuild
	
# autobuild:
# 	inotifywait -mr source --exclude _build -e close_write -e create -e delete -e move --format '%w %e %T' --timefmt '%H%M%S' | while read file event tm; do
# 	current=$(date +'%H%M%S')
# 	delta=`expr $current - $tm`
# 	if [ $delta -lt 2 -a $delta -gt -2 ] ; then
# 		sleep 1  # спать 1 секунду на случай если не все файлы скопированы
# 		make html singlehtml
# 		xdotool search --name Chromium key --window %@ F5
# 	fi
# 	done


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)