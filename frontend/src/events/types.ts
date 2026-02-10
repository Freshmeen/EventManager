export type EventData = {
    eventId?: string;
    name: string;
    description?: string;
    acceptationStatus?: string;
    startsAt: Date;
    endsAt: Date;
    maxVolunteers?: number;
    minVolunteers?: number;
    imagePath?: string;
}