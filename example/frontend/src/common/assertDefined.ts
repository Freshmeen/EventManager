export function assertDefined<T>(arg: T | null | undefined): T {
    if (arg === null || arg === undefined) {
        throw new Error("Argument is null or undefined");
    }
    return arg;
}