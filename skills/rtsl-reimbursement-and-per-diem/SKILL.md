---
name: "rtsl-reimbursement-and-per-diem"
description: "Turn an RTSL international trip folder into copy-paste Nexonia entries for the expense report and per diem. Use for reimbursement, per diem, or Nexonia requests."
metadata:
  summary: "Turn a trip folder of receipts into copy-paste expense and per diem entries."
  category: Meetings and admin
---

# RTSL Reimbursement and Per Diem (Nexonia)

Turns a folder of travel documents into entries the person can paste straight into Nexonia, RTSL's expense tool. It covers two reports: the expense report (receipts) and the per diem report.

Scope: international trips only for now. If the trip is inside India, say this skill doesn't cover it yet and stop.

## Output rules

- Give everything in chat. Don't create an artifact or file unless asked.
- Put each entry in a plain code block so it copies cleanly.
- Memo text is plain sentences. No tables, bullets or markdown inside a memo, since the Nexonia memo field can't show them. Keep memos under 1,500 characters.
- Dates are MM/DD/YYYY.
- Write in short, plain sentences. No em dashes.

## Step 1: Read the trip folder

Read every file. Use pdftotext for PDFs. Look at images and scanned PDFs directly, since many receipts are photos (for example a sleeping pod bill or a WhatsApp boarding pass). Sort each file into:

- Receipts (become expense lines): hotel folio, taxi or Grab receipts, roaming or SIM packs, seat upgrades, airport pods or lounges, visas, and so on.
- Supporting documents (uploaded, not linked to a line): TRF, manager approval email, itinerary or visit schedule, e-tickets, boarding passes.

A Grab or Uber PDF exported from email often holds many rides. Pull out each ride's date, pickup, drop-off, booking ID and total paid. Indonesian receipts use dots as thousands separators (RP 150.100 = IDR 150,100).

## Step 2: Build the trip timeline

From the boarding passes and e-tickets, work out:

- First travel day: the day the person left home.
- Last travel day: the day they got back home.
- Days in the destination between those two days.
- Hotel nights, from the folio.
- Layovers, especially overnight ones.

## Step 3: Propose new file names (show first, don't rename yet)

Show the full list of old name to new name, then wait for approval before renaming. Use this pattern:

- Supporting documents, numbered in travel order:
  - 01_TRF_<Name>_<Country>_<MonYYYY>.docx
  - 02_Itinerary_<City>_visit_<dates>.pdf
  - 03_Approval_flight_booking_<Approver>_<date>.pdf
  - 04_Eticket_<Airline>_<Route>_<PNR>_<date>.pdf
  - 05+_BoardingPass_<Airline>_<FlightNo>_<FROM-TO>_<date>.<ext>
- Receipts:
  - R1_Receipt_<Vendor>_<What>_<date>_<CUR><amount>.<ext>

Avoid colons and slashes in names. Use mv -n so nothing gets overwritten. If the TRF is a .docx, offer to save a PDF copy too (soffice --headless --convert-to pdf). Deletion may be blocked, so flag any temp file that gets left behind.

## Step 4: Confirm a few things with the person

Ask these together in one message before building the entries:

1. Coding: Function, Enabling, Country, Grant. Defaults are your usual Function and Enabling codes, the trip's destination country, and the grant on the TRF. The grant on the TRF wins over the one on a past report (for example, if the TRF names grant code X, pick the grant that matches X). Never copy the country from an old report.
2. Travel day country for per diem: default India / Other. Always confirm it.
3. Whether they took a travel advance. If yes, get the request code and amount for the memo.
4. Hotel breakfast is assumed included. Say so, and let them correct it.

## Step 5: Expense report entries

Shared fields, stated once at the top:

- Receipt: Yes
- Paid By: Employee
- 1. Function, 2. Enabling, 3. Country, 4. Grant (from step 4)

One block per item, grouped under a heading per category:

```
Category: <dropdown value>
Date: MM/DD/YYYY
Total: <amount with 2 decimals, no commas>
Currency: <receipt currency>
Receipt: <renamed receipt file>
Memo: <plain sentences>
```

Rules:

- Enter each amount in the currency on its receipt (IDR, INR, THB, USD...). Never convert. Nexonia fills in the exchange rate. Warn if the person asks to put everything in one currency.
- One line per taxi ride, like past reports. Put the booking ID in the memo. Link the same multi-ride PDF to every ride line. If the person wants one combined line, give a plain-text list of rides in the memo, one ride per line, with the total.
- Hotel: split out any meals on the folio (room service, restaurant). Lodging = room charge + service charge + tax. Meals on the folio are covered by per diem, so leave them out of the expense report when per diem is claimed. Use Split Item if they want to enter the folio total once.
- Memos say what, where, when and why. Example: "Jakarta airport (Terminal 2) to the hotel on arrival. Grab booking A-XXXXXXXXXXXX."

Category mapping (Nexonia dropdown values):

- Hotel room: Lodging
- Airport sleeping pod or transit hotel: Lodging, with the layover times in the memo
- Taxi, Grab, Uber, airport transfer: Taxi, Car Service
- Roaming pack, local SIM: Telecommunications
- Seat upgrade, extra legroom, airline fees: Airfare
- Visa, medical, other travel costs: Travel - Other (Visa, Med, etc...)
- Train: Train
- Business meal not covered by per diem: Meal-Business (non per diem)
- Advance reconciliation: Travel Advance Rec/ Retirement

Other values seen in the dropdown: Advertising Media and Comm, Business Insurance, Conference registration, Contracts and Consulting, Coworking Space, Equipment, Hosted Wkshp Speaker Fees, Hosted Wkshp Venue, IT Svc Support Fees, Large Volume Printing, Membership & Dues, Mileage reimbursement (and country variants), RTSL Convening / Field Day / Org Meeting / Year-End Celebration items, Small Volume Printing, Software, Saas, Subscriptions & Publications, Translation Services, Travel Advance and Cash Advances.

## Step 6: Per diem entries

Per diem usually goes in its own report. Suggest a title like per_diem_<city>_<country>_visit_<dates>.

Categories:

- Travel days: Per Diem Travel Days (Non-U.S Destinations) Effective 2026
- Other days: Per Diem Days (Non-U.S.Destinations) Effective 2026

Rules:

- The first and last travel days are travel days. Tick Travel Day. Country is India / Other unless the person said otherwise in step 4.
- Every day in between is a normal day. Country is the destination, with the city as Location if it's listed, otherwise Other.
- Group days in a row that have the same meals into one line using the end date and Days.
- Hotel breakfast is included by default, so untick Breakfast on mornings after a hotel night. On the arrival day there was no hotel breakfast, so tick all meals.
- Untick any meal that was provided (by the hotel, a workshop or a host) and say so in the memo.
- Attach boarding passes to travel days, and the hotel folio plus itinerary to normal days.

Block format:

```
Category: <per diem category>
Date: MM/DD/YYYY
End date: MM/DD/YYYY
Days: <n>.00
Country: <country>
Location: <city or Other>
Travel Day: ticked (travel days only)
Meals: <which are ticked and unticked>
Attach: <file names>
Memo: This is for Oct 27-29. Breakfast was provided at hotel. Lunch and dinner were self-sponsored.
```

Nexonia fills in the rate and amount on its own, so don't calculate them.

## Step 7: Checks (list problems at the top of the reply)

- The name on each receipt matches the traveller. Airline add-on receipts sometimes carry the wrong name. If so, suggest asking the airline for a corrected receipt, and add a memo note.
- The seat or flight on an upgrade receipt matches the boarding pass.
- No meal is claimed through both a receipt and per diem.
- Every travel leg has a boarding pass. No obvious ride is missing (for example hotel to airport on the departure day).
- The grant matches the TRF.
- Note it if the visit schedule or itinerary is missing, or if the TRF's itinerary table is empty.
- Give totals per currency so the person can check them against Nexonia's subtotal.

## Step 8: Wrap up

End with what to upload through Manage Receipts (all supporting documents), then Submit. Keep the closing short.