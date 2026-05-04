# ZDI-16-167: Novell Zenworks ChangePassword XPath Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-167
- **ZDI-CAN:** ZDI-CAN-3136
- **Date:** 2016-02-11
- **CVE:** CVE-2015-5970
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** cpnrodzc7
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-167/
## Vulnerability Details

This vulnerability allows remote attackers to exfiltrate arbitrary text files on vulnerable installations of Novell Zenworks. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ChangePassword RPC method. By providing a malformed query, an attacker can combine a system entity reference with an XPath injection vulnerability to exfiltrate arbitrary text files from the system.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: https://www.novell.com/support/kb/doc.php?id=7017240

## Disclosure Timeline

- 2015-09-17 - Vulnerability reported to vendor
- 2016-02-11 - Coordinated public release of advisory
