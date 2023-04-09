from fastapi import FastAPI
import uvicorn
from Portal_USK import PortalUSK


app = FastAPI()
USK = PortalUSK()

PATH_DATABASE = './DATABASE'


@app.get('/getcourses')
async def getCourses(name: str,
                     fakultas: str = '',
                     jurusan: str = ''):

    return USK.findCoursesFromDir(
        path=PATH_DATABASE+'/PESERTA USK',
        namePerson=name,
        nameFakultas=fakultas,
        nameProdi=jurusan
    )


@app.get('/')
async def alwaysOnReplit():
  return "online"

if __name__ == "__main__":

  # uvicorn.run(app,  host="0.0.0.0", port=8000)
  uvicorn.run(app)
