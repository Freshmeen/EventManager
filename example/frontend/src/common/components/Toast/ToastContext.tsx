import {createContext, PropsWithChildren, useContext, useEffect, useState} from "react";
import {ToastException} from "./ToastException";
import styles from "./Toast.module.css";

type ToastContextType = {
    showToast: (message: string, type?: "success" | "error" | "info") => void;
};

const ToastContext = createContext<ToastContextType | undefined>(undefined);

export const useToast = (): ToastContextType => {
    const context = useContext(ToastContext);
    if (!context) {
        throw new Error("useToast must be used within a ToastProvider");
    }
    return context;
};

export function ToastProvider({ children }: PropsWithChildren) {
    const [toasts, setToasts] = useState<{ message: string; type: string }[]>([]);

    const showToast = (message: string, type: "success" | "error" | "info" = "info") => {
        setToasts((prev) => [...prev, { message, type }]);
        setTimeout(() => {
            setToasts((prev) => prev.slice(1));
        }, 3000);
    };

    useEffect(() => {
        const toastExceptionListener = (event: PromiseRejectionEvent) => {
            if (event.reason instanceof ToastException) {
                showToast(event.reason.message, event.reason.type);
                event.preventDefault()
            }
        }

        window.addEventListener("unhandledrejection", toastExceptionListener);

        return () => {
            window.removeEventListener("unhandledrejection", toastExceptionListener);
        };
    }, []);

    return (
        <ToastContext.Provider value={{ showToast }}>
            {children}
            {toasts.length > 0 && (
                <div className={styles.toastContainer}>
                    {toasts.map((toast, index) => (
                        <div key={index} className={`${styles.toast} ${(() => {
                            switch (toast.type) {
                                case "info":
                                    return styles.info;
                                case "error":
                                    return styles.error;
                                case "success":
                                    return styles.success;
                            }
                        })()}`}>
                            {toast.message}
                        </div>
                    ))}
                </div>
            )}
        </ToastContext.Provider>
    );
};
