from ScrapePortalUSK import PortalUSK

app = PortalUSK()










if __name__ == "__main__":

    peserta = app.findCoursesFromDir(
        './PESERTA USK',
        "FATHURRAHMAN",
        nameFakultas="Pertanian"
    )

    print(peserta)