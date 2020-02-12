from models import db, Jobs

def table():
    db.session.add(Jobs(
        name = "Mcdonalds",
        position = "Crew Member",
        location = "Miami Gardens, FL",
        salary = "$10.21"
        ))
    db.session.add(Jobs(
        name = "Wendys",
        position = "Crew Member",
        location = "Miami Gardens, FL",
        salary = "$10.75"
        ))
    db.session.add(Jobs(
        name = "Popeye's",
        position = "Crew Member",
        location = "Carol City, FL",
        salary = "$9.74"
        ))

    db.session.commit()
    return "successfully added"
