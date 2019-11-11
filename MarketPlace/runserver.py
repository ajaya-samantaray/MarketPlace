import logging as logger
logger.basicConfig(level="DEBUG")


# Run Server
if __name__ == '__main__':
    logger.debug("Starting Flask Server")
    from MarketPlace.api import *

    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
