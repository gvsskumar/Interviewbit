import {useState} from 'react'

const getDaysInMonth = (year,month) =>{
    return new Date(year,month+1,0).getDate();
}

const getFirstDay = (year,month)=>{
    return new Date(year,month,1).getDay()
}

const months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
const CalendarComponent = () =>{
 const today = new Date();
 const [currentDate,setCurrentDate] = useState(today)
 const [selectedDate,setSelectedDate] = useState(null)
 const year = currentDate.getFullYear()
 const month = currentDate.getMonth()
 const daysInMonth = getDaysInMonth(year,month)
 const firstDay = getFirstDay(year,month)

 const prevMonth = () =>{
    setCurrentDate(new Date(year,month-1,1))
 }
 const nextMonth = () =>{
    setCurrentDate(new Date(year,month+1,1))
 }

 const dates = []

 for (let i=0;i<firstDay;i++){
    dates.push(null)
 }
 for(let d=1;d<=daysInMonth;d++){
    dates.push(new Date(year,month,d))
 }
 
 const days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
 return(<div className='container' style={{width:'300px',border:'1px solid #959292',padding:'10px'}}>
    <div className='header' style={{display:'flex', justifyContent:'center'}}>
        <button onClick={prevMonth}>prv</button>
        <h4>{months[month]} {year}</h4>
        <button onClick={nextMonth}>nxt</button>
    </div>
    <div className='dayHeader' style={{display:'grid',gridTemplateColumns:'repeat(7, 1fr)'}}>
    {
        days.map((day)=>(<div key={day} >{day}</div>))
    }
    </div>
    <div className='weeklyDates' style={{display:'grid',gridTemplateColumns:'repeat(7, 1fr)'}}>
        {dates.map((date,index)=>(<div key={index} onClick={()=>setSelectedDate(date)}>{date ? date.getDate() : ""}</div>))}
    </div>
 </div>)
}


export default CalendarComponent;