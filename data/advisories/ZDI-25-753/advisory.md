# ZDI-25-753: (Pwn2Own) QNAP TS-464 Improper Handling of URL Encoding Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-753
- **ZDI-CAN:** ZDI-CAN-25482
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** Chris Anastasio @mufinnnnnnn & Fabius Watson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-753/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of QNAP TS-464 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the function responsible for URL decoding. The issue results from improper implementation of the decoding algorithm. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
