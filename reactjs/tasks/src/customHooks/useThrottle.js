import { useState,useEffect,useRef } from "react";

const useThrottle = (value,delay=500) => {
    const [throttleValue,setThrottleValue] = useState(value);
    const lastExecuted = useRef(Date.now())
    useEffect(()=>{
        const handler = setTimeout(()=>{
            const now = Date.now();
            if(now - lastExecuted >= delay){
            setThrottleValue(value)
            lastExecuted.current = now
            }
        return () =>{
            clearTimeout(handler)
        }    
        },delay)
    },[value,delay])
    return throttleValue;
}
export default useThrottle;