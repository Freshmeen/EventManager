import styles from "./Button.module.css";
import {PropsWithChildren} from "react";

type Props = PropsWithChildren & {
    onClick: () => void;
    type?: "negative" | "positive" | "default";
};

const buttonTypes = {
    negative: styles.negative,
    positive: styles.positive,
    default: styles.default,
};

export default function Button({onClick, children, type = "default"}: Props) {
    return (
        <button className={`${styles.button} ${buttonTypes[type]}`} onClick={onClick}>
            {children}
        </button>
    )
}