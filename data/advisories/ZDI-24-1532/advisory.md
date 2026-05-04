# ZDI-24-1532: 7-Zip Zstandard Decompression Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1532
- **ZDI-CAN:** ZDI-CAN-24346
- **Date:** 2024-11-20
- **CVE:** CVE-2024-11477
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** 7-Zip
- **Affected Products:** 7-Zip
- **Credit:** Nicholas Zubrisky (@NZubrisky) of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1532/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of 7-Zip. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the implementation of Zstandard decompression. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in fixed in 7-Zip 24.07

## Disclosure Timeline

- 2024-06-12 - Vulnerability reported to vendor
- 2024-11-20 - Coordinated public release of advisory
- 2024-11-20 - Advisory Updated
