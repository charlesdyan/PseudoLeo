class HelloWorldHandler(IPythonHandler):
    def post(self):
        json_body = json.loads(self.request.body.decode('utf-8'))
        
        if (json_body.is_dict):
            log_file = 'somewhere/log/' + rand_hex_something_or_other() + '.log'
            cmds = ["gsutil cp {src} {dest} > {log_file}".format(src, dest, log_file) for src, dest in json_body]
            self.finish('Check here for copy status: $log_file')
            [execute_shell(cmd) for cmd in cmds]
        else:
            self.finish(400, 'response body must be of the form { "{src_url1}": "{dest_url1}", ... }')
        

def load_jupyter_server_extension(nb_server_app):
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], '/gsutil')
    web_app.add_handlers(host_pattern, [(route_pattern, GsutilHandler)])