# Online Responses Setup (GitHub Pages)

Your current site is static on GitHub Pages, so `server.py` does not run there.
To get real responses online, connect the page to a Google Form.

## 1) Create a Google Form

Create a form with these **Short answer** fields:

1. `submittedAt`
2. `picksJson`
3. `suggestedGift`
4. `suggestedDescription`
5. `finalWish`
6. `skippedWishInput`
7. `starterPlanJson`

Responses will automatically be available in the Google Form responses tab (or linked Google Sheet).

## 2) Get form action URL

1. Open the form.
2. Click the three dots (top-right) -> `Get pre-filled link`.
3. Fill anything in every field and click `Get link`.
4. Open that pre-filled link in a browser.
5. View page source and find:
   - `form action="https://docs.google.com/forms/d/e/.../formResponse"`
6. Copy that full `formResponse` URL.

## 3) Get each `entry.xxxxx` field id

In the same page source, find each `entry.` id next to your questions.

Map them inside:
- `index.html`
- `ONLINE_RESPONSE_CONFIG.googleForm.formAction`
- `ONLINE_RESPONSE_CONFIG.googleForm.fields.*`

## 4) Commit and push

After replacing placeholders in `index.html`, push to GitHub.

## 5) Test

1. Open your GitHub Pages link.
2. Submit one test response.
3. Check Google Form responses.

## Notes

- The page also saves a backup in local browser storage under key:
  - `birthday_gift_quest_responses_v1`
- If online config is missing, the page shows a small owner note.
