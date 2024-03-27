import axios from "axios";

const SERVER_URL: string = `http://${document.location.hostname}:4000/`;

export default class AxiosRest {
  static async Post<T, D>(url: string, data: D): Promise<T> {
    const response = await axios.post(SERVER_URL + url, data);
    return response.data;
  }

  static async Get<T>(url: string): Promise<T> {
    const response = await axios.get(SERVER_URL + url);
    return response.data;
  }
}
