## Introduction

Redux is a predictable state container for JavaScript applications, commonly used with React. It helps manage the application's state efficiently and ensures consistency across components.

---

## Core Principles of Redux

1. **Single Source of Truth**: The entire application state is stored in a single JavaScript object.
    
2. **State is Read-Only**: The state can only be changed by dispatching actions.
    
3. **Changes are Made with Pure Functions**: Reducers specify how the state changes in response to actions.
    

---

## Key Components

### 1. Store

The store holds the application state and is created using `createStore` (or `configureStore` in Redux Toolkit).

```javascript
import { createStore } from 'redux';
import rootReducer from './reducers';

const store = createStore(rootReducer);
```

### 2. Actions

Actions are objects that describe what should happen in the application.

```javascript
const increment = () => ({
  type: 'INCREMENT'
});
```

### 3. Reducers

Reducers define how the state should change in response to actions.

```javascript
const counterReducer = (state = 0, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return state + 1;
    case 'DECREMENT':
      return state - 1;
    default:
      return state;
  }
};
```

### 4. Dispatch

Dispatching an action updates the state.

```javascript
store.dispatch(increment());
```

---

## Redux Toolkit (RTK)

Redux Toolkit simplifies Redux usage with utilities like `createSlice` and `configureStore`.

```javascript
import { createSlice, configureStore } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: 0,
  reducers: {
    increment: (state) => state + 1,
    decrement: (state) => state - 1,
  },
});

const store = configureStore({ reducer: counterSlice.reducer });
export const { increment, decrement } = counterSlice.actions;
```

---

## When to Use Redux?

- When multiple components need access to shared state.
    
- When the application state is complex and needs predictable updates.
    
- When debugging and time-travel debugging are essential.
    

---

## Conclusion

Redux is a powerful state management tool for complex applications. While it introduces some boilerplate, Redux Toolkit significantly reduces complexity. Understanding its principles helps in managing application state efficiently.

---

## References

- [Redux Official Docs](https://redux.js.org/)
    
- [Redux Toolkit](https://redux-toolkit.js.org/)