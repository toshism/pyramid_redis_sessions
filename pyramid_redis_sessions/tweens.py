def no_session_renew_factory(handler, registry):

    def no_session_renew_tween(request):
        bypass_paths = request.registry.settings.get('redis.sessions_bypass', '').split(',')
        if request.path in bypass_paths:
            request.session._no_update = True

        response = handler(request)

        if hasattr(request.session, '_no_update'):
            del request.session._no_update

        return response

    return no_session_renew_tween
