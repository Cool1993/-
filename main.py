"""Main entry point for OpsAny CLI."""
from src.service import compare_host_num, model_handler

def main():
    """Run the main application."""
    try:
        compare_host_num.compare_host_num()
        # model_handler.sync_public_ip_data()
        # model_handler.sync_underutil_data()
    except Exception as e:
        print(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()