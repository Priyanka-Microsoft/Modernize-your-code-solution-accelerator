import asyncio
import uuid
import pytest
from datetime import datetime
from enum import Enum

# Import the abstract base class and related models/enums.
from common.database.database_base import DatabaseBase
from common.models.api import BatchRecord, FileRecord, ProcessStatus

DatabaseBase.__abstractmethods__ = set()


@pytest.fixture
def db_instance():
    # Instantiate the DatabaseBase directly.
    class ConcreteDatabase(DatabaseBase):
        def create_batch(self, user_id, batch_id):
            pass

        def get_file_logs(self, file_id):
            pass

        def get_batch_files(self, user_id, batch_id):
            pass

        def delete_file_logs(self, file_id):
            pass

        def get_user_batches(self, user_id):
            pass

        def add_file(self, batch_id, file_id, file_name, file_path):
            pass

        def get_batch(self, user_id, batch_id):
            pass

        def get_file(self, file_id):
            pass

        def log_file_status(self, file_id, status, description, log_type):
            pass

        def log_batch_status(self, batch_id, status, file_count):
            pass

        def delete_all(self, user_id):
            pass

        def delete_batch(self, user_id, batch_id):
            pass

        def delete_file(self, user_id, batch_id, file_id):
            pass

        def close(self):
            pass

    return ConcreteDatabase()


def get_dummy_status():
    """
    Try to use a specific ProcessStatus value (e.g. PROCESSING).
    If that member is not available, just return the first member in the enum.
    """
    try:
        return ProcessStatus.PROCESSING
    except AttributeError:
        members = list(ProcessStatus)
        if members:
            return members[0]
        # If the enum is empty, create a dummy one
        DummyStatus = Enum("DummyStatus", {"DUMMY": "dummy"})
        return DummyStatus.DUMMY


@pytest.mark.asyncio
async def test_create_batch(db_instance):
    result = await db_instance.create_batch("user1", uuid.uuid4())
    # Since the method is abstract (and implemented as pass), result is None.
    assert result is None


@pytest.mark.asyncio
async def test_get_file_logs(db_instance):
    result = await db_instance.get_file_logs("file1")
    assert result is None


@pytest.mark.asyncio
async def test_get_batch_files(db_instance):
    result = await db_instance.get_batch_files("user1", "batch1")
    assert result is None


@pytest.mark.asyncio
async def test_delete_file_logs(db_instance):
    result = await db_instance.delete_file_logs("file1")
    assert result is None


@pytest.mark.asyncio
async def test_get_user_batches(db_instance):
    result = await db_instance.get_user_batches("user1")
    assert result is None


@pytest.mark.asyncio
async def test_add_file(db_instance):
    result = await db_instance.add_file(
        uuid.uuid4(), uuid.uuid4(), "test.txt", "/dummy/path"
    )
    assert result is None


@pytest.mark.asyncio
async def test_get_batch(db_instance):
    result = await db_instance.get_batch("user1", "batch1")
    assert result is None


@pytest.mark.asyncio
async def test_get_file(db_instance):
    result = await db_instance.get_file("file1")
    assert result is None


@pytest.mark.asyncio
async def test_log_file_status(db_instance):
    # Use an existing member for file status—here we use COMPLETED.
    result = await db_instance.log_file_status(
        "file1", ProcessStatus.COMPLETED, "desc", "log_type"
    )
    assert result is None


@pytest.mark.asyncio
async def test_log_batch_status(db_instance):
    dummy_status = get_dummy_status()
    result = await db_instance.log_batch_status("batch1", dummy_status, 5)
    assert result is None


@pytest.mark.asyncio
async def test_delete_all(db_instance):
    result = await db_instance.delete_all("user1")
    assert result is None


@pytest.mark.asyncio
async def test_delete_batch(db_instance):
    result = await db_instance.delete_batch("user1", "batch1")
    assert result is None


@pytest.mark.asyncio
async def test_delete_file(db_instance):
    result = await db_instance.delete_file("user1", "batch1", "file1")
    assert result is None


@pytest.mark.asyncio
async def test_close(db_instance):
    result = await db_instance.close()
    assert result is None
