import {EventsModel, useEventsModel} from "../model";
import {useAction} from "@reatom/npm-react";
import useAtoms from "../../common/hooks/useAtoms";
import {useEffect} from "react";
import Events from "../view/Events";
import styles from "./MainPage.module.css";
import EventComponent from "../view/Event";
import { EventData } from "../types";

export default function MainPage() {
    const {actions, atoms} = useEventsModel();
    const loadEvents = useAction(actions.loadEventsAction)
    const [events, initial] = useAtoms([atoms.eventsAtom, atoms.initialAtom])

    useEffect(() => {
        loadEvents();
    }, []);

    const sortedEvents = events.sort((a: EventData, b: EventData) => a.startsAt.getTime() - b.startsAt.getTime())

    return (
        <EventsModel>
            <div className={styles.container}>
                <h1 className={styles.title}>Ближайшие события</h1>

                {initial
                    ? <>
                        <EventComponent type="preview" event={sortedEvents[0]}/>
                        <Events events={sortedEvents.slice(1)}/>
                    </>
                    : <>
                        <EventComponent type="preview"/>
                        <Events skeleton={10}/>
                    </>
                }
            </div>
        </EventsModel>
    )
}