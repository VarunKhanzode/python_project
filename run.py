import uvicorn, warnings, logging
from app.main import create_app

app = create_app()

logging.basicConfig(filename='record.log' ,format='%(asctime)s %(levelname)s %(name)s %(threadName)s %(filename)s %(funcName)s  : %(message)s')
warnings.filterwarnings('ignore')

if __name__ == "__main__":
    uvicorn.run("run:app", reload=True)