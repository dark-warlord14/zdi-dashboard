# ZDI-15-290: SQLite printf Format String Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-290
- **ZDI-CAN:** ZDI-CAN-2889
- **Date:** 2015-07-01
- **CVE:** CVE-2015-3717
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SQLite
- **Affected Products:** SQLite
- **Credit:** Peter Rutenbar
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-290/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SQLite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the printf function. The issue lies in the ability to use an arbitrary format string as an argument to an insecure printf function. An attacker can leverage this vulnerability to achieve code execution under the context of the current process.

## Additional Details

SQLite has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2015-05-18 - Vulnerability reported to vendor
- 2015-07-01 - Coordinated public release of advisory
