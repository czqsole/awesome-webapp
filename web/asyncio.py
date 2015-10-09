# asyncio.py

@asyncio.coroutine
def creat_pool(loop, **kw):
	logging.info("create database connection pool...")
	global __pool
	__pool = yield from aiomysql.creat_pool(
		host = kw.get('host','localhost')
		post = 
		user = 
		password = 
		db = 
		charset =
		autocommit = 
		maxsize = 
		minsize = 
		loop = loop
		)


def select(sql, args, size = None):
	log(sql, args)
	global __pool
	with(yield from __pool) as conn:
		cur = yield from conn.cursor(aiomysql.DictCursor)
		yield from cur.execute(sql.replace('?', '%s'),args or ())
		if size:
			rs = yield from cur.fetchmany(size)
		else:
			rs = yield from cur.fetchall()
		yield from cur.close()
		logging.info('rows returned: %s' % len(rs))
		return rs

def execute(sql, args):
	log(sql)
	with(yield from __pool) as conn:
		try:
			cur = yield from conn.cursor()
			yield from cur.execute(sql.replace('?','%s'),args)
			affected = cur.rowcount
			yield from cue.close()
		except BaseException as e:
			raise
		return affected

class User(Model):
	__table__ = 'users'

	id = IntegerField(primary_key = True)
	name = StringField()