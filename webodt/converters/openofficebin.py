class OpenOfficeBinODFConverter(ODFConverter):


    def convert(self, document, format=None, output_filename=None, delete_on_close=True):
        output_filename, format = self._guess_format_and_filename(output_filename, format)
	where_is_file = os.path.dirname(document.name)
	basename = os.path.basename(document.name)
 	os.system("cd "+where_is_file+ " && "+str(WEBODT_OOBIN_COMMAND)+" --headless --invisible --convert-to pdf "+str(document.name))
	converted_filename = re.sub(r"\.odt",".pdf", str(document.name))
	fd = Document(converted_filename, mode='r', delete_on_close=False)
        return fd
