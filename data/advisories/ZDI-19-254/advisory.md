# ZDI-19-254: (Pwn2Own) Samsung Galaxy S9 Untrusted Site Redirection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-254
- **ZDI-CAN:** ZDI-CAN-7476
- **Date:** 2019-03-05
- **CVE:** CVE-2019-6741
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S9
- **Credit:** MWR Labs - Georgi Geshev and Robert Miller
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-254/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung Galaxy S9. User interaction is required to exploit this vulnerability in that the target must connect to a wireless network. The specific flaw exists within the captive portal. By manipulating HTML, an attacker can force a page redirection. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in January 2019 Security Update (SMR-JAN-2019 - SVE-2018-13474)

## Disclosure Timeline

- 2018-11-15 - Vulnerability reported to vendor
- 2019-03-05 - Coordinated public release of advisory
- 2019-06-14 - Advisory Updated
