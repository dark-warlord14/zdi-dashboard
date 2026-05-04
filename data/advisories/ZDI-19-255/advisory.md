# ZDI-19-255: (Pwn2Own) Samsung Galaxy S9 GameServiceReceiver Unsafe Updates Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-255
- **ZDI-CAN:** ZDI-CAN-7477
- **Date:** 2019-03-05
- **CVE:** CVE-2019-6742
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S9
- **Credit:** MWR Labs - Georgi Geshev and Robert Miller
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-255/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung Galaxy S9. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the GameServiceReceiver update mechanism. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 1.4.20.2 or above

## Disclosure Timeline

- 2018-11-15 - Vulnerability reported to vendor
- 2019-03-05 - Coordinated public release of advisory
- 2019-06-14 - Advisory Updated
