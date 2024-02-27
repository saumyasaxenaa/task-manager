import { useState } from "react";
import { TaskContext } from "./Tasks";
import { useContext } from "react";
import {
  Box,
  Button,
  Checkbox,
  FormControl,
  FormHelperText,
  FormLabel,
  Input,
  InputAddon,
  InputGroup,
} from "@chakra-ui/react";
import { Form, redirect } from "react-router-dom";

const AddTask = () => {
  const [task, setTask] = useState("");
  const [priority, setPriority] = useState(false);
  const { tasks, fetchTasks } = useContext(TaskContext);

  const handleInput = (event) => {
    setTask(event.target.value);
  };

  const handleSubmit = (event) => {
    // console.log(newTask);
    const newTask = {
      task: task,
      priority: priority,
    };
    fetch("http://localhost:8000/tasks", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newTask),
    }).then(fetchTasks);
  };

  return (
    <Box
      maxW={"500px"}
      p={4}
      bg={"blue.200"}
      borderRadius={"12px"}
      display="flex"
      justifyContent="center"
      m={"auto"}
      mt={"10px"}
    >
      <form onSubmit={handleSubmit}>
        <InputGroup size="md">
          <Input
            pr="4.5rem"
            type="text"
            placeholder="Add a todo item"
            aria-label="Add a todo item"
            onChange={handleInput}
          />
        </InputGroup>
        <FormControl display="flex" alignItems="center">
          <Checkbox
            name="priority"
            size="md"
            onChange={() => setPriority(!priority)}
          ></Checkbox>
          <FormLabel ml={"5px"} mt={"5px"}>
            Priority
          </FormLabel>
        </FormControl>
        <Button bgColor="blue.100" type="Submit">
          Submit
        </Button>
      </form>
    </Box>
  );
};
export default AddTask;
