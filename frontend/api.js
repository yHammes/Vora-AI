const BASE_URL = "https://vora-ai-back-end.vercel.app";

async function request(endpoint, body) {
  const url = `${BASE_URL}/${endpoint}`;
  console.log(`[${endpoint}] Request started`, { url, ...body });

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    const data = await response.text();
    const level = response.ok ? "log" : "warn";
    console[level](
      `[${endpoint}] Request ${response.ok ? "successful" : "failed"}`,
      { status: response.status, data },
    );

    return { status: response.status, data };
  } catch (error) {
    console.error(`[${endpoint}] Unexpected error`, {
      error: error.message,
      stack: error.stack,
    });
    throw error;
  }
}

async function send_message(question, user_id, session_id) {
  try {
    if (!user_id) {
      window.location.href = "index.html";
      return { status: 401, detail: "Usuário não autenticado" };
    }

    const response = await request("send_message", {
      user_id,
      session_id,
      question,
    });

    return response;
  } catch (error) {
    console.error("Erro em send_message:", error);

    return {
      status: 500,
      detail: error.message || "Erro ao enviar mensagem",
    };
  }
}

async function register(user_name, password) {
  try {
    const response = await request("register", {
      user_name,
      password,
    });

    return response;
  } catch (error) {
    console.error("Erro em register:", error);

    return {
      status: 500,
      detail: error.message || "Erro ao registrar usuário",
    };
  }
}

async function login(user_name, password) {
  try {
    const response = await request("login", {
      user_name,
      password,
    });

    return response;
  } catch (error) {
    console.error("Erro em login:", error);

    return {
      status: 500,
      detail: error.message || "Erro ao fazer login",
    };
  }
}
