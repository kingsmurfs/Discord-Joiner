import tls_client
import ctypes
import time

from colorama import Fore, Style, init

init(autoreset=True)  # Start colorama

class DiscordJoiner():
    def __init__(self):
        # Counters
        self.joined = 0
        self.failed = 0
        
        # Request Config
        self.proxy = '' # Proxy format: user:pass@host:port   [use residential proxies]
        self.session = tls_client.Session(client_identifier="chrome_124", random_tls_extension_order=True)
        self.session.proxies = {"http": f"http://{self.proxy}", "https": f"https://{self.proxy}"}
        
        # User Config
        self.token = '' # Put token account
        self.invite = '' # Put invite server, only code. Dont use discord.gg/fortnite  -->  use: fortnite
        
    def update_console_title(self):
        try:
            ctypes.windll.kernel32.SetConsoleTitleW(
                f"Discord Token Joiner | Joined: {self.joined} | Failed: {self.failed} |    DevBy: kingsmurfs") # Console Title
        except Exception as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)
            
    def get_discord_cookies(self):
        try:            
            response = self.session.get("https://discord.com")
            match response.status_code:
                case 200:
                    return "; ".join(
                        [f"{cookie.name}={cookie.value}" for cookie in response.cookies]
                    ) + "; locale=en-US"
                case _:
                    return "__dcfduid=4e0a8d504a4411eeb88f7f88fbb5d20a; __sdcfduid=4e0a8d514a4411eeb88f7f88fbb5d20ac488cd4896dae6574aaa7fbfb35f5b22b405bbd931fdcb72c21f85b263f61400; __cfruid=f6965e2d30c244553ff3d4203a1bfdabfcf351bd-1699536665; _cfuvid=rNaPQ7x_qcBwEhO_jNgXapOMoUIV2N8FA_8lzPV89oM-1699536665234-0-604800000; locale=en-US"
        except Exception as e:
            print(e)
    
    def headers_joiner(self):
        return {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'pt-BR,pt;q=0.6',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'authorization': self.token,
            'content-type': 'application/json',
            'cookie': self.get_discord_cookies(),
            'Dnt': '1',
            'Origin': 'https://discord.com',
            'Priority': 'u=1, i',
            'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjExMzM1MDYzMjU2MDM2ODQ1MzQiLCJsb2NhdGlvbl9jaGFubmVsX2lkIjoiMTEzMzU3Nzk4OTQxODkyNjEyMSIsImxvY2F0aW9uX2NoYW5uZWxfdHlwZSI6MH0=',
            'x-discord-timezone': 'America/Sao_Paulo',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InB0LUJSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI5MTk2MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
        }
    
    def joiner(self):
        try:
            print(f"{Fore.CYAN}(+) Starting Joiner{Style.RESET_ALL}  --->  {Fore.CYAN}Token:{Style.RESET_ALL} {self.token}  --->  {Fore.CYAN}Server:{Style.RESET_ALL} {self.invite}")
            headers = self.headers_joiner()
            joiner = self.session.post(f"https://discord.com/api/v9/invites/{self.invite}", headers=headers, json={})
            if joiner.status_code != 200:
                print(f"{Fore.RED}(-) Join Failed Error:{Style.RESET_ALL} {joiner.text}")
                self.failed += 1
                self.update_console_title()
                time.sleep(5)
            else:
                print(f"{Fore.GREEN}(+) Token Joined:{Style.RESET_ALL} {self.token[:40]}  --->  {Fore.GREEN}Server:{Style.RESET_ALL} {self.invite}")
                self.joined += 1
                self.update_console_title()
                time.sleep(5)   
        except:
            print(f"Function Exit")
    
    def main(self):
        self.update_console_title()
        self.joiner()

if __name__ == "__main__":
    joiner = DiscordJoiner()
    joiner.main()
