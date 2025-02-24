import names
import requests
import time
import random
from eth_account import Account
from fake_useragent import UserAgent

def generate_eth_wallet():
    account = Account.create()
    private_key = account._private_key.hex()
    public_key = account.address
    return public_key, private_key

def generate_twitter_name():
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    numbers = str(random.randint(100, 999))
    return f"{first_name}{last_name}{numbers}"

def register(wallet, twitter, invite):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,id;q=0.7",
        "Origin": "https://agentmoana.xyz",
        "Priority": "u=1",
        "Referer": "https://agentmoana.xyz/",
        "Sec-CH-UA": '"Not A;Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": UserAgent().random
    }
    payload = {
        "wallet": wallet,
        "twitter": twitter,
        "invite": invite
    }
    response = requests.post("https://moana-y43h.onrender.com/user", json=payload, headers=headers, timeout=30)
    data = response.json()
    
    # Log the full response for debugging
    #print("API Response:", data)
    
    if data.get("success"):
        return data.get("user", {})
    else:
        return None

def main():
    print("Auto Referral Moana by @AirdropFamilyIDN")
    invite = input("Enter your referral code: ")
    iterations = int(input("Mau berapa referral: "))
    success_count = 0
    failed_count = 0
    for _ in range(iterations):
        print(f"\nProcessing referral {_+1}/{iterations}")
        public_key, private_key = generate_eth_wallet()
        wallet = public_key
        twitter_name = generate_twitter_name()
        print(f"Your generated Twitter handle is {twitter_name}.")
        twitter = twitter_name
        user_data = register(wallet, twitter, invite)
        if user_data:
            print(f"Registration successful! Your user ID is {user_data['_id']}")
            print(f"Join Group https://t.me/AirdropFamilyIDN")
            success_count += 1
        else:
            print("Registration failed. Please try again later.")
            failed_count += 1
        time.sleep(5)
    

    print(f"\nTotal referral sukses: {success_count}")
    print(f"Total referral gagal : {failed_count}")

if __name__ == "__main__":
    main()