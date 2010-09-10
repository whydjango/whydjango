echo "getting boostrap.py"
if [ -f "bootstrap.py" ]; then
	rm bootstrap.py
fi
if which wget &> /dev/null; then
	wget http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py
else
    curl http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py > bootstrap.py
fi
echo "running bootstrap.py"
python bootstrap.py $*
echo "running buildout"
bin/buildout
echo "done"