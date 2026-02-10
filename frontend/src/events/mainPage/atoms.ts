import {atom} from "@reatom/core";
import {EventData} from "../types";

export const monthEventsAtom = atom<EventData[]>([]);
export const initialAtom = atom<boolean>(false);