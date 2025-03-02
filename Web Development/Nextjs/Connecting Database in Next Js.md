Connection using mongoose 

```
import mongoose from "mongoose";

type ConnectionObject = {
	isConnected?: number
}

const connection: ConnectionObject = {}

async function dbConnect(): Promise<void> {
	if (connection.isConnected){
		console.log("Already Connected to Database");
		return;
	}

	try{
		const db = await mongoose.connect(process.env.MONGODB_URI || '', {});
		console.log(db);

		connection.isConnected = db.connections[0].readyState;
		console.log("Database Connection Failed!!!", error);
	} catch (error) {
		console.log("Connection Failed!!");
		process.exit(1);
	}
}

export default dbConnect;
```