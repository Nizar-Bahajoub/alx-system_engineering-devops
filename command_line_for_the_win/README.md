<h1>Command line for the win</h1>

<p> Take Screenshots: First, make sure you have taken screenshots of the completed levels as per the general requirements. Save these screenshots in a local directory on your machine.</p>

<p>Open Terminal or Command Prompt: Open a terminal or command prompt on your local machine. On Windows, you can open the Command Prompt by pressing Windows + R, typing "cmd," and hitting Enter.</p>

<p>Connect to Sandbox Environment: Use the SFTP command-line tool to establish a connection to the sandbox environment. You will need the following information:

Hostname: The hostname or IP address of the sandbox environment.
Username: The username provided for accessing the sandbox environment.
Password: The password associated with the provided username.


The SFTP command to establish a connection will be in the following format:
sftp [username]@[hostname]
</p>

<p> Or just coping the SSH from sandbox and use the Password </p>

<p>Navigate to the Desired Directory: cd alx-system_engineering-devops</p>

<p> Upload Screenshot: put [local_filepath]</p>

<p>Exit the sftp server: exit</p>

<p>Then move to the ssh sever and upload the new directory to Github</p>
