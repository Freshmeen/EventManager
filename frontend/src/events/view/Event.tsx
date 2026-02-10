import {EventData} from '../types';
import styles from './Event.module.css';
import {format} from "date-fns"
import Button from "../../common/components/Button/Button";
import {CSSProperties} from "react";

type Props = {
    event?: EventData;
    type?: 'default' | 'preview'
}

export default function EventComponent(props: Props) {
    if (props.type === undefined){
        props.type = 'default';
    }
    return (
        props.type === 'default'
                ? <DefaultEventComponent {...props}/>
                : <PreviewEventComponent {...props}/>
    );
}

function DefaultEventComponent(props: Props) {
    return (
        <div className={`${styles.event} ${props.event ? '' : styles.skeleton}`}>
            {
                props.event
                    ? <img src={props.event.imagePath} alt={props.event.name} className={styles.image}/>
                    : <div className={`${styles.image}`}/>
            }
            <div className={styles.info}>
                <div className={styles.eventInfo}>
                    <h2 className={styles.name}>{props.event?.name || ''}</h2>
                    <p className={styles.description}>{props.event?.description || ''}</p>
                </div>
                <div className={styles.organizationInfo}>
                    {props.event?.startsAt
                        ? <span className={styles.startsAt}>{format(props.event.startsAt, 'dd.MM.yyyy HH:mm')}</span>
                        : <span className={styles.startsAt}></span>}
                    <Button type={props.event ? 'filled' : 'skeleton'} text="Участвовать"/>
                </div>
            </div>
        </div>
    );
}

const previewBackgroundGradient: CSSProperties = {
    backgroundImage: `linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1))`
};

function PreviewEventComponent(props: Props) {
    return (
        <div className={`${styles.eventPreview} ${props.event ? '' : styles.skeleton}`} style={{
            background: `${previewBackgroundGradient.backgroundImage}, url(${props.event?.imagePath}) no-repeat center center / cover`
        }}>
            <h2 className={styles.name}>{props.event?.name || ''}</h2>
            <p className={styles.description}>{props.event?.description || ''}</p>
            <div className={styles.bottomPanel}>
                <div className={styles.organizationInfo}>
                    <span className={styles.at}>{format(props.event?.startsAt || 0, 'dd.MM.yyyy HH:mm')} — {format(props.event?.endsAt || 0, 'dd.MM.yyyy HH:mm')}</span>
                </div>
                <Button type={props.event ? 'filled' : 'skeleton'} text="Участвовать"/>
            </div>
        </div>
    );
}