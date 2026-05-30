from config import settings

settings.validate()

print("Config loaded successfully!")
print(f"Country: {settings.ADZUNA_COUNTRY}")
print(f"Results per page: {settings.RESULTS_PER_PAGE}")
print(f"Max pages: {settings.MAX_PAGES}")
print(f"App ID loaded: {'Yes' if settings.ADZUNA_APP_ID else 'No'}")
print(f"App Key loaded: {'Yes' if settings.ADZUNA_APP_KEY else 'No'}")