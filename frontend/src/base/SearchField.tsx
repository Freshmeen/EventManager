import styles from './SearchField.module.css';
import {useRef} from "react";


type Props = {
    placeholder?: string
    onSearch?: (query: string) => void
    onChange?: (query: string) => void
}

function SearchField({ placeholder, onSearch, onChange }: Props) {
    const input = useRef<HTMLInputElement>(null);
    if (!onSearch) {
        onSearch = () => {};
    }
    if (!onChange) {
        onChange = () => {};
    }

    return (
        <div className={styles.field}>
            <input
                className={styles.input}
                type="text"
                placeholder={placeholder || 'Поиск...'}
                ref={input}
                onChange={() => {
                    if (!input.current) return;
                    onChange(input.current.value);
                }}
            />
            <svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" onClick={() => {
                if (!input.current) return;
                onSearch(input.current.value);
            }} className={styles.icon}>
                <path d="M19.6829 21.6206L13.1084 15.0624C12.6331 15.4337 12.0707 15.7203 11.4212 15.9221C10.7717 16.1239 10.0755 16.2249 9.33266 16.2249C7.42916 16.2249 5.81516 15.5626 4.49066 14.2381C3.16616 12.9136 2.50391 11.3122 2.50391 9.43385C2.50391 7.55568 3.16457 5.9541 4.48591 4.6291C5.80741 3.3041 7.41157 2.6416 9.29841 2.6416C11.1854 2.6416 12.7886 3.30419 14.1079 4.62935C15.4274 5.95435 16.0872 7.55735 16.0872 9.43835C16.0872 10.1794 15.9857 10.8659 15.7829 11.4979C15.5802 12.1297 15.2886 12.7096 14.9079 13.2376L21.5079 19.8041L19.6829 21.6206ZM9.31816 13.6916C10.5087 13.6916 11.5122 13.2794 12.3289 12.4551C13.1456 11.6308 13.5539 10.6231 13.5539 9.4321C13.5539 8.2411 13.1447 7.23385 12.3264 6.41035C11.5081 5.58668 10.5039 5.17485 9.31391 5.17485C8.11457 5.17485 7.10199 5.58702 6.27616 6.41135C5.45016 7.23552 5.03716 8.2431 5.03716 9.4341C5.03716 10.6251 5.44949 11.6324 6.27416 12.4561C7.09899 13.2798 8.11366 13.6916 9.31816 13.6916Z"/>
            </svg>
        </div>
    );
}

export default SearchField;