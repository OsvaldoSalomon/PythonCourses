class Email:
    valid_domain = "epicprogram.io"

    def __init__(self, subject, body, from_recipient):
        self.subject = subject
        self.body = body
        self.is_from_recipient_valid(self.valid_domain, from_recipient)
        self.__from_recipient = from_recipient

    @property
    def from_recipient(self):
        return self.__from_recipient

    @from_recipient.setter
    def from_recipient(self, from_recipient):
        self.is_from_recipient_valid(self.valid_domain, from_recipient)
        self.__from_recipient = from_recipient

    def send(self, to):
        print(f"Sending email from: {self.__from_recipient} with subject: {self.subject} and body: {self.body} to: {to}")

    @classmethod
    def greeting(cls):
        return cls("Welcome", "Welcome to epic programming.io", "greeting@epicprogramming.io")

    @staticmethod
    def is_from_recipient_valid(valid_domain, from_recipient):
        split = from_recipient.split("@")
        if split[1] != valid_domain:
            raise Exception("Invalid domain")



if __name__ == "__main__":
    greeting_email = Email("Welcome!", "Welcome to this program!", "osvaldo@epicprogram.io")
    bf_email = Email("Black Friday 2020!", "50% discount on our platform", "bf@epicprogram.io")

    # bf_email.from_recipient = "bf@epicprogramming.uk"

    greeting_email.send("bob@nasa.gov")
    bf_email.send("alex@gmail.com")
