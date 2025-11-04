import {useAction} from "@reatom/npm-react";
import {Action} from "@reatom/core";

export default function useActions(actions: Action<any>[]): Array<any> {
    if (actions.length == 0) {
        return [];
    }
    const [firstAction, ...otherActions] = actions;
    return [useAction(firstAction), ...useActions(otherActions)]
}