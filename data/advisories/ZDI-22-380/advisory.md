# ZDI-22-380: (Pwn2Own) Samsung Galaxy S21 Improper Error Handling Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-380
- **ZDI-CAN:** ZDI-CAN-15916
- **Date:** 2022-02-18
- **CVE:** N/A
- **CVSS:** 4.6
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S21
- **Credit:** TBD
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-380/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Samsung Galaxy S21 phones. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the handling of errors when accessing trusted URLs. An attacker can force a page redirection from HTTPS to HTTP. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current user.

## Additional Details

The patch was applied in server side on November 30th, 2021

## Disclosure Timeline

- 2021-12-30 - Vulnerability reported to vendor
- 2022-02-18 - Coordinated public release of advisory
