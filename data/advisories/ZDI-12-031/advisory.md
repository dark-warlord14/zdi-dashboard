# ZDI-12-031: Novell iPrint Server attributes-natural-language Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-031
- **ZDI-CAN:** ZDI-CAN-1354
- **Date:** 2012-02-08
- **CVE:** CVE-2011-4194
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** G. Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-031/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Server. Authentication is not required to exploit this vulnerability. The flaw exists within the mod_ipp apache module component of the iprint-server, which listens by default on 631/tcp. During the handling of get-printer-attributes requests containing a attributes-natural-language attribute cause a validation routine to be hit. When validating this parameter the contents of the attribute are copied, without validation, to a fixed length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7010084

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-02-08 - Coordinated public release of advisory
