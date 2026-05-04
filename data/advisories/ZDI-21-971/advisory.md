# ZDI-21-971: (Pwn2Own) Zoom Heap based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-971
- **ZDI-CAN:** ZDI-CAN-13587
- **Date:** 2021-08-17
- **CVE:** CVE-2021-34407
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Zoom
- **Affected Products:** Client
- **Credit:** Daan Keuper and Thijs Alkemade from Computest
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-971/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Zoom Clients. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of encrypted messages. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Zoom has issued an update to correct this vulnerability. More details can be found at: https://explore.zoom.us/en/trust/security/security-bulletin/

## Disclosure Timeline

- 2021-04-07 - Vulnerability reported to vendor
- 2021-08-17 - Coordinated public release of advisory
