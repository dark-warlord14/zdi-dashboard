# ZDI-23-1052: Western Digital MyCloud PR4100 Logger Class Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1052
- **ZDI-CAN:** ZDI-CAN-19745
- **Date:** 2023-08-09
- **CVE:** N/A
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Discovered by: Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1052/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of the Western Digital MyCloud PR4100 NAS device. Authentication is required to exploit this vulnerability. The specific flaw exists within the Logger class. The issue results from the lack of proper validation of a user-supplied string before using it to perform an exec call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in My Cloud Firmware Version 5.26.119

## Disclosure Timeline

- 2022-12-02 - Vulnerability reported to vendor
- 2023-08-09 - Coordinated public release of advisory
