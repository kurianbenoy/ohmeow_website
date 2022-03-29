import sys, re
logs = sys.stdin.read()

draft_url = re.findall(r'Website Draft URL: .*(https://.*)', logs)[0]
assert draft_url, 'Was not able to find Draft URL in the logs:\n{}'.format(logs)
print(f"::set-output name=draft_url::{draft_url}")

