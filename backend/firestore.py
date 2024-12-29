import firebase_admin
from firebase_admin import credentials, firestore
import logging

# Initialize Firestore
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Set up logging
logger = logging.getLogger(__name__)

def get_afroverb_data(collection_name):
    try:
        collection_ref = db.collection(collection_name)
        docs = collection_ref.stream()
        data = [doc.to_dict() for doc in docs]
        return data
    except Exception as e:
        logger.error(f"Error getting data from Firestore: {e}")
        return None

def sync_data_to_firestore(collection_name, data):
    try:
        collection_ref = db.collection(collection_name)
        for item in data:
            doc_ref = collection_ref.document(item['id'])
            doc_ref.set(item)
        logger.info(f"Data synchronized to Firestore collection: {collection_name}")
    except Exception as e:
        logger.error(f"Error syncing data to Firestore: {e}")

def add_document(collection_name, data):
    try:
        collection_ref = db.collection(collection_name)
        doc_ref = collection_ref.document(data['id'])
        doc_ref.set(data)
        logger.info(f"Document added to Firestore collection: {collection_name}")
    except Exception as e:
        handle_firestore_error(e)

def get_document(collection_name, document_id):
    try:
        doc = db.collection(collection_name).document(document_id).get()
        if doc.exists:
            logger.info(f"Document retrieved from {collection_name} collection.")
            return doc.to_dict()
        else:
            logger.warning(f"Document {document_id} not found in {collection_name} collection.")
            return None
    except Exception as e:
        logger.error(f"Error retrieving document from {collection_name} collection: {e}")
        return None

def update_document(collection_name, document_id, update_data):
    try:
        db.collection(collection_name).document(document_id).update(update_data)
        logger.info(f"Document {document_id} updated in {collection_name} collection.")
    except Exception as e:
        logger.error(f"Error updating document {document_id} in {collection_name} collection: {e}")

def delete_document(collection_name, document_id):
    try:
        db.collection(collection_name).document(document_id).delete()
        logger.info(f"Document {document_id} deleted from {collection_name} collection.")
    except Exception as e:
        logger.error(f"Error deleting document {document_id} from {collection_name} collection: {e}")

def handle_firestore_error(e):
    logger.error(f"Firestore operation failed: {e}")
