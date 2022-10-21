from csv import reader
import click


def data_importer(db, dm, file_path, dtypes: list):
    # try:
        with open(file_path) as fp:
            rd = reader(fp)

            for cnt, row in enumerate(rd):
                if cnt == 0:
                    fields = row
                    continue
                data = {field: dtype(cell) for field, cell, dtype in zip(fields, row, dtypes)}
                record = dm(**data)
                db.session.add(record)
            db.session.commit()
            click.echo(click.style(f"Added {cnt} records in {dm.__name__}", fg="green"))
    # except sqlalchemy.exc.IntegrityError:
    #     click.echo(click.style(f"Could not load data in {dm.__name__}, UNIQUE constraint failed", fg="red"))
    #     db.session.rollback()
    # finally:
    #     db.session.close()
