# ZDI-13-189: Novell iPrint Client op-client-interface-version Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-189
- **ZDI-CAN:** ZDI-CAN-1533
- **Date:** 2013-08-13
- **CVE:** CVE-2012-0411
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** Brian Gorenc HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-189/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ienipp.ocx ActiveX object. A vulnerability exists in the op-client-interface-version operation, which takes two strings as parameters. When these strings are combined to create the response url, Novell iPrint copies this string to a fixed-length buffer on the stack. This can lead to memory corruption which can be leveraged to execute code under the context of the process.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/kb/doc.php?id=7008708

## Disclosure Timeline

- 2012-03-14 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
