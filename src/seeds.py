from models import db, Users

def table():
    db.session.add(Users(
        username = "bobcaboo" ,
        email = "bobbycaca@wea.com",
        password ="rigo123"
    ))
    db.session.add(Users(
        username = "CurlyPvictor" ,
        email = "victorpierre@gmail.com",
        password = "Choeurlee7289"
    ))
    db.session.add(Users(
        username = "Justusmays",
        email = "justusmays@outlook.com",
        password = "Justus7289"
    ))
    db.session.add(Users(
        username = "RaejayLindsay",
        email = "Anthonylindsay@gmail.com",
        password ="Anthony7289"
    ))
    db.session.add(Users(
        username = "Nasteeth",
        email = "Nasisalonelyvirgin@incel.net",
        password = "Weaboo7289"
    ))
    db.session.add(Users(
        username = "ZionR",
        email = "Raymondjr@aol.com",
        password ="Zion7289"
    ))
    db.session.add(Users(
        username = "Issac25",
        email = "Otakuboy@incel.com",
        password = "Incel7289"
    ))
    db.session.add(Users(
        username = 'bobcaboo' ,
        email = 'bobbycaca@wea.com',
        password ='rigo123'
    ))
    db.session.add(Users(
        username = "hello641" ,
        email = "fafababa@wer.com",
        password = "tytyy65"
    ))
    db.session.add(Users(
        username = "odin23" ,
        email =" wendesdays@rte.com",
        password = "dfanekal"
    ))
    db.session.add(Users(
        username = "freya" ,
        email = "lightmyblade@rabbit.com",
        password = "macaroni"
    ))
    db.session.add(Users(
        username = "lokiicegiant" ,
        email = "vil@evilness.com" ,
        password = "nasnas"
    ))
    db.session.add(Users(
        username = "cubanlinks" ,
        email = "rodwave@wer.com" ,
        password = "hellolol"
    ))

    db.session.commit()
    return "successfully added"



