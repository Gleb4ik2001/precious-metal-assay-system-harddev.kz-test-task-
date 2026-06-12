def test_create_sample(client):
    response = client.post(
        "/samples",
        json={
            "sample_code": "AU-001",
            "weight": 15.5,
            "operator": "Ivanov",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["sample_code"] == "AU-001"
    assert data["weight"] == 15.5
    assert data["operator"] == "Ivanov"
    assert data["status"] == "created"


def test_create_sample_with_negative_weight(client):
    response = client.post(
        "/samples",
        json={
            "sample_code": "AU-001",
            "weight": -10,
            "operator": "Ivanov",
        },
    )

    assert response.status_code == 422


def test_get_samples(client):
    client.post(
        "/samples",
        json={
            "sample_code": "AU-001",
            "weight": 10,
            "operator": "Ivanov",
        },
    )

    response = client.get("/samples")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["sample_code"] == "AU-001"


def test_update_sample_status(client):
    create_response = client.post(
        "/samples",
        json={
            "sample_code": "AU-001",
            "weight": 10,
            "operator": "Ivanov",
        },
    )

    sample_id = create_response.json()["id"]

    response = client.patch(
        f"/samples/{sample_id}/status",
        json={
            "status": "approved"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "approved"


def test_summary_report(client):
    client.post(
        "/samples",
        json={
            "sample_code": "AU-001",
            "weight": 10,
            "operator": "Ivanov",
        },
    )

    client.post(
        "/samples",
        json={
            "sample_code": "AU-002",
            "weight": 20,
            "operator": "Petrov",
        },
    )

    response = client.get("/reports/summary")

    assert response.status_code == 200

    data = response.json()

    assert data["total_samples"] == 2
    assert data["average_weight"] == 15
    assert data["min_weight"] == 10
    assert data["max_weight"] == 20
    assert data["status_counts"]["created"] == 2