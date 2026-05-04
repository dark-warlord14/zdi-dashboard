# ZDI-24-828: (Pwn2Own) Samsung Galaxy S23 instantgame Improper Input Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-828
- **ZDI-CAN:** ZDI-CAN-22441
- **Date:** 2024-06-21
- **CVE:** CVE-2023-42580
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S23
- **Credit:** @_s_n_t of @pentestltd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-828/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Samsung Galaxy S23 smartphones. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the InstantPlaysUrlUtil class. The issue results from a logical error when checking the safety of URIs. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungmobile.com/serviceWeb.smsb?year=2023&month=12

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
