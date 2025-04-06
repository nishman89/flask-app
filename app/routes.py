from flask import Blueprint, jsonify, redirect, url_for
from app.database import mysql
from app.dtos import SpartanDTO  # Import SpartanDTO to handle data transfer objects

# Create a Blueprint for Spartan routes
spartan_routes = Blueprint('spartan_routes', __name__)


# Route to retrieve all Spartans from the database
@spartan_routes.route('/spartans', methods=['GET'])
def get_spartans():
    """
    Fetches all Spartans from the database and returns them as a JSON response.

    Key concepts:
    - **Cursor**: A database cursor is a control structure that allows traversal over database records.
    - **Tuple (from fetchall)**: Each Spartan record retrieved is a tuple containing multiple fields.
    - **DTO (Data Transfer Object)**: A design pattern used to encapsulate data and transfer it efficiently.

    Steps:
    1. Establish a database connection.
    2. Create a cursor object to interact with the database.
    3. Execute a query to fetch all records from the 'spartans' table.
    4. Retrieve all results as a list of tuples.
    5. Convert each tuple into a SpartanDTO object for structured data representation.
    6. Convert each SpartanDTO object into a dictionary for JSON serialization.
    7. Return the list of Spartan dictionaries as a JSON response.
    """
    cursor = mysql.connection.cursor()  # Open a database cursor to execute queries
    cursor.execute("SELECT * FROM spartans")  # Execute SQL query to retrieve all Spartans
    spartans = cursor.fetchall()  # Fetch all results as a list of tuples
    cursor.close()  # Close the cursor to release database resources
    if spartans:
        # Convert database tuples into SpartanDTO objects
        spartans_dto = [SpartanDTO.spartan_to_dto(spartan) for spartan in spartans]

        # Convert DTO objects into dictionaries for JSON response
        spartan_dicts = [spartan.__dict__ for spartan in spartans_dto]

        return jsonify(spartan_dicts)  # Return JSON response containing all Spartans

    return jsonify({"message": "There are no Spartans in the database"})

# Route to retrieve a specific Spartan by ID
@spartan_routes.route('/spartans/<int:id>', methods=['GET'])
def get_spartan(id):
    """
    Fetches a specific Spartan by ID from the database and returns it as a JSON response.

    Key concepts:
    - **fetchone()**: Unlike fetchall(), fetchone() retrieves only the first matching record.
    - **Parameterized Query**: Using "%s" instead of string formatting (`f"SELECT ..."`),
      which prevents SQL injection.

    Steps:
    1. Establish a database connection.
    2. Create a cursor object to interact with the database.
    3. Execute a query to fetch the Spartan record with the given ID using a parameterized query.
    4. Retrieve the first matching result.
    5. If a Spartan is found, convert it into a SpartanDTO object.
    6. Convert the SpartanDTO object into a dictionary for JSON serialization.
    7. Return the Spartan dictionary as a JSON response.
    8. If no record is found, return a 404 error response.
    """
    cursor = mysql.connection.cursor()  # Open a database cursor
    cursor.execute("SELECT * FROM spartans WHERE id = %s", (id,))  # Secure query using parameterized values
    spartan = cursor.fetchone()  # Fetch the first (and only) result
    cursor.close()  # Close the cursor to release database resources

    if spartan:
        # Convert the database record into a SpartanDTO object
        spartan_dto = SpartanDTO.spartan_to_dto(spartan)
        return jsonify(spartan_dto.__dict__)  # Convert DTO to dictionary and return JSON response

    return jsonify({"error": "Spartan not found"}), 404  # Return 404 if Spartan does not exist


# Home route that redirects to the Spartans list
@spartan_routes.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to Sparta Global Academy API. "
                   "Adding /spartans at the end of the URL provides you a list of all Spartans in the database, "
                   "and /spartans/{id} will return details of a specific Spartan."
    })