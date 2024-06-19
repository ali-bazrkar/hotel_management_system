from sqlalchemy import exc
from model.tools.logging import Logger
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import pymysql.err


def exception_handling(function):
    def inner(*args, **kwargs):
        try:
            output = function(*args, **kwargs)
            if not "find" in function.__name__:
                Logger.info(f"{function.__qualname__}{args[1:]} [RETURNED] : {output[1]}")
            else:
                Logger.info(f"{function.__qualname__}{args[1:]}")
            return output
        except IntegrityError as e:
            if "Duplicate entry" in str(e) and "for key 'user_tbl.username'" in str(e):
                Logger.error(f"{function.__qualname__}{args[1:]} [RAISED EXCEPTION] : Username already exists")
                return False, "Username already exists"

            if isinstance(e, IntegrityError) and "Duplicate entry" in str(e):
                Logger.error("[RAISED INTEGRITY ERROR] : there is a 'Duplicate entry' for ID with 'unique' value.")
                return False, "there is a 'Duplicate entry' for ID with 'unique' value."

            if "Column" in str(e) and "cannot be null" in str(e):
                Logger.error(
                    f"{function.__qualname__}{args[1:]} [RAISED INTEGRITY ERROR] : Non-nullable column cannot be null")
                return False, "Non-nullable column cannot be null"
            else:
                Logger.error(f"{function.__qualname__}{args[1:]} [RAISED INTEGRITY ERROR] : {e}")
                return False, str(e)
        except pymysql.err.IntegrityError as e:
            Logger.error(f"{function.__qualname__}{args[1:]} [RAISED INTEGRITY ERROR] : {e}")
            return False, str(e)
        except exc.SQLAlchemyError as e:
            Logger.error(f"{function.__qualname__}{args[1:]} [RAISED SQLALCHEMY EXCEPTION] : {e}")
            return False, str(e)
        except Exception as e:
            Logger.error(f"{function.__qualname__}{args[1:]} [RAISED EXCEPTION] : {e}")
            return False, str(e)

    return inner
