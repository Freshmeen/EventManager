import {PropsWithChildren} from "react";
import styles from "./Base.module.css";
import SearchField from "./SearchField";
import "./Base.css"

function Base(props: PropsWithChildren) {
    return (
        <div className={styles.base}>
            <header className={styles.header}>
                <h1>EVENT MANAGER</h1>
                <SearchField
                    onSearch={(query) => {
                        console.log("Search: " + query);
                    }}
                    onChange={(query) => {
                        console.log("Change: " + query);
                    }}
                />
                <div className={styles.authButton}>
                    <span>Выйти</span>
                    <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M8.33341 36.0281C7.15758 36.0281 6.15994 35.6182 5.34049 34.7985C4.52105 33.9791 4.11133 32.9814 4.11133 31.8056V8.3335C4.11133 7.15016 4.52105 6.146 5.34049 5.321C6.15994 4.496 7.15758 4.0835 8.33341 4.0835H20.278V8.3335H8.33341V31.8056H20.278V36.0281H8.33341ZM26.903 29.1181L23.8959 26.1806L27.868 22.1806H14.8055V17.9585H27.8126L23.8405 13.9585L26.8472 11.0072L35.9167 20.0906L26.903 29.1181Z"
                            fill="#FA5D21"/>
                    </svg>
                </div>
            </header>
            <main className={styles.main}>
                {props.children}
            </main>
        </div>
    )
}

export default Base;