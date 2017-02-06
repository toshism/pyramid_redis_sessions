def no_session_renew_factory(handler, registry):

    def no_session_renew_tween(request):
        bypass_paths = request.registry.settings.get('redis.sessions.bypass_routes', '').split(',')
        if request.path in bypass_paths:
            request.session._no_update = True

        response = handler(request)

        return response

    return no_session_renew_tween
