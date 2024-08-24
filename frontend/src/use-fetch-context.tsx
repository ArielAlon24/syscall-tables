import React, {
  createContext,
  useContext,
  useEffect,
  useState,
  ReactNode,
  FC,
} from "react";

const FetchContext = createContext<
  | {
      data: any;
      error: string | null;
    }
  | undefined
>(undefined);

interface FetchProviderProps<T> {
  url: string;
  children: ReactNode;
}

export const FetchProvider = <T,>({ url, children }: FetchProviderProps<T>) => {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch(url)
      .then((response) => response.json())
      .then((data: T) => setData(data))
      .catch((error) => setError(`Error fetching JSON: ${error}`));
  }, [url]);

  return (
    <FetchContext.Provider value={{ data, error }}>
      {children}
    </FetchContext.Provider>
  );
};

export function useFetchContext<T>() {
  const context = useContext(FetchContext);
  if (context === undefined) {
    throw new Error("useFetchContext must be used within a FetchProvider");
  }
  return context as { data: T | null; error: string | null };
}
