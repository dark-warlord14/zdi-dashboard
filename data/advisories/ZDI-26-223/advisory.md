# ZDI-26-223: (Pwn2Own) Samsung Galaxy S25 Smart Touch Call Application Protection Mechanism Failure Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-223
- **ZDI-CAN:** ZDI-CAN-28331
- **Date:** 2026-03-23
- **CVE:** CVE-2025-58488
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:N/A:L
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S25
- **Credit:** Interrupt Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-223/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Samsung Galaxy S25. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of URL parameters. The issue results from the lack of protections prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungmobile.com/serviceWeb.smsb?year=2025&month=12

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-23 - Coordinated public release of advisory
- 2026-03-23 - Advisory Updated
