from models.model_1 import get_connection

def test_connection():
    conn = get_connection()
    if conn:
        print("Connection successful!")
    else:
        print("Connection failed.")
    conn.close()

if __name__ == '__main__':
    test_connection()