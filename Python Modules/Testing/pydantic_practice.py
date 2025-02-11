from pydantic import BaseModel, SecretStr, validator


# Define a model using BaseModel
class Account(BaseModel):
    name: str
    balance: float
    pin: SecretStr

    # Custom validator for the balance field
    @validator("balance")
    def balance_must_be_positive(cls, value):
        if value < 0:
            raise ValueError("Balance must be positive")
        return value

    # Another custom validator to ensure the name is capitalized
    @validator("name")
    def name_must_be_capitalized(cls, value):
        if not value.istitle():
            raise ValueError("Name must be capitalized")
        return value

    class Config:
        # Prevent invalid assignment by enabling assignment validation
        validate_assignment = True


# Example usage:
try:
    account = Account(name="John", balance=100.0, pin="1234")
    print(account.dict())  # {'name': 'John', 'balance': 100.0, 'pin': '**********'}

    # Try assigning an invalid value (this will raise an error due to validate_assignment=True)
    account.balance = -50.0
except Exception as e:
    print(f"Error: {e}")

# Handle sensitive data
print(account.pin.get_secret_value())  # Access the sensitive value securely
