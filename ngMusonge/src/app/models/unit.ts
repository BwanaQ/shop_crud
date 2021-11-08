export interface Unit {
  id: number;
  name: string;
  rent: number;
  occupied: boolean;
  image: string;
  location: string;
  date_added: string;
  likes: number[];
  owner: number;
}
