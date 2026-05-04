# ZDI-15-151: Novell Zenworks Rtrlet doPost Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-151
- **ZDI-CAN:** ZDI-CAN-2600
- **Date:** 2015-04-22
- **CVE:** CVE-2015-0781
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-151/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Zenworks. By default, authentication is not required to exploit this vulnerability. The specific flaw exists within the doPost method of the Rtrlet class. The issue lies in the failure to sanitize the path of files uploaded, allowing files to be placed anywhere on the server. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current process.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: https://www.novell.com/support/kb/doc.php?id=7016431

## Disclosure Timeline

- 2015-01-15 - Vulnerability reported to vendor
- 2015-04-22 - Coordinated public release of advisory
