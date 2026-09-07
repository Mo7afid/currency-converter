# Currency Converter CLI

A simple interactive command-line tool written in Python for fetching live exchange rates and converting between Moroccan Dirham (MAD), Euro (EUR), and US Dollar (USD).

The script retrieves reference exchange rates directly from the Frankfurter API and provides a terminal-based interactive menu for quick rate checks and conversions.

---

## Features

- Live exchange rate lookup for EUR/MAD and USD/MAD.
- Bidirectional currency conversion:
  - Euro (EUR) to Moroccan Dirham (MAD)
  - US Dollar (USD) to Moroccan Dirham (MAD)
  - Moroccan Dirham (MAD) to Euro (EUR)
  - Moroccan Dirham (MAD) to US Dollar (USD)
- Automatic handling for network and connection errors.
- Clean terminal-based menu interface.

---

## Prerequisites

- Python 3.6+
- `requests` library

You can install the required dependency using `pip`:

```bash
pip install requests
```

---

## How to Run

1. Clone or download `currency.py`.
2. Run the script from your terminal:

```bash
python currency.py
```

---

## Usage Example

When you run the script, an interactive menu will appear:

```text
enter your choice number
1:View exchange rates
2:Convert currency 
3:exit
your choice: 
```

### Viewing Rates
Selecting option `1` displays the date and the current exchange rates:

```text
date:2026-09-07
1 euro = 10.82dh
1 usd = 9.85dh
```

### Converting Amounts
Selecting option `2` opens the conversion menu:

```text
enter your choice number
1:from euro to mad
2:from usd to mad 
3:from mad to euro
4:from mad to usd
```

Enter your desired conversion choice, followed by the amount when prompted.

---

## Code Architecture

The script is organized into distinct functions:

- `main()`: Manages the CLI execution flow, menu navigation, input validation, and user pauses.
- `api()`: Sends GET requests to the Frankfurter API endpoints to fetch base rates for `EUR` and `USD` relative to `MAD`.
- `print_rates(data1, data2)`: Formats and displays current exchange rates alongside the rate date.
- `euro_to_mad(data1, num)`: Converts Euro amount to MAD.
- `usd_to_mad(data2, num)`: Converts USD amount to MAD.
- `mad_to_euro(data1, num)`: Converts MAD amount to Euro.
- `mad_to_usd(data2, num)`: Converts MAD amount to USD.

---

## Data Source

Exchange rate data is provided by the public [Frankfurter API](https://www.frankfurter.app/), which tracks European Central Bank reference exchange rates. No API key required.

---

## License

Open-source under the MIT License.
