import {EventResponse} from "../api/generated";
import {EventData} from "./types";

export function remapEventsFromApi(events: EventResponse[]): EventData[] {
    return events.map(event => {
        return {
            eventId: event.event_id,
            name: event.name,
            description: event.description ?? undefined,
            startsAt: new Date(parseInt(event.starts_at) * 1000),
            endsAt: new Date(parseInt(event.ends_at) * 1000),
            maxVolunteers: event.max_volunteers ?? undefined,
            minVolunteers: event.min_volunteers ?? undefined,
            imagePath: event.image_path ?? undefined
        }
    })
}