import axios from "axios";

const SERVER_URL: string = `http://${document.location.hostname}:4000/`;

export async function post<T, D>(url: string, data: D) {
  const response = await axios.post<T>(SERVER_URL + url, data);
  return response.data;
}

export async function get<T>(url: string) {
  const response = await axios.get<T>(SERVER_URL + url);
  return response.data;
}
