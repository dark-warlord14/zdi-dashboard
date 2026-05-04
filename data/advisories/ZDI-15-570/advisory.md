# ZDI-15-570: SQLite fts3_tokenizer Untrusted Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-570
- **ZDI-CAN:** ZDI-CAN-2888
- **Date:** 2015-11-18
- **CVE:** CVE-2015-7036
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SQLite
- **Affected Products:** SQLite
- **Credit:** Peter Rutenbar
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-570/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SQLite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the fts3_tokenizer function. The issue lies in the optional second argument which is expected to be a pointer into a structure. An attacker can leverage this vulnerability to achieve code execution under the context of the current process.

## Additional Details

SQLite has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT204942 Addressed in OS X 10.10.4 and iOS 8.4.

## Disclosure Timeline

- 2015-05-18 - Vulnerability reported to vendor
- 2015-11-18 - Coordinated public release of advisory
