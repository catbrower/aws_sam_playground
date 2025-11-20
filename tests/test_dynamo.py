# tests/test_process_object.py

from unittest.mock import MagicMock, patch
from my_lambda.handler import process_object, serialize_my_object


def test_process_object_writes_to_dynamodb():
    # ------------------------------------------------------------
    # Arrange
    # ------------------------------------------------------------
    input_obj = {
        "id": "abc123",
        "value": "hello-world",
        "count": 5
    }

    expected_item = serialize_my_object(input_obj)

    # Create a mock DynamoDB client
    mock_ddb = MagicMock()

    # Patch ONLY the get_dynamodb() call inside write_to_table(), 
    # but we will pass the client directly so boto3 is never called.
    with patch("my_lambda.db.get_dynamodb", return_value=mock_ddb):

        # ------------------------------------------------------------
        # Act
        # ------------------------------------------------------------
        returned_item = process_object(input_obj, dynamodb_client=mock_ddb)

    # ------------------------------------------------------------
    # Assert
    # ------------------------------------------------------------
    # ensure serialization matches expectation
    assert returned_item == expected_item

    # ensure DynamoDB was called correctly
    mock_ddb.put_item.assert_called_once_with(
        TableName="MyTargetTable",
        Item=expected_item
    )

    # Ensure no extra calls
    assert mock_ddb.method_calls == [
        ("put_item", (), {"TableName": "MyTargetTable", "Item": expected_item})
    ]
