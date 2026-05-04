# ZDI-23-1053: Western Digital MyCloud PR4100 REST SDK Use of Potentially Dangerous Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1053
- **ZDI-CAN:** ZDI-CAN-19746
- **Date:** 2023-08-09
- **CVE:** N/A
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Discovered by: Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1053/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of the Western Digital MyCloud PR4100 NAS device. Authentication is required to exploit this vulnerability. The specific flaw exists within the REST SDK. The issue results from the lack of proper validation of a user-supplied string before passing it to the "call_user_function" inbuilt function. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in My Cloud Firmware Version 5.26.119

## Disclosure Timeline

- 2022-12-02 - Vulnerability reported to vendor
- 2023-08-09 - Coordinated public release of advisory
