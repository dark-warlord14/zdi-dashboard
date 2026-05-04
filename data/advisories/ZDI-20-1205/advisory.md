# ZDI-20-1205: Microhard Bullet-LTE Ping Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1205
- **ZDI-CAN:** ZDI-CAN-10595
- **Date:** 2020-08-26
- **CVE:** CVE-2020-17406
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microhard
- **Affected Products:** Bullet-LTE
- **Credit:** Ricky "HeadlessZeke" Lawshae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1205/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microhard Bullet-LTE. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of the ping parameter provided to tools.sh. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in R112

## Disclosure Timeline

- 2020-03-03 - Vulnerability reported to vendor
- 2020-08-26 - Coordinated public release of advisory
- 2020-09-17 - Advisory Updated
