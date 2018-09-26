class HelloWorldHandler(IPythonHandler):
    def post(self):
        #get src/dest from post somehow
        log_file='somewhere/log/' + rand_hex_something_or_other() + '.log'
        execute_shell('gsutil cp src dest > log_file')
        self.finish('Check here for copy status: $log_file')

def load_jupyter_server_extension(nb_server_app):
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], '/gsutil')
    #define params for src and dest if needed
    web_app.add_handlers(host_pattern, [(route_pattern, GsutilHandler)])