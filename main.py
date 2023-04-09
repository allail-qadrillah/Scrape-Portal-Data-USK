from fastapi import FastAPI
import uvicorn
from Portal_USK import PortalUSK


app = FastAPI()
USK = PortalUSK()

PATH_DATABASE = './DATABASE'


@app.get('/get-courses')
async def get_courses(name: str,
                     fakultas: str = '',
                     jurusan: str = ''):

    return USK.findCoursesFromDir(
        path=PATH_DATABASE+'/PESERTA USK',
        namePerson=name,
        nameFakultas=fakultas,
        nameProdi=jurusan
    )


@app.get('/get-similar-name')
async def get_similar_name(name: str, limit: int = 3):

  return USK.find_similar_name( path=PATH_DATABASE+'/nama_mahasiswa.json', 
                                search=name,
                                limit=limit)

@app.get('/')
async def alwaysOnReplit():
  return "online"

if __name__ == "__main__":

  # uvicorn.run(app,  host="0.0.0.0", port=8000)
  uvicorn.run(app)
