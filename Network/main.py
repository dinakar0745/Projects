import shodan

# Replace 'YOUR_SHODAN_API_KEY' with your actual Shodan API key
SHODAN_API_KEY = 'z0J2cylBQAiLoeU2z0B0HAFuFsdcXbOf'

def shodan_info(ip_address):
    # Initialize Shodan API client
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        # Get information about the specified IP address
        host_info = api.host(ip_address)

        # Print general information
        print(f"IP Address: {host_info['ip_str']}")
        print(f"Organization: {host_info.get('org', 'N/A')}")
        print(f"Operating System: {host_info.get('os', 'N/A')}")
        print(f"Hostnames: {', '.join(host_info.get('hostnames', ['N/A']))}")
        
        # Print open ports, protocols, and vulnerabilities
        print("\nOpen Ports:")
        for item in host_info['data']:
            print(f"  Port: {item['port']}")
            print(f"  Protocol: {item['transport']}")
            print(f"  Vulnerabilities:")
            for vuln in item.get('vulns', []):
                print(f"    - {vuln}")
            print()

    except shodan.APIError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'TARGET_IP_ADDRESS' with the IP address you want to query
    target_ip = '14.192.0.9'
    shodan_info(target_ip)
