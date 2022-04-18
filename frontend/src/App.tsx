import { useEffect, useState } from "react";
import "./App.css";

interface UnreadMesssages {
  count: number;
  messages: Array<any>;
}

function App() {
  const [unreadMessages, setUnreadMessages] = useState({} as UnreadMesssages);
  useEffect(() => {
    // DJANGO RESOURCES NEED TRAILING SLASH FOR SOME GODDAMN REASON
    // PROD_BACKEND - LEAVE THIS ENABLED BY DEFAULT SINCE THIS GETS SERVED until we flag on env vars
    fetch("https://okada-api.com/unread_messages/")
      .then((response) => response.json())
      .then((data) =>
        setUnreadMessages({ count: data.count, messages: data.results })
      );
    // LOCAL_BACKEND
    // fetch("http://127.0.0.1:8000/unread_messages/")
    //   .then((response) => response.json())
    //   .then((data) =>
    //     setUnreadMessages({ count: data.count, messages: data.results })
    //   );
  });

  if (unreadMessages && unreadMessages.count == 0) {
    return <>No Message Data</>;
  }

  const messages = unreadMessages?.messages?.map((message) => {
    return (
      <div>
        {`${message.sender_name}` + " " + `${message.scraper_run_time}`}
      </div>
    );
  });
  // console.log(unreadMessages);

  return <>{messages}</>;
}

export default App;
