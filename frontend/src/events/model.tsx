import {createContext, PropsWithChildren, useContext, useEffect} from "react";
import {loadEventsAction} from "./mainPage/actions";
import {monthEventsAtom, initialAtom} from "./mainPage/atoms";
import {useAction} from "@reatom/npm-react";

const actions = {
    loadEventsAction,
}

const atoms = {
    eventsAtom: monthEventsAtom,
    initialAtom,
}

const EventsContext = createContext({atoms, actions});

export function EventsModel({children}: PropsWithChildren) {
    return (
        <EventsContext.Provider value={{actions, atoms}}>
            {children}
        </EventsContext.Provider>
    )
}

export function useEventsModel() {
    const context = useContext(EventsContext);
    if (!context) {
        throw new Error("useBooks must be used within a BooksProvider");
    }
    return context;
}