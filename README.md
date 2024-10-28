# EaglerCux
> [!IMPORTANT]
> Follow the step by step to use EaglerCux

## Watch Zepr's video on EaglerCux to learn how to setup your server!

### Setup
Make your server run for 4 hours straight: [Open](https://github.com/settings/codespaces)<br>
Create your server: [Open](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=879700044&skip_quickstart=true&machine=standardLinux32gb&geo=EuropeWest)


## Installing Java
```bash
sudo apt update -y & sudo apt full-upgrade -y & sudo apt autoremove -y & sudo apt auto-clean -y
```
```bash
sdk install java 17.0.9-amzn
```
> write "y" without " and MAKE SURE TO WRITE y

## Make 4 command line tabs
* Server - > First Tab
* Velocity - > Second Tab
* Limbo - > Third Tab
* EaglerCux - > Fourth Tab

## Commands to start the server
```bash
cd server
chmod +x server.sh
./server.sh
```
## Commands to start the Velocity proxy
```bash
cd velocity
chmod +x velocity.sh
./velocity.sh
```
## Commands to start Limbo/nLogin (Verify your players)
```bash
cd limbo
chmod +x limbo.sh
./limbo.sh
```
## Commands to start EaglerCux
```bash
cd EaglerCux
python main.py
```

## Misc Information

#### Watch Zepr's video on it

#### How to be an operator/admin in the server?

1.) Go to the Server/Backend - > First tab

2.) then type "op username" without "" and change the username to yours

> Based on EaglerXVelocity by: [IsmaelTech](https://www.youtube.com/@ismaeltechI)
