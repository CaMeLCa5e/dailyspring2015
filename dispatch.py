def this():
	##

def that():
	##

dispatch = {
	'do_something': this,
	'do_something_else': that
}

dispatch['do_something']()