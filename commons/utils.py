import uuid, os

def get_image_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	return os.path.join(instance._meta.db_table, filename)