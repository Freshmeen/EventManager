export class ToastException extends Error {
    message: string;
    type: "success" | "error" | "info";

    constructor(message: string, type: "success" | "error" | "info" = "info") {
        super(message);
        this.message = message;
        this.type = type;
        this.name = "ToastException";
    }
}
