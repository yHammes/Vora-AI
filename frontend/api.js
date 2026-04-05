async function send_message(question, user_id, session_id) {
  const endpoint = "https://vora-ai-back-end.vercel.app/send_message";
  console.log("[send_message] Request started", {
    endpoint,
    user_id,
    session_id,
    question,
  });

  try {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id, session_id, question }),
    });

    const data = await response.text();

    if (!response.ok) {
      console.warn("[send_message] Request failed", {
        status: response.status,
        data,
      });
      return { status: response.status, data };
    }

    console.log("[send_message] Request successful", {
      status: response.status,
      data,
    });
    return { status: response.status, data };
  } catch (error) {
    console.error("[send_message] Unexpected error", {
      error: error.message,
      stack: error.stack,
    });
    throw error;
  }
}

async function register(user_name, password) {
  const endpoint = "https://vora-ai-back-end.vercel.app/register";
  console.log("[register] Request started", { endpoint, user_name });

  try {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_name, password }),
    });

    const data = await response.text();

    if (!response.ok) {
      console.warn("[register] Request failed", {
        status: response.status,
        data,
      });
      return { status: response.status, data };
    }

    console.log("[register] Request successful", {
      status: response.status,
      data,
    });
    return { status: response.status, data };
  } catch (error) {
    console.error("[register] Unexpected error", {
      error: error.message,
      stack: error.stack,
    });
    throw error;
  }
}

async function login(user_name, password) {
  const endpoint = "https://vora-ai-back-end.vercel.app/login";
  console.log("[login] Request started", { endpoint, user_name });
}
