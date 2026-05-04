# ZDI-22-379: (Pwn2Own) Samsung Galaxy S21 Open Redirect Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-379
- **ZDI-CAN:** ZDI-CAN-15871
- **Date:** 2022-02-18
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S21
- **Credit:** Sam Thomas (@_s_n_t) of Pentest Ltd (@pentestltd)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-379/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Samsung Galaxy S21 phones. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Galaxy Store. By manipulating client-side HTML, an attacker can redirect the web view to an arbitrary site. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

The patch was applied in server side on November 9th, 2021

## Disclosure Timeline

- 2022-01-21 - Vulnerability reported to vendor
- 2022-02-18 - Coordinated public release of advisory
