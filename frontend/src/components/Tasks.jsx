import { createContext, useEffect, useState } from "react";
import "./styles.css";
import AddTask from "./AddTask";
import { Box, Flex, Stack, Text } from "@chakra-ui/react";

export const TaskContext = createContext({
  tasks: [],
  fetchTasks: () => {},
});

const TodoHelper = ({ task, priority }) => {
  return (
    <Box p={1}>
      <Flex justify="space-around">
        <Text mt={4} as="div">
          {task} {priority ? "!!" : ""}
        </Text>
      </Flex>
    </Box>
  );
};

const Tasks = () => {
  const [tasks, setTasks] = useState([]);
  const fetchTasks = async () => {
    const response = await fetch("http://localhost:8000/tasks");
    const tasks = await response.json();
    console.log(tasks);
    setTasks(tasks);
  };
  useEffect(() => {
    fetchTasks();
  }, []);
  return (
    <TaskContext.Provider value={{ tasks, fetchTasks }}>
      <AddTask />
      <Stack spacing={5} textAlign={"center"}>
        {tasks.map((task) => (
          <TodoHelper
            key={task.id}
            task={task.task}
            priority={task.priority}
            fetchTasks={fetchTasks}
          />
        ))}
      </Stack>
    </TaskContext.Provider>
  );
};
export default Tasks;
