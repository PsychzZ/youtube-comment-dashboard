import { useState, createContext, useEffect } from "react";
import { CommentsStats, VideoUrl } from "../types/types";
import { post } from "../utils/AxiosRest";

export const VideoContext = createContext<ReturnType<typeof useLink>>({
  commentStats: undefined,
  submitVideoUrl: () => {},
  videoUrl: { videoUrl: "" },
  setVideoUrl: () => {},
  notValidUrl: false,
  setNotValidUrl: () => {},
  open: false,
  setOpen: () => {},
  loading: false,
  setLoading: () => {},
});

export function useLink() {
  const [commentStats, setCommentStats] = useState<CommentsStats>();
  const [videoUrl, setVideoUrl] = useState<VideoUrl>({ videoUrl: "" });
  const [notValidUrl, setNotValidUrl] = useState<boolean>(false);
  const [open, setOpen] = useState<boolean>(true);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    if (notValidUrl) {
      setOpen(true);
    }
  }, [videoUrl, notValidUrl]);

  function submitVideoUrl(videoUrl: VideoUrl) {
    console.log(videoUrl);
    post<CommentsStats, VideoUrl>("videos", videoUrl)
      .then((res) => {
        setCommentStats(res);
        setLoading(false);
      })
      .catch(() => {
        setNotValidUrl(true);
        setLoading(true);
      });
  }

  return {
    commentStats,
    submitVideoUrl,
    videoUrl,
    setVideoUrl,
    notValidUrl,
    setNotValidUrl,
    open,
    setOpen,
    loading,
    setLoading,
  };
}
