import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio

class TestEventMembers:

    async def test_add_member_success(self, client: AsyncClient, create_user_fixture, create_event_fixture):
        user_id = create_user_fixture["user_id"]
        event_id = create_event_fixture["event_id"]

        payload = {
            "user_id": user_id,
            "event_id": event_id,
            "role": "volunteer",
            "comment": "Ready to help!"
        }

        response = await client.post("/api/v1/event-members/", json=payload)

        assert response.status_code == 201
        data = response.json()
        assert data["user_id"] == user_id
        assert data["event_id"] == event_id
        assert data["role"] == "volunteer"
        assert data["comment"] == "Ready to help!"
        assert data["acceptation_status"] == "PENDING"

    async def test_add_member_duplicate(self, client: AsyncClient, create_user_fixture, create_event_fixture):
        user_id = create_user_fixture["user_id"]
        event_id = create_event_fixture["event_id"]

        payload = {"user_id": user_id, "event_id": event_id, "role": "volunteer"}

        await client.post("/api/v1/event-members/", json=payload)

        response = await client.post("/api/v1/event-members/", json=payload)
        assert response.status_code == 400
        assert "already a member" in response.json()["detail"]

    async def test_get_members_by_event(self, client: AsyncClient, create_user_fixture, create_event_fixture):
        user_id = create_user_fixture["user_id"]
        event_id = create_event_fixture["event_id"]

        await client.post("/api/v1/event-members/", json={
            "user_id": user_id, "event_id": event_id, "role": "organizer"
        })

        response = await client.get(f"/api/v1/event-members/event/{event_id}")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["user_id"] == user_id
        assert data[0]["role"] == "organizer"

    async def test_get_specific_membership(self, client: AsyncClient, create_user_fixture, create_event_fixture):
        user_id = create_user_fixture["user_id"]
        event_id = create_event_fixture["event_id"]

        await client.post("/api/v1/event-members/", json={
            "user_id": user_id, "event_id": event_id
        })

        response = await client.get(f"/api/v1/event-members/{event_id}/{user_id}")
        assert response.status_code == 200
        assert response.json()["user_id"] == user_id

    async def test_update_member(self, client: AsyncClient, create_user_fixture, create_event_fixture):
        user_id = create_user_fixture["user_id"]
        event_id = create_event_fixture["event_id"]

        await client.post("/api/v1/event-members/", json={
            "user_id": user_id, "event_id": event_id, "role": "volunteer"
        })

        update_payload = {
            "role": "organizer",
            "acceptation_status": "ACCEPTED"
        }

        response = await client.patch(f"/api/v1/event-members/{event_id}/{user_id}", json=update_payload)
        assert response.status_code == 204  # No content

        get_response = await client.get(f"/api/v1/event-members/{event_id}/{user_id}")
        data = get_response.json()
        assert data["role"] == "organizer"
        assert data["acceptation_status"] == "ACCEPTED"

    async def test_delete_member(self, client: AsyncClient, create_user_fixture, create_event_fixture):
        user_id = create_user_fixture["user_id"]
        event_id = create_event_fixture["event_id"]

        await client.post("/api/v1/event-members/", json={
            "user_id": user_id, "event_id": event_id
        })

        del_response = await client.delete(f"/api/v1/event-members/{event_id}/{user_id}")
        assert del_response.status_code == 204

        get_response = await client.get(f"/api/v1/event-members/{event_id}/{user_id}")
        assert get_response.status_code == 404

    async def test_not_found(self, client: AsyncClient, create_event_fixture):
        event_id = create_event_fixture["event_id"]
        fake_user_id = "00000000-0000-0000-0000-000000000000"

        response = await client.get(f"/api/v1/event-members/{event_id}/{fake_user_id}")
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]