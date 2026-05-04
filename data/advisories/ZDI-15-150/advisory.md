# ZDI-15-150: Novell Zenworks FileViewer Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-150
- **ZDI-CAN:** ZDI-CAN-2577
- **Date:** 2015-04-22
- **CVE:** CVE-2015-0783
- **CVSS:** 3.5
- **CVSS Vector:** AV:N/AC:M/Au:S/C:P/I:N/A:N
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-150/
## Vulnerability Details

This vulnerability allows attackers to obtain sensitive information on vulnerable installations of Novell Zenworks. User interaction is not required to exploit this vulnerability. The specific flaw exists within the FileViewer class. The issue lies in the failure to sanitize the "filename" variable. The attacker can leverage this to read files remotely.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: https://www.novell.com/support/kb/doc.php?id=7016431

## Disclosure Timeline

- 2015-01-15 - Vulnerability reported to vendor
- 2015-04-22 - Coordinated public release of advisory
