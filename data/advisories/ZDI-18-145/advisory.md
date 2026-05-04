# ZDI-18-145: Novell NetIQ Access Manager FwRequest Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-145
- **ZDI-CAN:** ZDI-CAN-5088
- **Date:** 2018-02-06
- **CVE:** CVE-2018-1342
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** NetIQ Access Manager
- **Credit:** Ariele Caltabiano (kimiya) and rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-145/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell NetIQ Access Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FwRequest class. The issue results from the lack of proper validation of user-supplied data, which can allow for the upload of arbitrary files. An attacker can leverage this to execute code in the context of the current process.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: https://www.netiq.com/support/kb/doc.php?id=7022444

## Disclosure Timeline

- 2017-08-21 - Vulnerability reported to vendor
- 2018-02-06 - Coordinated public release of advisory
- 2018-02-06 - Advisory Updated
