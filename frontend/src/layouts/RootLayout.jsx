import { Grid, GridItem } from "@chakra-ui/react";

const RootLayout = () => {
  return (
    <Grid templateColumns={"repeat(6, 1fr)"} bg={"gray.50"}>
      <GridItem
        as={"aside"}
        colSpan={{ base: 6, lg: 2, xl: 1 }}
        bg={"purple.400"}
        minH={{ lg: "100vh" }}
        p={{ base: "20px", lg: "30px" }}
      >
        TEST
      </GridItem>
    </Grid>
  );
};
export default RootLayout;
