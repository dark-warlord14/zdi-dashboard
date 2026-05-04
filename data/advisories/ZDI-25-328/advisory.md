# ZDI-25-328: (0Day) (Pwn2Own) WOLFBOX Level 2 EV Charger BLE Encryption Keys Uninitialized Variable Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-328
- **ZDI-CAN:** ZDI-CAN-26295
- **Date:** 2025-06-06
- **CVE:** CVE-2025-5749
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** WOLFBOX
- **Affected Products:** Level 2 EV Charger
- **Credit:** Tobias Scharnowski, Felix Buchmann, and Kristian Covic of fuzzware.io
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-328/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of WOLFBOX Level 2 EV Charger devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of cryptographic keys used in vendor-specific encrypted communications. The issue results from the lack of proper initialization of a variable prior to accessing it. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

ZDI made several attempts to contact the vendor using the contact information on their website, as well as trying to reach them on various social platforms which yielded no response. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-03-10 - Vulnerability reported to vendor
- 2025-06-06 - Coordinated public release of advisory
- 2025-06-06 - Advisory Updated
