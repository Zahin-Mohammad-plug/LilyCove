import sqlite3

def count_cards(database_path):
    """
    Connects to the database and counts total and distinct cards.
    Args:
        database_path (str): Path to the SQLite database file.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Query total cards
        cursor.execute("SELECT COUNT(*) FROM cards;")
        total_cards = cursor.fetchone()[0]

        # Query distinct cards
        cursor.execute("SELECT COUNT(DISTINCT id) FROM cards;")
        distinct_cards = cursor.fetchone()[0]

        # Print the results
        print(f"Total Cards: {total_cards}")
        print(f"Distinct Cards: {distinct_cards}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

# Path to your SQLite database
database_path = "T:\OneDrive - Carleton University\Coding Porjects\LillyCove\LilyCoveMain\LilyCove\json2Sql\pokemonDb.sqlite"
count_cards(database_path)
