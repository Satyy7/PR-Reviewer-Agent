from app.services.langfuse_service import (
    langfuse
)

print(type(langfuse))

print("\nMethods:\n")

for item in dir(langfuse):
    if not item.startswith("_"):
        print(item)