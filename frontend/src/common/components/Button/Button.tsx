import React from "react";
import styles from "./Button.module.css"

type ButtonType = "filled" | "outlined" | "inactive";

type ButtonProps = {
    onClick?: () => void;
    type?: "filled" | "outlined" | "inactive",
    icon?: ButtonIcon;
    text: string;
} | {
    type: "skeleton",
    text: string;
}

type ButtonIcon = ({
    component: React.ReactNode;
} | {
    name: string;
}) & {
    position: "left" | "right";
}

const types = {
    filled: {
        backgroundColor: "var(--accent-color)",
        color: "var(--white-color)"
    },
    outlined: {
        backgroundColor: "var(--white-color)",
        color: "var(--accent-color)",
        border: "1px solid var(--accent-color)"
    },
    inactive: {
        backgroundColor: "var(--light-grey-color)",
        color: "var(--white-color)"
    },
    skeleton: {
        backgroundColor: "var(--skeleton-color)",
        color: "var(--skeleton-color)"
    }
};

export default function Button(props: ButtonProps) {
    const type = props.type || "filled";
    const style = types[type];

    if (props.type == "skeleton") {
        return (
            <button className={styles.button} style={style} disabled>
                <span>{props.text}</span>
            </button>
        );
    }

    return (
        <button onClick={props.onClick} className={styles.button} style={style} disabled={props.type == "inactive"}>
            {<span>{props.text}</span>}
        </button>
    );
}