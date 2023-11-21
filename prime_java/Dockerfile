#Use the official OpenJDK image as a parent image
FROM openjdk:latest

# Set the working directory to /app
WORKDIR /app

# COpy the current dic content into container /app
COPY .  /app

# Compile the Java code
RUN javac prime_num.java

# Run the program when the container starts 
CMD ["java" , "prime_num"]

