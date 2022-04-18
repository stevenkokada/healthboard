import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

interface UnreadMesssagesDate {
  messages: Array<any>;
}

function App() {
  const [unreadMessages, setUnreadMessages] = useState(
    {} as UnreadMesssagesDate
  );
  useEffect(() => {
    // DJANGO RESOURCES NEED TRAILING SLASH FOR SOME GODDAMN REASON
    // PROD_BACKEND - LEAVE THIS ENABLED BY DEFAULT SINCE THIS GETS SERVED until we flag on env vars
    fetch("https://okada-api.com/unread_messages/")
      .then((response) => response.json())
      .then((data) => setUnreadMessages({ messages: data.results }));
    // LOCAL_BACKEND
    // fetch("http://127.0.0.1:8000/unread_messages/")
    //   .then((response) => response.json())
    //   .then((data) => setUnreadMessages({ messages: data.results }));
  });

  if (unreadMessages && unreadMessages?.messages?.length == 0) {
    return <>No Message Data</>;
  }

  const messages = unreadMessages?.messages?.map((message) => {
    return (
      <>
        {message.sender_name}
        {message.scraper_run_time}
      </>
    );
  });

  return <>{messages}</>;
}

export default App;
