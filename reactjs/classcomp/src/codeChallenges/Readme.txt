https://chatgpt.com/g/g-p-69b23caf1e54819195a4202e61a8d8cd-react/c/69d3f579-ce98-83e8-a72e-0058e4f9c0f0

AbortController is used to cancel an ongoing API request (fetch call)
  controller = new AbortController();

  Create a controller
  Attach it to fetch:

  fetch(url, { signal: this.controller.signal })
  Cancel request when component unmounts:

  this.controller.abort();
👉 This stops the API call immediately

🔄 Real-Life Analogy (Easy to remember)
API request = 🚕 Taxi ride
Component = 🧍 Passenger
AbortController = ❌ Cancel button
=======================================
