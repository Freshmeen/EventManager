import { action, atom } from "@reatom/core"
import type { PopupType, UserType } from "./types"

const inputAtom = atom<string>("")
const popupTypeAtom = atom<PopupType>(null)
const userTypeAtom = atom<UserType>(null)

const inputHandleChange = action((ctx, event: React.ChangeEvent<HTMLInputElement>) => {
    inputAtom(ctx, event.target.value)
})

const callPopup = action((ctx, popupType: PopupType) => {
    popupTypeAtom(ctx, popupType)
})

const changeUserType = action((ctx, newType: UserType) => {
    userTypeAtom(ctx, newType)
})

export {
    inputAtom,
    popupTypeAtom,
    userTypeAtom,
    inputHandleChange,
    callPopup,
    changeUserType
}