# app/dtos.py

class SpartanDTO:
    def __init__(self, first_name, last_name, email, stream, trainer, start_date, end_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.stream = stream
        self.trainer = trainer
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def spartan_to_dto(spartan_tuple):
        return SpartanDTO(
            first_name=spartan_tuple[1],  # Adjust index based on your DB schema
            last_name=spartan_tuple[2],
            email=spartan_tuple[3],
            stream=spartan_tuple[4],
            trainer=spartan_tuple[5],
            start_date=spartan_tuple[6],
            end_date=spartan_tuple[7]
        )

