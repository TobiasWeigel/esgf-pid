import esgfpid.defaults

#
# Logging helpers
#

def logtrace(logger, msg, *args, **kwargs):
    '''
    If esgfpid.defaults.LOG_TRACE_TO_DEBUG, messages are treated
    like debug messages (with an added [trace]).
    Otherwise, they are ignored.
    '''
    if esgfpid.defaults.LOG_TRACE_TO_DEBUG:
        logdebug(logger, '[trace] '+msg, *args, **kwargs)
    else:
        pass

def logdebug(logger, msg, *args, **kwargs):
    '''
    Logs messages as DEBUG,
    unless show=True and esgfpid.defaults.LOG_SHOW_TO_INFO=True,
    (then it logs messages as INFO).
    '''
    if _is_show(kwargs):
        _logshow(logger, msg, *args, **kwargs)
    else:
        logger.debug(msg, *args, **kwargs)

def _is_show(kwargs):
    show_this_message = 'show' in kwargs and kwargs['show'] == True
    if show_this_message and esgfpid.defaults.LOG_SHOW_TO_INFO:
        return True
    return False

def _logshow(logger, msg, *args, **kwargs):
    del kwargs['show']
    logger.info(msg, *args, **kwargs)

def loginfo(logger, msg, *args, **kwargs):
    '''
    Logs messages as INFO,
    unless esgfpid.defaults.LOG_INFO_TO_DEBUG,
    (then it logs messages as DEBUG).
    '''
    if _is_show(kwargs):
        _logshow(logger, msg, *args, **kwargs)
    elif esgfpid.defaults.LOG_INFO_TO_DEBUG:
        logger.debug(msg, *args, **kwargs)
    else:
        logger.info(msg, *args, **kwargs)


def logwarn(logger, msg, *args, **kwargs):
    if _is_show(kwargs):
        _logshow(logger, '[WARN] '+msg, *args, **kwargs)
    else:
        logger.warn(msg, *args, **kwargs)

def logerror(logger, msg, *args, **kwargs):
    if _is_show(kwargs):
        _logshow(logger, '[ERROR] '+msg, *args, **kwargs)
    else:
        logger.error(msg, *args, **kwargs)

def log_every_x_times(logger, counter, x, msg, *args, **kwargs):
    '''
    Works like logdebug, but only prints first and
    and every xth message.
    '''
    if counter==1 or counter % x == 0:
        msgf = msg + (' (counter %i)' % counter)
        logdebug(logger, msgf, *args, **kwargs)
