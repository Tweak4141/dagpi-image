from concurrent.futures import ProcessPoolExecutor

executor = ProcessPoolExecutor(max_workers=4)


def get_executor() -> ProcessPoolExecutor:
	global executor
	return executor
