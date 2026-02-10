import {EventData} from "../types";
import EventComponent from "./Event";

import styles from "./Events.module.css";

type Props = {
    events: EventData[];
} | {
    skeleton: number;
};

export default function Events(props: Props) {
    if ("skeleton" in props) {
        const skeleton = props.skeleton;
        if (skeleton <= 0) {
            throw new Error("skeleton must be greater than 0");
        }
        return <div className={styles.events}>
            {Array.from({length: skeleton}, (_, i) => (
                <EventComponent key={i}/>
            ))}
        </div>
    }
    const events = props.events;
    return (
        <div className={styles.events}>
            {events.map((event) => (
                <EventComponent event={event}/>
            ))}
        </div>
    );
}