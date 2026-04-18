import { useEffect } from "react";

function UserListFC() {
  useEffect(() => {
    const controller = new AbortController();

    fetch("https://jsonplaceholder.typicode.com/users", {
      signal: controller.signal
    })
      .then(res => res.json())
      .then(data => console.log(data))
      .catch(err => {
        if (err.name !== "AbortError") console.error(err);
      });

    return () => {
      controller.abort(); // cleanup (like componentWillUnmount)
    };
  }, []);

  return <div>Users</div>;
}
export default UserListFC