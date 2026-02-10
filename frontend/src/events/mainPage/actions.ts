import {EventsApi} from "../../api/generated";
import {action} from "@reatom/core";
import {monthEventsAtom, initialAtom} from "./atoms";
import {remapEventsFromApi} from "../remap";


const api = new EventsApi();

export const loadEventsAction = action((ctx) => {
    api.listEventsByTimeIntervalApiV1EventsTimeIntervalPost({
        since: Math.floor(Number(new Date().getTime() / 1000)),
        until: Math.floor(new Date(new Date().getTime() + 30 * 24 * 60 * 60 * 1000).getTime() / 1000)
    })
        .then(events => {
            monthEventsAtom(ctx, remapEventsFromApi(events.data));
            initialAtom(ctx, true);
        })
});