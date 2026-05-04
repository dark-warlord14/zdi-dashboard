# ZDI-13-258: Novell ZENworks umaninv Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-258
- **ZDI-CAN:** ZDI-CAN-1790
- **Date:** 2013-11-24
- **CVE:** CVE-2013-1084
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Brett Gervasoni
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-258/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENworks. Authentication is not required to exploit this vulnerability. The specific flaw exists within the unmaninv web service. The issue lies in the failure to user-supplied sanitize input when returning the contents of a file. An attacker can leverage this vulnerability to retrieve credentials which can then be leveraged to execute code under the context of SYSTEM.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/kb/doc.php?id=7012760

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-11-24 - Coordinated public release of advisory
